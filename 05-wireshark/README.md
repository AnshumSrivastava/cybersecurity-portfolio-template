# 05 — Wireshark Network Investigation

## Objective

Move beyond command-line abstraction and analyze raw network traffic frames directly:

> *"Ask questions of network evidence."*

---

## What Problem Were We Solving?
Detecting network anomalies, tracking conversations, identifying unencrypted protocols, and uncovering security incidents by inspecting captured packet streams.

## Key Investigation Areas
* Filtering packets with Wireshark display filters (`ip.addr`, `tcp.port`, `dns`, `http`)
* Reconstructing TCP streams (`Follow TCP Stream`)
* Inspecting DNS queries and domain resolution patterns
* Distinguishing cleartext vs encrypted protocols
* Analyzing packet header flags (SYN, ACK, FIN, RST)

---

## Directory Contents

* [`captures/`](./captures/) — Network packet captures (`.pcapng`).
* [`findings.md`](./findings.md) — Investigative report detailing observations, packet filters, evidence, and security meanings.
* `screenshots/` — Visual packet analysis evidence and stream reconstruction screenshots.
