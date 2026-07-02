#!/usr/bin/env bash
set -u -o pipefail

log() {
  printf '[%s] %s\n' "$(date -Is)" "$*"
}

is_expected_dirty_line() {
  local line="$1"
  case "$line" in
    *" logs/"*) return 0 ;;
    *"testing/logs/"*) return 0 ;;
  esac
  return 1
}

check_initial_git_state() {
  local status
  status="$(git status --short || true)"
  if [[ -z "$status" ]]; then
    log "Initial git status clean."
    return 0
  fi
  log "Initial git status:"
  printf '%s\n' "$status"
  while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    if ! is_expected_dirty_line "$line"; then
      log "ERROR: unexpected dirty git entry before campaign: $line"
      return 1
    fi
  done <<< "$status"
  log "Initial git dirt is limited to logs artifacts; proceeding."
}

stage_batch_artifacts() {
  local batch_dir="$1"
  local note_file="$batch_dir/PCAP_EXCLUSIONS.md"
  local excluded=0
  local threshold_bytes=$((95 * 1024 * 1024))
  local -a excluded_files=()

  while IFS= read -r -d '' file; do
    local size
    size="$(stat -c '%s' "$file")"
    if (( size > threshold_bytes )); then
      excluded=1
      excluded_files+=("$(basename "$file") size=${size}")
      log "Excluding large pcapng from git add: $file (${size} bytes)"
    else
      git add "$file"
    fi
  done < <(find "$batch_dir" -type f -name '*.pcapng' -print0)

  while IFS= read -r -d '' file; do
    git add "$file"
  done < <(find "$batch_dir" -type f ! -name '*.pcapng' -print0)

  if (( excluded )); then
    {
      echo "# Excluded capture files"
      echo
      echo "These local capture files were excluded from the Git commit because they exceeded the campaign size threshold and were likely to cause push rejection:"
      echo
      for entry in "${excluded_files[@]}"; do
        echo "- ${entry}"
      done
    } > "$note_file"
    git add "$note_file"
  fi
}

run_and_commit_batch() {
  local variant="$1"
  local router_count="$2"
  local wrapper="$3"
  local config="$4"
  local batch_glob="$5"

  log "Starting batch: variant=${variant} routers=${router_count} config=${config}"

  local before_file after_file batch_dir run_rc analysis_rc
  before_file="$(mktemp)"
  after_file="$(mktemp)"
  find logs -maxdepth 1 -type d -name "${batch_glob}" -print | sort > "$before_file"

  run_rc=0
  "./${wrapper}" --config "${config}" --runs 5 || run_rc=$?

  find logs -maxdepth 1 -type d -name "${batch_glob}" -print | sort > "$after_file"
  batch_dir="$(comm -13 "$before_file" "$after_file" | tail -n 1)"
  rm -f "$before_file" "$after_file"

  if [[ -z "$batch_dir" ]]; then
    batch_dir="$(find logs -maxdepth 1 -type d -name "${batch_glob}" -print | sort | tail -n 1)"
  fi

  if [[ -z "$batch_dir" || ! -d "$batch_dir" ]]; then
    log "ERROR: could not determine batch directory for ${variant} ${router_count}router"
    return 1
  fi

  log "Batch directory: ${batch_dir}"

  analysis_rc=0
  python3 scripts/analyze_test_logs.py --logs-dir "$batch_dir" --write-markdown || analysis_rc=$?

  if [[ "$run_rc" -ne 0 ]]; then
    log "WARNING: runner exited with rc=${run_rc} for ${variant} ${router_count}router"
  fi
  if [[ "$analysis_rc" -ne 0 ]]; then
    log "WARNING: analysis exited with rc=${analysis_rc} for ${variant} ${router_count}router"
  fi

  git status --short
  stage_batch_artifacts "$batch_dir"

  if git diff --cached --quiet; then
    log "No staged artifacts for ${variant} ${router_count}router; skipping commit"
  else
    git commit -m "Add ${variant} ${router_count}router 5-run batch"
    local sha
    sha="$(git rev-parse HEAD)"
    log "Committed ${sha} for ${variant} ${router_count}router"
    if ! git push; then
      log "ERROR: git push failed for ${variant} ${router_count}router"
      return 1
    fi
    log "Pushed ${sha} for ${variant} ${router_count}router"
  fi

  log "Completed batch: variant=${variant} routers=${router_count} run_rc=${run_rc} analysis_rc=${analysis_rc}"
  return 0
}

cd "$(cd "$(dirname "$0")/.." && pwd)"
log "Campaign working directory: $PWD"

check_initial_git_state || exit 1

for path in ./run_ucast_test.sh ./run_ucast_fastpr_test.sh ./run_mcast_test.sh scripts/analyze_test_logs.py \
  ucast_test_devices_2routers.toml ucast_test_devices_3routers.toml ucast_test_devices_4routers.toml \
  ucast_fastpr_test_devices_2routers.toml ucast_fastpr_test_devices_3routers.toml ucast_fastpr_test_devices_4routers.toml \
  mcast_test_devices_2routers.toml mcast_test_devices_3routers.toml mcast_test_devices_4routers.toml; do
  if [[ ! -e "$path" ]]; then
    log "ERROR: required path missing: $path"
    exit 1
  fi
done

run_and_commit_batch "ucast" "2" "run_ucast_test.sh" "ucast_test_devices_2routers.toml" "ucast-2router-5runs-*" || exit 1
run_and_commit_batch "ucast" "3" "run_ucast_test.sh" "ucast_test_devices_3routers.toml" "ucast-3router-5runs-*" || exit 1
run_and_commit_batch "ucast" "4" "run_ucast_test.sh" "ucast_test_devices_4routers.toml" "ucast-4router-5runs-*" || exit 1
run_and_commit_batch "ucast_fastpr" "2" "run_ucast_fastpr_test.sh" "ucast_fastpr_test_devices_2routers.toml" "ucast_fastpr-2router-5runs-*" || exit 1
run_and_commit_batch "ucast_fastpr" "3" "run_ucast_fastpr_test.sh" "ucast_fastpr_test_devices_3routers.toml" "ucast_fastpr-3router-5runs-*" || exit 1
run_and_commit_batch "ucast_fastpr" "4" "run_ucast_fastpr_test.sh" "ucast_fastpr_test_devices_4routers.toml" "ucast_fastpr-4router-5runs-*" || exit 1
run_and_commit_batch "mcast" "2" "run_mcast_test.sh" "mcast_test_devices_2routers.toml" "mcast-2router-5runs-*" || exit 1
run_and_commit_batch "mcast" "3" "run_mcast_test.sh" "mcast_test_devices_3routers.toml" "mcast-3router-5runs-*" || exit 1
run_and_commit_batch "mcast" "4" "run_mcast_test.sh" "mcast_test_devices_4routers.toml" "mcast-4router-5runs-*" || exit 1
log "All requested directed 5-run batches completed."
