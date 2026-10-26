# Detection hypotheses and Splunk SPL examples

Choose the correct index and sourcetype for your own training instance. These examples assume the fields in `data-dictionary.md` have been extracted. Use the synthetic sample only.

## Rule A · Repeated failures by user and source

Hypothesis: five or more failures for one user/source in a five-minute window warrant review.

```spl
index=lab_auth event_type=authentication outcome=failure
| bin _time span=5m
| stats count as failures values(host) as hosts by _time user source_ip
| where failures >= 5
```

## Rule B · Failure followed by success

This is a candidate signal, not proof of account compromise. Inspect underlying events, MFA context, and baseline.

```spl
index=lab_auth event_type=authentication
| stats count(eval(outcome="failure")) as failures
        count(eval(outcome="success")) as successes
        earliest(_time) as first_seen latest(_time) as last_seen
        values(mfa) as mfa_results values(host) as hosts
        by user source_ip
| where failures >= 3 AND successes >= 1
```

For a production-ready sequence rule, implement ordering and a bounded time window explicitly in the selected SIEM’s supported query/rule language. The simple aggregation above does not itself prove the success followed the failures.

## Rule C · Telemetry freshness

Create a panel that displays latest event time and ingestion delay. Alert on missing/stale data using an owner-approved threshold. An empty event search alone is not proof of normal activity.

## Tuning questions
- Do NAT/shared egress addresses combine unrelated users?
- Are service accounts or scheduled tests creating expected failures?
- Are timestamps normalized and ingestion delay visible?
- Is the alert threshold tested against both `repeated_failure_then_success` and `benign_near_miss` scenarios?
- Does the analyst see event IDs and enough context to make a decision?
