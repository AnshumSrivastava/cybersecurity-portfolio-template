# Generated Network Baseline Summary

> Built from sanitized local evidence only; this tool performs no network activity.

## Service observation — LAB-WEB-01

| TCP port | State | Service |
|---:|---|---|
| 22 | closed | ssh |
| 80 | open | http |
| 443 | open | https |

## Capture observation

| Time (UTC) | Flow | Protocol | Observation |
|---|---|---|---|
| 2026-10-20T10:01:12Z | ANALYST-01 → LAB-DNS | DNS | standard query and response observed |
| 2026-10-20T10:01:15Z | ANALYST-01 → LAB-WEB-01:443 | TCP | SYN SYN-ACK ACK handshake complete |
| 2026-10-20T10:01:15Z | ANALYST-01 → LAB-WEB-01:443 | TLS | ClientHello and ServerHello observed |

## Analyst prompts

- Confirm that the HTTP listener is redirect-only and contains no session-bearing content.
- Confirm the intended exposure and source-zone policy for HTTPS.
- Validate TLS policy and certificate separately; ClientHello/ServerHello alone is insufficient.
