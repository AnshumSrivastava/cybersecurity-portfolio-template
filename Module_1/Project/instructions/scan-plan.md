# Approved Scan Plan and Execution Record

## Pre-flight checklist

- [x] Written lab authorization and target list recorded in `../completed-project/scope.md`.
- [x] Target is the synthetic `LAB-WEB-01` label only; no address range/discovery scan.
- [x] Source workstation and 09:00–11:00 UTC window are approved.
- [x] Owner notified; stop contact and exclusions are known.
- [x] No credential checks, UDP scanning, scripts, brute force, or exploitation are authorized.

## Command record

```text
nmap -sT -sV --version-light --reason -Pn -p 22,80,443 LAB-WEB-01
```

| Field | Recorded value |
|---|---|
| Tool/version | Nmap 7.95 (training record) |
| Start | 2026-10-20 09:32 UTC |
| Target | LAB-WEB-01 / sanitized `192.0.2.25` |
| Scope | TCP ports 22, 80, 443 only |
| Output | `../data/lab-web-01-nmap.xml` and sanitized text excerpt |
| Result | 22 closed; 80 and 443 open |

## Interpretation safeguards

A port result means that a TCP connection state was observed at one time from one location. It does not verify software patching, account policy, web application security, firewall rules on another path, or the absence of other services.
