#!/usr/bin/env bash
set -euo pipefail
timestamp="$(date -u +%Y%m%dT%H%M%SZ)"
output_dir="reports/$timestamp"
root="/"
log_file=""
while (($#)); do
  case "$1" in
    --output) output_dir=$(dirname "${2:?missing output path}"); explicit_output=$2; shift 2 ;;
    --output-dir) output_dir=${2:?missing output directory}; shift 2 ;;
    --root) root=${2:?missing root path}; shift 2 ;;
    --log) log_file=${2:?missing authentication log path}; shift 2 ;;
    -h|--help) echo "Usage: $0 [--root ROOT] [--log AUTH.LOG] [--output-dir DIRECTORY] [--output REPORT.md]"; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done
mkdir -p "$output_dir"
baseline="${explicit_output:-$output_dir/baseline.md}"
python3 "$(dirname "$0")/cis_audit.py" --root "$root" --output "$baseline"
if [[ -n "$log_file" ]]; then
  python3 "$(dirname "$0")/log_monitor.py" --log "$log_file" > "$output_dir/auth-triage.md"
fi
{
  echo "# Audit Run Manifest"
  echo
  echo "- Generated (UTC): $timestamp"
  echo "- Assessed root: \`$root\`"
  echo "- Baseline report: \`$(basename "$baseline")\`"
  [[ -n "$log_file" ]] && echo "- Authentication triage: \`auth-triage.md\` (input: \`$log_file\`)"
  echo "- Mode: read-only; no configuration, service, package, or account changes were made."
} > "$output_dir/manifest.md"
echo "Wrote audit artifacts to: $output_dir"
