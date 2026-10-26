# Linux Baseline & Hardening Report

**System:** HARDENING-LAB-01 (training fixture) · **Assessment:** 2026-10-20 · **Method:** read-only subset checker v1.0

## Executive summary

The training baseline review found that the sample SSH policy requires owner review before it can be considered aligned with the approved standard, and that some checks could not be assessed in a staged fixture. The authentication-log review also identified five failed logins from one documentation-range source. This is a triage signal, not evidence of compromise. No system changes were made.

## Results

| Control | Result | Evidence | Disposition |
|---|---|---|---|
| FS-01/FS-02 | NOT ASSESSED | Fixture intentionally omits password files. | Inspect with authorized read access on the live lab VM. |
| SSH-01 | PASS | `PermitRootLogin no` in staged SSH configuration. | Preserve through configuration management; verify effective runtime setting. |
| SSH-02 | PASS | `PasswordAuthentication no` in staged SSH configuration. | Confirm break-glass access before enforcing on a live host. |
| HOST-01 | NOT ASSESSED | Staged-root mode deliberately skips service checks. | Confirm audit logging service state on the authorized live host. |
| AUTH-01 | NOT ASSESSED | Fixture has no `login.defs`. | Review password-aging policy and documented service accounts. |

## Remediation plan

| Priority | Action | Owner | Change safeguards | Retest |
|---:|---|---|---|---|
| 1 | Verify effective SSH settings with the owner; retain root-login restriction and confirm key-only access fits recovery procedures. | Linux owner | Approved maintenance window and console recovery path. | Re-run checker and capture approved `sshd -T` evidence. |
| 2 | Confirm audit service and log retention meet the selected OS baseline. | Platform owner | Do not enable/restart services without a change ticket. | Approved service-state and log-write validation. |
| 3 | Review password-aging policy and documented non-human account exceptions. | Identity owner | Validate impact on service accounts before change. | Policy evidence plus sample account review. |

## Limitations

The supplied checker is a transparent educational subset, not a CIS benchmark scanner. `PASS` applies only to the exact check, `REVIEW` needs context, and `NOT ASSESSED` cannot be treated as a pass. All data in this report is synthetic.
