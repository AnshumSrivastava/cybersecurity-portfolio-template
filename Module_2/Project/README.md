# Module 2 · Automated Log-Monitoring & Hardening Toolkit

This is a complete, read-only Linux hardening and log-triage project. The structure separates the finished submission, safe synthetic data, operating instructions, and executable tools.

## Folder map

| Folder | Contents | Use it when… |
|---|---|---|
| [completed-project/](completed-project/) | Completed baseline and log-triage reports, scope, verification results, and generated evidence. | Reviewing the submission or handing it to an owner. |
| [data/](data/) | Synthetic authentication log and staged Linux root fixture. | Reproducing the complete project safely. |
| [instructions/](instructions/) | Control catalogue, remediation/rollback runbook, alert-triage runbook, remediation register, and test plan. | Understanding how to interpret and operate the toolkit. |
| [tools/](tools/) | Audit/log scripts and fixture-driven tests. | Generating reports in an authorized lab. |

## Reproduce the included project safely

```bash
cd Module_2/Project
tools/run_audit.sh --root data/lab-root --log data/auth.log \
  --output-dir completed-project/generated-evidence
python3 -m unittest discover -s tools/tests -v
```

This uses only local fixtures. The baseline tool performs no configuration changes, package installation, account modification, service restart, or network transmission.

## Safe operating boundary

Run against a real Linux host only if you own it or have written authorization. The tool is a transparent educational subset of CIS-style checks, not a CIS certification tool. Never use `sudo` merely to turn `NOT ASSESSED` into a passing result; obtain approval, document the gap, and use an approved evidence source.

## Deliverables

- Owner-approved scope and target record
- Generated baseline, log-triage, and run-manifest artifacts
- Interpretation of every PASS, FAIL, REVIEW, and NOT ASSESSED result
- Owner-approved remediation / rollback plan and objective retest
- Test results, limitations, and evidence-handling notes
