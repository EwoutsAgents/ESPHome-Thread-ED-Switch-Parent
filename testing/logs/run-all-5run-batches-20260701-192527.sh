#!/usr/bin/env bash
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
TESTING_DIR="$REPO_ROOT/testing"
CAMPAIGN_SCRIPT_REL="testing/logs/$(basename "$0")"
CAMPAIGN_LOG_REL="testing/logs/$(basename "$0" .sh).log"
BRANCH_NAME="main"

log() {
  printf '[%s] %s\n' "$(date -Is)" "$*"
}

find_newest_batch_dir() {
  local variant="$1"
  local routers="$2"
  find "$TESTING_DIR/logs" -maxdepth 1 -type d -name "${variant}-${routers}router-5runs-*" | sort | tail -n 1
}

write_large_file_note() {
  local batch_dir="$1"
  local note_path="$batch_dir/push-excluded-files.md"
  shift
  {
    printf '# Push exclusions\n\n'
    printf 'Git push rejected one or more large capture files. They remain local and were excluded from the pushed commit.\n\n'
    printf 'Excluded files:\n'
    for file in "$@"; do
      printf -- '- `%s`\n' "${file#$REPO_ROOT/}"
    done
  } >"$note_path"
}

commit_and_push_batch() {
  local variant="$1"
  local routers="$2"
  local batch_dir="$3"
  local commit_msg="Add ${variant} ${routers}router 5-run batch"
  local push_output

  git -C "$REPO_ROOT" status --short
  git -C "$REPO_ROOT" add "$batch_dir" "$CAMPAIGN_SCRIPT_REL" "$CAMPAIGN_LOG_REL"

  if git -C "$REPO_ROOT" diff --cached --quiet; then
    log "No staged artifacts for ${variant} ${routers}router; skipping commit"
    return 0
  fi

  if ! git -C "$REPO_ROOT" commit -m "$commit_msg"; then
    log "ERROR: git commit failed for ${variant} ${routers}router"
    return 1
  fi

  push_output="$(git -C "$REPO_ROOT" push origin "$BRANCH_NAME" 2>&1)"
  local push_rc=$?
  printf '%s\n' "$push_output"
  if [[ $push_rc -eq 0 ]]; then
    log "Pushed batch commit for ${variant} ${routers}router"
    return 0
  fi

  if grep -Eiq 'GH001|file.*larger than|pack exceeds|large files detected' <<<"$push_output"; then
    log "Push rejected due to large files for ${variant} ${routers}router; retrying without .pcapng artifacts"
    git -C "$REPO_ROOT" reset --soft HEAD~1

    mapfile -t pcap_files < <(find "$batch_dir" -type f -name '*.pcapng' | sort)
    if [[ ${#pcap_files[@]} -eq 0 ]]; then
      log "ERROR: push looked like a large-file rejection, but no .pcapng files were found in $batch_dir"
      return 1
    fi

    git -C "$REPO_ROOT" reset
    git -C "$REPO_ROOT" add "$batch_dir" "$CAMPAIGN_SCRIPT_REL" "$CAMPAIGN_LOG_REL"
    for pcap in "${pcap_files[@]}"; do
      git -C "$REPO_ROOT" reset -q -- "$pcap"
    done

    write_large_file_note "$batch_dir" "${pcap_files[@]}"
    git -C "$REPO_ROOT" add "$batch_dir/push-excluded-files.md"

    if ! git -C "$REPO_ROOT" commit -m "$commit_msg"; then
      log "ERROR: git commit failed after excluding large files for ${variant} ${routers}router"
      return 1
    fi

    push_output="$(git -C "$REPO_ROOT" push origin "$BRANCH_NAME" 2>&1)"
    push_rc=$?
    printf '%s\n' "$push_output"
    if [[ $push_rc -eq 0 ]]; then
      log "Pushed reduced batch commit for ${variant} ${routers}router after excluding large files"
      return 0
    fi
  fi

  log "ERROR: git push failed for ${variant} ${routers}router"
  return 1
}

run_and_commit_batch() {
  local variant="$1"
  local routers="$2"
  local wrapper="$3"
  local config="$4"

  log "Starting batch: variant=${variant} routers=${routers} config=${config}"

  local run_rc=0
  "$TESTING_DIR/$wrapper" --config "$config" --runs 5 || run_rc=$?

  local batch_dir
  batch_dir="$(find_newest_batch_dir "$variant" "$routers")"
  if [[ -z "$batch_dir" || ! -d "$batch_dir" ]]; then
    log "ERROR: could not determine batch directory for ${variant} ${routers}router"
    return 1
  fi

  log "Batch directory: ${batch_dir#$REPO_ROOT/}"

  local analysis_rc=0
  (cd "$TESTING_DIR" && python3 scripts/analyze_test_logs.py --logs-dir "${batch_dir#$TESTING_DIR/}" --write-markdown) || analysis_rc=$?

  if [[ $run_rc -ne 0 ]]; then
    log "WARNING: runner exited with rc=${run_rc} for ${variant} ${routers}router"
  fi
  if [[ $analysis_rc -ne 0 ]]; then
    log "WARNING: analysis exited with rc=${analysis_rc} for ${variant} ${routers}router"
  fi

  if ! commit_and_push_batch "$variant" "$routers" "$batch_dir"; then
    return 1
  fi

  log "Completed batch: variant=${variant} routers=${routers}"
  return 0
}

systemic_preflight() {
  command -v git >/dev/null 2>&1 || { log "ERROR: git not found"; return 1; }
  command -v setsid >/dev/null 2>&1 || { log "ERROR: setsid not found"; return 1; }
  command -v python3 >/dev/null 2>&1 || { log "ERROR: python3 not found"; return 1; }

  [[ -x "$TESTING_DIR/run_stock_test.sh" ]] || { log "ERROR: missing runner run_stock_test.sh"; return 1; }
  [[ -x "$TESTING_DIR/run_ucast_test.sh" ]] || { log "ERROR: missing runner run_ucast_test.sh"; return 1; }
  [[ -x "$TESTING_DIR/run_ucast_fastpr_test.sh" ]] || { log "ERROR: missing runner run_ucast_fastpr_test.sh"; return 1; }
  [[ -x "$TESTING_DIR/run_mcast_test.sh" ]] || { log "ERROR: missing runner run_mcast_test.sh"; return 1; }
  [[ -f "$TESTING_DIR/scripts/analyze_test_logs.py" ]] || { log "ERROR: missing analyzer script"; return 1; }

  local cfg
  for cfg in \
    stock_test_devices_2routers.toml stock_test_devices_3routers.toml stock_test_devices_4routers.toml \
    ucast_test_devices_2routers.toml ucast_test_devices_3routers.toml ucast_test_devices_4routers.toml \
    ucast_fastpr_test_devices_2routers.toml ucast_fastpr_test_devices_3routers.toml ucast_fastpr_test_devices_4routers.toml \
    mcast_test_devices_2routers.toml mcast_test_devices_3routers.toml mcast_test_devices_4routers.toml; do
    [[ -f "$TESTING_DIR/$cfg" ]] || { log "ERROR: missing config $cfg"; return 1; }
  done

  if ! git -C "$REPO_ROOT" diff --quiet || ! git -C "$REPO_ROOT" diff --cached --quiet; then
    log "ERROR: repo has tracked changes before campaign start"
    git -C "$REPO_ROOT" status --short
    return 1
  fi

  return 0
}

main() {
  mkdir -p "$TESTING_DIR/logs"
  log "Campaign script: $CAMPAIGN_SCRIPT_REL"
  log "Campaign log: $CAMPAIGN_LOG_REL"
  log "Repo root: $REPO_ROOT"

  if ! systemic_preflight; then
    exit 1
  fi

  run_and_commit_batch "stock" "2" "run_stock_test.sh" "stock_test_devices_2routers.toml" || exit 1
  run_and_commit_batch "stock" "3" "run_stock_test.sh" "stock_test_devices_3routers.toml" || exit 1
  run_and_commit_batch "stock" "4" "run_stock_test.sh" "stock_test_devices_4routers.toml" || exit 1

  run_and_commit_batch "ucast" "2" "run_ucast_test.sh" "ucast_test_devices_2routers.toml" || exit 1
  run_and_commit_batch "ucast" "3" "run_ucast_test.sh" "ucast_test_devices_3routers.toml" || exit 1
  run_and_commit_batch "ucast" "4" "run_ucast_test.sh" "ucast_test_devices_4routers.toml" || exit 1

  run_and_commit_batch "ucast_fastpr" "2" "run_ucast_fastpr_test.sh" "ucast_fastpr_test_devices_2routers.toml" || exit 1
  run_and_commit_batch "ucast_fastpr" "3" "run_ucast_fastpr_test.sh" "ucast_fastpr_test_devices_3routers.toml" || exit 1
  run_and_commit_batch "ucast_fastpr" "4" "run_ucast_fastpr_test.sh" "ucast_fastpr_test_devices_4routers.toml" || exit 1

  run_and_commit_batch "mcast" "2" "run_mcast_test.sh" "mcast_test_devices_2routers.toml" || exit 1
  run_and_commit_batch "mcast" "3" "run_mcast_test.sh" "mcast_test_devices_3routers.toml" || exit 1
  run_and_commit_batch "mcast" "4" "run_mcast_test.sh" "mcast_test_devices_4routers.toml" || exit 1

  log "All requested 5-run batches completed."
}

main "$@"
