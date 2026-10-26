# Control Catalogue and Interpretation Rules

| ID | Check | Why it matters | PASS means | Common limitation / false-positive risk |
|---|---|---|---|---|
| FS-01 | `/etc/passwd` mode ≤ 0644 | Prevents unauthorized modification while preserving normal account lookup. | File mode met the small checker threshold. | Ownership, ACLs, immutable flags, and OS-specific layout are not checked. |
| FS-02 | `/etc/shadow` mode ≤ 0640 | Reduces access to password hashes. | Mode met threshold. | Group membership and ACLs may still expose data. |
| SSH-01 | `PermitRootLogin no` | Limits direct remote root authentication. | Explicit setting is `no`. | Include files/effective configuration and approved break-glass design need separate review. |
| SSH-02 | `PasswordAuthentication no` | Reduces password-spraying exposure when key auth is managed safely. | Explicit setting is `no`. | Not universally appropriate; validate service access and recovery before change. |
| HOST-01 | Audit service active | Supports accountable, reviewable event collection. | Local `auditd` service reports active. | Other distributions use other audit/log services; active does not prove useful rules or retention. |
| HOST-02 | Firewall service active | Supports host-level traffic control. | Local UFW service reports active. | An equivalent firewall may be used; active does not prove a secure rule set. |
| AUTH-01 | `PASS_MAX_DAYS` review | Supports password policy review where passwords are used. | Never automatically passes; needs policy context. | Modern SSO/service accounts may make local password aging inapplicable. |

## Status vocabulary

- **PASS:** this narrow implementation check matched its expected value.
- **FAIL:** the direct observed value mismatched the expected value.
- **REVIEW:** a policy decision or a platform-specific check is required.
- **NOT ASSESSED:** the file/service was unavailable or permission was intentionally insufficient. It is never equivalent to PASS.

This catalogue maps concepts commonly found in CIS Benchmarks, but does not substitute for the version-specific CIS Benchmark, organization policy, or a formal compliance assessment.
