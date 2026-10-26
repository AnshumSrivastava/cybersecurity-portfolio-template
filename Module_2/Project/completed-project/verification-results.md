# Verification Results — completed training run

**Date:** 2026-10-27 · **Environment:** local course workspace / synthetic fixture only

| Test | Command / method | Expected | Observed | Status |
|---|---|---|---|---|
| Shell syntax | `bash -n tools/run_audit.sh` | Valid Bash syntax | No syntax errors | PASS |
| Log unit test | `python3 -m unittest discover -s tools/tests -v` | Repeated-failure signal identified | Fixture test passed | PASS |
| Staged-root unit test | Same test suite | SSH policy rendered without live-service check | Fixture test passed | PASS |
| Network-safe baseline report | `tools/cis_audit.py --root data/lab-root` | Report emitted; staged/missing controls not misreported as pass | Report produced with explicit `NOT ASSESSED` statuses | PASS |
| Combined workflow | `tools/run_audit.sh --root data/lab-root --log data/auth.log --output-dir completed-project/generated-evidence` | Baseline, log triage, and manifest created | All three artifacts produced | PASS |
| Sample auth detection | `tools/log_monitor.py --log data/auth.log` | Five failures for one source flagged | `learner` / `192.0.2.44` flagged for review | PASS |

## Interpretation

These checks verify program behavior against a synthetic fixture. They do not certify a host as compliant, prove a firewall rule set is secure, or establish compromise from a log signal. Production use requires authorization, target-specific change approval, and a review of platform-specific controls.
