# Project 5 · SOC Monitoring and Detection Dashboard

## Scenario and goal
Build a defensive monitoring workflow from synthetic authentication events. Show that events ingest correctly, detections match defined scenarios, analysts can inspect context, and a case can be triaged and handed off. Use Splunk, Elastic, or an equivalent documented platform.

## Synthetic data
`sample-data/auth_events.jsonl` contains fictional accounts, hosts, timestamps, and documentation-range IPs. It includes a normal baseline, repeated failures followed by success, a benign near-miss, and delayed ingestion. See `data-dictionary.md`. The `scenario` field is an instructor label; do not use it as the detection condition.

## Workflow
1. Ingest the JSONL file and verify timestamps, time zone, field extraction, duplicates, and event freshness.
2. Create three detections: repeated failures, failure-followed-by-success, and unusual source context. `detections.md` includes SPL examples and limitations.
3. Build a dashboard showing outcomes over time, top user/source combinations, alert queue, and latest-event freshness.
4. Test positive, benign, and missing-telemetry cases from `test-results.csv`. Record expected and observed results.
5. Triage one synthetic alert using `triage-template.md`. Separate facts from hypothesis and state confidence.
6. Present an alert-to-escalation handoff with evidence IDs, next owner, action, and follow-up time.

## Privacy and safety
Use only the included synthetic files or instructor-provided logs. Never ingest production logs, real identifiers, passwords, tokens, or personal data. Do not generate actual login attempts or password guesses; the behavior is already represented in the sample events.

## Deliverables
- Data dictionary and ingestion notes
- Three detection rules with test evidence and tuning notes
- Dashboard export/screenshots and reproducible queries
- Completed triage record and handoff
- Positive/negative test matrix and known limitations

## Assessment · 100 points
Data quality/privacy 15 · detection logic 25 · dashboard usefulness 20 · triage/escalation 20 · testing/false positives 15 · handoff clarity 5.

## References
[NIST log-management project](https://csrc.nist.gov/Projects/log-management) · [Splunk SPL tutorial](https://docs.splunk.com/Documentation/Splunk/latest/SearchTutorial/Usethesearchlanguage) · [Elastic security documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-getting-started.html).
