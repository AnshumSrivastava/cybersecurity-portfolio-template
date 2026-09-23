# 04 — Network Reconnaissance With Nmap

## Objective

Move from basic network configuration to systematic network reconnaissance:

> *"I can systematically discover hosts, ports, and services."*

---

## What Problem Were We Solving?
Gaining full visibility into live devices and exposed attack surfaces on an authorized target subnet using Nmap.

## The Reconnaissance Methodology

```text
Stage 1: Host Discovery   (Determine which machines are active)
           ↓
Stage 2: Port Scanning    (Determine which ports accept connections)
           ↓
Stage 3: Service Detection (Identify specific software and versions)
           ↓
Stage 4: Interpretation   (Evaluate potential vulnerabilities and risks)
```

---

## Directory Contents

* [`scans/`](./scans/)
  * `host-discovery.txt` — Ping sweep output identifying online systems.
  * `port-scan.txt` — SYN/TCP port scan output.
  * `service-scan.txt` — Version detection (`-sV`) output.
* [`findings.md`](./findings.md) — Technical analysis answering: What hosts exist? What ports are open? What services are running? What does that tell us?
* `evidence/` — Raw terminal scan outputs and execution logs.
