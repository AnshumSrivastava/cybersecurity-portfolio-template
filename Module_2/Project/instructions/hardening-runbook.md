# Approved Hardening Runbook

## Before any change

1. Open a change record with system owner, business owner, maintenance window, rollback owner, and success criteria.
2. Back up only approved configuration files and verify a console/recovery path. Do not place backups containing secrets in the course repository.
3. Identify dependencies: automation accounts, monitoring collectors, configuration management, and application service accounts.
4. Convert every audit observation into a decision: remediate, accept with expiry, or investigate. `NOT ASSESSED` requires evidence—not closure.

## Change sequence

| Order | Change candidate | Pre-check | Rollback | Objective validation |
|---:|---|---|---|---|
| 1 | SSH root/password policy | Confirm managed key access and emergency console access. | Restore approved prior configuration through console. | Authorized non-root key login works; direct root login is rejected. |
| 2 | Audit service/rules | Confirm disk budget and log collection path. | Restore prior rule set; retain evidence. | Service active; a benign approved event appears in the expected protected log. |
| 3 | Host firewall policy | Build allowlist from documented service inventory and management sources. | Console access plus previous approved rule set. | Approved flows work; unapproved test flow is denied in lab. |
| 4 | Password/account policy | Classify human, service, and break-glass accounts. | Restore prior settings under identity-owner approval. | Test account policy behaves as intended; services continue. |

## After change

Re-run the read-only audit, check service health and monitoring, attach approved evidence to the change record, and schedule a review date. A passing script result does not replace operational validation.
