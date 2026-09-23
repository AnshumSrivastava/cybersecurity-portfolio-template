# 09 — Reconnaissance Investigation

## Objective

Develop information gathering as an analytical cybersecurity mindset:

> *"Before attacking or troubleshooting something, first understand what exists."*

---

## What Problem Were We Solving?
Systematically mapping external infrastructure, passive asset discovery, domain footprinting, service enumeration, and identifying attack vectors without running intrusive exploits.

## Information Sources Investigated
* **DNS Records:** A, AAAA, CNAME, MX, TXT, SPF records
* **IP Information & Routing:** Autonomous System Numbers (ASN), CIDR blocks
* **Port & Service Mapping:** Accessible perimeter ports and service daemons
* **HTTP Header Analysis:** Server headers, TLS configurations, security headers (`Strict-Transport-Security`, `Content-Security-Policy`)
* **Open Source Intelligence (OSINT):** Public certificates (Certificate Transparency logs), whois data

---

## Directory Contents

* [`target.md`](./target.md) — Scope definition, target URLs, authorization parameters.
* [`findings.md`](./findings.md) — Structured intelligence report detailing gathered facts and threat vectors.
* `evidence/` — Query logs, DNS traces, and HTTP responses.
