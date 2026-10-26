# Tools and Tests

| File | Action |
|---|---|
| `cis_audit.py` | Reads selected configuration and service state; emits Markdown or JSON; makes no changes. |
| `log_monitor.py` | Reads a supplied auth-log-style file and emits review signals; does not tail or alter logs. |
| `run_audit.sh` | Creates baseline, optional auth triage, and run manifest in one output folder. |
| `tests/test_tools.py` | Fixture-driven regression tests; no live-host inspection. |

Run tests from the project root:

```bash
python3 -m unittest discover -s tools/tests -v
```
