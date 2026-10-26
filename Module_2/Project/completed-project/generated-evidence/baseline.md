# Linux baseline review

Generated: 2026-10-26 21:21 UTC
Assessed root: `/mnt/projects/myAnatomy/Module_2/Project/data/lab-root`

> Read-only educational subset; validate against your OS/version and approved CIS profile.

| ID | Check | Status | Evidence | Remediation |
|---|---|---|---|---|
| FS-01 | /etc/passwd permissions | **PASS** | /etc/passwd mode is 0644; expected no more permissive than 0644. | Set ownership and permissions for /etc/passwd according to the approved OS baseline. |
| FS-02 | /etc/shadow permissions | **PASS** | /etc/shadow mode is 0640; expected no more permissive than 0640. | Set ownership and permissions for /etc/shadow according to the approved OS baseline. |
| SSH-01 | PermitRootLogin | **PASS** | Configured value: no; expected no. | Disable direct SSH root login. |
| SSH-02 | PasswordAuthentication | **PASS** | Configured value: no; expected no. | Use managed key-based authentication where compatible. |
| HOST-01 | Live service checks | **NOT ASSESSED** | Skipped for staged root. | Run on the authorized live host for service state checks. |
| AUTH-01 | Password aging policy | **REVIEW** | PASS_MAX_DAYS   90 | Confirm password-aging policy and approved account exceptions. |

## Review notes
`FAIL` indicates a direct mismatch in this small check. `REVIEW` needs context; `NOT ASSESSED` is not a pass. Record approved exceptions and retest after any change.
