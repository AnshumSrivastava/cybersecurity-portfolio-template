# Data and Fixtures

All content in this folder is synthetic and safe for offline testing. It must not be treated as evidence about a real Linux host.

| Item | Purpose |
|---|---|
| `auth.log` | Auth-log fixture: five failed attempts from one source, plus an unrelated key-based success. |
| `lab-root/` | Minimal staged filesystem for a read-only baseline-check demonstration. |

Run the complete fixture workflow from the project root (not from `data/`):

```bash
tools/run_audit.sh --root data/lab-root --log data/auth.log --output-dir completed-project/generated-evidence
```

The command writes reports under `completed-project/generated-evidence/`; it does not access a real host or modify the fixture.
