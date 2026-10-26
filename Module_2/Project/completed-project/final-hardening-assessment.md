# Linux Hardening & Authentication Monitoring Assessment

| Document control | Value |
|---|---|
| Assessment ID | HARDENING-LAB-01 / baseline-2026-10-20 |
| Environment | Local staged Linux fixture and synthetic authentication log |
| Assessment type | Read-only CIS-style configuration baseline and log triage |
| Authorization | `LAB-AUTH-2026-10-20` training exercise |
| Scope | Defined in [scope.md](scope.md) |
| Tooling | `../tools/cis_audit.py`, `../tools/log_monitor.py`, `../tools/run_audit.sh` |

## Executive summary

The completed training assessment used a staged Linux filesystem and a six-line synthetic authentication log. File-permission and explicit SSH policy checks passed in the fixture. Password-aging policy requires an owner decision, while live audit/firewall service state was intentionally not assessed because the fixture is not a running operating system. The log-monitoring rule identified five failed logins for one user/source pair. That is a review signal, not evidence of compromise.

No configuration, package, service, account, or network changes were made. The priority is to carry the same evidence-aware process to an owner-authorized host: confirm effective SSH policy, audit/logging service, host firewall/equivalent control, account exceptions, and the context behind authentication alerts.

## Scope and method

Only the fixture in `../data/lab-root/` and `../data/auth.log` were used. The assessment did not inspect a live host. The combined launcher was run with:

```bash
tools/run_audit.sh --root data/lab-root --log data/auth.log \
  --output-dir completed-project/generated-evidence
```

The launcher writes a baseline report, optional authentication triage, and a manifest. It only reads the supplied root/log and writes the requested output folder. Control logic, interpretation rules, and known limitations are documented in [../instructions/controls.md](../instructions/controls.md).

## Baseline results

| Control | Status | Direct fixture evidence | Meaning | Required follow-up |
|---|---|---|---|---|
| FS-01 | PASS | `/etc/passwd` mode is 0644 | Narrow permission threshold met. | Review ownership/ACLs on any real host. |
| FS-02 | PASS | `/etc/shadow` mode is 0640 | Narrow permission threshold met. | Review group membership/ACLs on any real host. |
| SSH-01 | PASS | `PermitRootLogin no` | Explicit root-login policy is restrictive in the fixture. | Validate effective runtime configuration and console recovery path. |
| SSH-02 | PASS | `PasswordAuthentication no` | Explicit key-only policy in the fixture. | Confirm managed-key and break-glass workflows before a real change. |
| HOST-01 | NOT ASSESSED | Staged-root operation skips live service checks. | No statement about audit-service state is possible. | Review approved live-host service evidence. |
| HOST-02 | NOT ASSESSED | Staged-root operation skips live service checks. | No statement about firewall/equivalent state is possible. | Review approved live-host rule/service evidence. |
| AUTH-01 | REVIEW | `PASS_MAX_DAYS 90` in fixture. | Policy value exists but needs account/service context. | Confirm policy and approved exceptions with identity owner. |

## Authentication-log results

| Signal | Observed value | Assessment |
|---|---|---|
| Input volume | 6 log lines | Sufficient only for fixture demonstration. |
| Repeated failure rule | `learner` from `192.0.2.44` had 5 failures | Meets the configured review threshold. |
| Success after same-pair failures | None | No same-user/source successful login appears in this file. |
| Other success | `admin_demo` key-based success from `198.51.100.10` | Separate event; no adverse conclusion from this data alone. |

The triage workflow is documented in [../instructions/log-triage-runbook.md](../instructions/log-triage-runbook.md). Before action on a live alert, corroborate approved identity, VPN/MFA, endpoint, and firewall records within a narrow time window.

## Risk and remediation register

| ID | Condition | Rating | Action | Owner | Validation |
|---|---|---|---|---|---|
| H-01 | Live audit and firewall state are not assessed by the fixture. | Medium | Collect approved service/rule evidence on the authorized host. | Platform + Network owner | Re-run after evidence collection; `NOT ASSESSED` must be replaced by evidence, not assumption. |
| H-02 | Password aging has an observed setting but no account-exception context. | Medium | Classify human, service, and break-glass accounts; document approved exceptions. | Identity owner | Policy/exception review and safe test account validation. |
| H-03 | Repeated authentication failures hit the review threshold. | Medium | Validate source/account context; follow incident process if unexpected. | System/identity owner | Case record shows corroboration and decision. |
| H-04 | SSH key-only/root restrictions may affect recovery if changed without planning. | Medium | Confirm console access, key management, and rollback before enforcement. | Linux owner | Approved non-root key login and recovery test. |

## Change and retest requirements

Use [../instructions/hardening-runbook.md](../instructions/hardening-runbook.md) and [../instructions/remediation-template.md](../instructions/remediation-template.md). Each change needs an owner, maintenance window, documented rollback, validated dependency list, and objective retest. Never treat a `PASS` in this subset as CIS certification.

## Limitations

The audit checks a small, transparent control subset. It does not assess kernel parameters, package signatures, all filesystem permissions, PAM, sudo, remote logging, audit rules, firewall rule quality, cloud controls, containers, EDR, vulnerabilities, or application security. The staged root intentionally cannot demonstrate running service state. All labels, accounts, addresses, and data in this submission are synthetic.
