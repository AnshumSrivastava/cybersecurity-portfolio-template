# Retest Plan

## Preconditions

- The owner approved the exact target, source, window, and test actions in writing.
- The relevant configuration change is deployed and a rollback route exists.
- A pre-change and post-change service matrix is available.
- Test accounts/data contain no personal information.

## Retest matrix

| Retest ID | Related action | Safe verification | Pass condition | Evidence to retain |
|---|---|---|---|---|
| RT-01 | HTTPS-only behavior | One approved HTTP request to `LAB-WEB-01:80` from `ANALYST-01` | Redirects to HTTPS without a sensitive response body or session artifact | Sanitized status/Location header only |
| RT-02 | Firewall matrix | Re-run only the original approved three-port TCP observation | Results match approved service matrix; unexpected port state is investigated | Command, version, timestamp, sanitized XML/text |
| RT-03 | TLS lifecycle | Owner validates certificate name, validity window, and approved protocol policy | Certificate/process meets owner policy | Approved certificate review record; no private key |
| RT-04 | Documentation governance | Compare inventory/matrix with approved router/web change records | Owners, rules, and review dates are current | Signed review record |

## Retest result record

| Retest ID | Date/window | Assessor | Result | Exception / limitation | Owner sign-off |
|---|---|---|---|---|---|
| RT- | | | Pass / Fail / Not assessed | | |
