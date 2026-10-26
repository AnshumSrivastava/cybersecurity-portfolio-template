# Authentication Log Triage — completed training example

**Input:** `../data/auth.log` · **Threshold:** 5 failures per user/source pair · **Result:** review required

## Facts

| Signal | Value |
|---|---|
| Lines read | 6 |
| Repeated failure alert | `learner` from `192.0.2.44`: 5 failures |
| Successful login after that failure sequence | None observed |
| Other successful login | `admin_demo` from `198.51.100.10` using public key |

## Analyst assessment

The repeated failures meet the configured review threshold. The log does not establish intent, password validity, account compromise, or whether the source is expected. There is no successful login from the alerted source in the supplied file.

## Next actions

1. Ask the lab owner whether `192.0.2.44` and the learner account were part of an authorized exercise.
2. Preserve the minimal sanitized evidence and check correlated authentication/audit events within the approved window.
3. If activity is unexpected, follow the lab incident process; do not block sources or reset accounts based solely on this one file.
