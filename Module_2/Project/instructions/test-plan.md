# Toolkit test plan

| ID | Test | Command | Expected result | Actual result |
|---|---|---|---|---|
| T01 | Unit tests | `python3 -m unittest discover -s tools/tests -v` | All fixture tests pass | |
| T02 | Auth threshold | `python3 tools/log_monitor.py --log data/auth.log` | One review alert for `192.0.2.44` | |
| T03 | Structured output | `python3 tools/log_monitor.py --log data/auth.log --format json` | Valid JSON with counts and alerts | |
| T04 | Staged-root audit | `python3 tools/cis_audit.py --root data/lab-root` | No live services touched; unavailable checks marked `NOT ASSESSED` | |
| T05 | Report output | `tools/run_audit.sh --root data/lab-root --log data/auth.log --output-dir completed-project/generated-evidence` | Baseline, log triage, and manifest created | |

Record tool version, platform, and sanitized output. Do not treat a successful run as proof that every operating-system control was assessed.
