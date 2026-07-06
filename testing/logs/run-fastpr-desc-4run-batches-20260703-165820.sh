#!/usr/bin/env bash
set -euo pipefail

REPO="/home/ewout/.openclaw/workspace-softwaredeveloper/ESPHome-Thread-ED-Switch-Parent"
TESTING="$REPO/testing"
BRANCH="main"

cd "$TESTING"

echo "Launcher started: $(date -Iseconds)"
echo "Repo: $REPO"

test -x ./run_ucast_fastpr_test.sh
test -f scripts/analyze_test_logs.py

mapfile -t FASTPR_CONFIGS < <(ls -1 ucast_fastpr_test_devices_*routers.toml 2>/dev/null | sort -Vr)

if ((${#FASTPR_CONFIGS[@]} == 0)); then
  echo "Systemic failure: no supported fastpr configs found"
  exit 1
fi

commit_batch() {
  local batch_rel="$1"
  local variant="$2"
  local routers="$3"
  local msg="Add ${variant} ${routers}router 4-run batch"
  local push_log
  push_log="$(mktemp)"

  git -C "$REPO" status --short -- "$batch_rel"
  git -C "$REPO" add "$batch_rel"
  git -C "$REPO" commit -m "$msg"

  if git -C "$REPO" push origin "$BRANCH" >"$push_log" 2>&1; then
    cat "$push_log"
    rm -f "$push_log"
    return 0
  fi

  cat "$push_log"
  if grep -Eq "GH001|file size limit|exceeds GitHub's file size limit" "$push_log"; then
    echo "Push failed due to large file; retrying without pcapng"
    git -C "$REPO" reset --soft HEAD~1
    mapfile -t PCAPS < <(find "$batch_rel" -type f -name '*.pcapng' | sort)
    local note="$batch_rel/EXCLUDED_LARGE_FILES.md"
    {
      echo "# Excluded large files"
      echo
      echo "These files were left local because Git push rejected them as too large:"
      echo
      for file in "${PCAPS[@]}"; do
        echo "- $file"
      done
    } > "$note"
    if ((${#PCAPS[@]} > 0)); then
      git -C "$REPO" restore --staged -- "${PCAPS[@]}" || true
    fi
    git -C "$REPO" add "$batch_rel"
    git -C "$REPO" commit -m "$msg"
    git -C "$REPO" push origin "$BRANCH"
    rm -f "$push_log"
    return 0
  fi

  rm -f "$push_log"
  return 1
}

run_batch() {
  local variant="$1"
  local wrapper="$2"
  local config="$3"
  local routers="$4"
  local batch_rc=0
  local new_dir=""
  local pattern="${variant}-${routers}router-4runs-*"

  mapfile -t BEFORE_DIRS < <(find logs -maxdepth 1 -mindepth 1 -type d -name "$pattern" -printf '%f\n' | sort)

  echo "Starting batch: variant=$variant routers=$routers config=$config"
  echo "Command: ./$wrapper --config $config --runs 4 --clean-before-compile"
  if ! "./$wrapper" --config "$config" --runs 4 --clean-before-compile; then
    batch_rc=$?
    echo "Batch command failed: variant=$variant config=$config rc=$batch_rc"
  fi

  mapfile -t AFTER_DIRS < <(find logs -maxdepth 1 -mindepth 1 -type d -name "$pattern" -printf '%f\n' | sort)
  new_dir="$(comm -13 <(printf '%s\n' "${BEFORE_DIRS[@]}") <(printf '%s\n' "${AFTER_DIRS[@]}") | tail -n 1 || true)"
  if [[ -z "$new_dir" ]]; then
    echo "Systemic failure: no batch directory detected for variant=$variant config=$config pattern=$pattern"
    return 1
  fi

  local batch_rel="testing/logs/$new_dir"
  echo "Batch directory: $batch_rel"

  if ! python3 scripts/analyze_test_logs.py --logs-dir "logs/$new_dir" --write-markdown; then
    echo "Analyzer failed for $batch_rel"
    if [[ $batch_rc -eq 0 ]]; then
      return 1
    fi
  fi

  if ! commit_batch "$batch_rel" "$variant" "$routers"; then
    echo "Systemic failure: commit/push failed for $batch_rel"
    return 1
  fi

  if [[ $batch_rc -ne 0 ]]; then
    echo "Continuing after failed batch with preserved artifacts: $batch_rel"
  else
    echo "Completed batch: $batch_rel"
  fi
  return 0
}

for config in "${FASTPR_CONFIGS[@]}"; do
  [[ "$config" =~ _([0-9]+)routers\.toml$ ]] || { echo "Systemic failure: bad config name $config"; exit 1; }
  run_batch "ucast_fastpr" "run_ucast_fastpr_test.sh" "$config" "${BASH_REMATCH[1]}"
done

echo "Launcher finished: $(date -Iseconds)"
