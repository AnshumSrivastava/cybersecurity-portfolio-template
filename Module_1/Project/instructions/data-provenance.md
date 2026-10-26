# Evidence Register and Data Provenance

## Dataset status

This project is a **reproducible training dataset**, not a claim about a live home network. Host names are aliases and IPv4 values come from the RFC 5737 documentation block. The project never performs a network scan unless a learner separately obtains authorization and uses their own approved lab target.

| Evidence ID | File | Origin | Collected / created | Integrity / handling | Permitted use |
|---|---|---|---|---|---|
| INV-01 | `../completed-project/inventory.csv` | Training team asset register | 2026-10-20 | Safe labels only; version-controlled | Topology and ownership baseline |
| NMAP-01–03 | `../data/lab-web-01-nmap.xml` | Synthetic Nmap-format lab output | 2026-10-20 | No real target identifiers or banners | Port/service observation exercise |
| PCAP-01–03 | `../data/capture-summary.csv` | Sanitized derived capture summary | 2026-10-20 | No raw PCAP, payload, MAC, cookie, or private address retained | Wireshark filter/interpretation exercise |
| R-01–04 | `../completed-project/final-report.md` | Analyst assessment based on evidence above | 2026-10-20 | Conclusions preserve limitations | Baseline reporting exercise |

## Collection and sanitization rules for a real authorized lab

1. Keep raw captures and scan outputs in an owner-approved protected location, not in this repository.
2. Record hash, collector, source interface, start/end time, tool version, exact filter/command, and authorization reference.
3. Create a minimal derivative for the report: replace hostnames and addresses with labels; remove payloads, credentials, tokens, cookies, MACs, and unrelated traffic.
4. Preserve the distinction between original evidence, derived evidence, and analyst conclusion.
5. Follow the owner’s retention and destruction schedule.
