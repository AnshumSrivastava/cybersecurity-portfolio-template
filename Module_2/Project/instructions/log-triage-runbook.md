# Authentication Alert Triage Runbook

## Trigger

`log_monitor.py` creates a review alert when one user/source pair reaches the configured failed-login threshold or when a successful login follows failures from the same pair.

## Triage steps

1. Preserve the input file's source, collection time, and hash in the protected case system; do not alter it.
2. Identify the account class (person, service, break-glass) and whether the source is an approved network or exercise system.
3. Check authorized identity, VPN, MFA, EDR, and firewall records for the same narrow time window.
4. Record facts separately from hypotheses. The script's alert is a prioritization signal, not attribution or compromise proof.
5. Escalate unexpected success-after-failure events to the system/identity owner. Containment changes require the incident or change process.

## Case record fields

| Field | Record |
|---|---|
| Alert ID / time | |
| Account / source label | |
| Evidence file and integrity reference | |
| Corroborating sources checked | |
| Facts | |
| Hypotheses / confidence | |
| Owner, decision, next review time | |
