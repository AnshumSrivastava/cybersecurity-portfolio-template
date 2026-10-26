# Synthetic authentication event data dictionary

All events are fictional. Source IPs use documentation-only address ranges. Usernames and hosts are aliases.

| Field | Meaning |
|---|---|
| `timestamp` | Event time in UTC (ISO 8601) |
| `ingest_time` | Time the sample pipeline received the event |
| `host` | Fictional authentication host alias |
| `user` | Synthetic account alias |
| `source_ip` | Documentation-range test address |
| `outcome` | `success` or `failure` |
| `event_type` | Event category |
| `mfa` | Synthetic MFA outcome/context |
| `scenario` | Label for instructor evaluation; do not use this as the detection condition |

Expected synthetic pattern: `learner_01` has five failures followed by a success from one source within a short window; `learner_03` has only two failures before success and is a near-miss. `learner_04` illustrates late ingestion. These fixtures test rule behavior; they do not represent realistic population rates.
