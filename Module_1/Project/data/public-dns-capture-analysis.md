# Public Wireshark DNS Sample — Reproducible Analysis

## Purpose and boundary

This is a separate **offline learning exercise**, not evidence about `NETSEC-LAB-01`. The source is Wireshark’s public `dns.cap` sample listed on its Sample Captures page. The raw file is deliberately not committed: even public captures can contain identifiers that are unnecessary for the course submission.

| Field | Value |
|---|---|
| Source | `https://wiki.wireshark.org/uploads/__moin_import__/attachments/SampleCaptures/dns.cap` |
| Source catalogue | [Wireshark Sample Captures](https://wiki.wireshark.org/SampleCaptures) |
| Retrieved | 2026-10-27 |
| File format | libpcap, Ethernet link type, microsecond timestamps |
| SHA-256 of reviewed source | `041eeb6f98bb398f1ee8b09651b5b5a84f6a62639f95bf226f9e7b77355d9f28` |
| Privacy treatment | No raw packet file, endpoint addresses, internal-style names, or query strings retained here. |

## Reproducible commands

Use only a copy obtained directly from the source and stored in an approved local training location.

```bash
tshark -r dns.cap -q -z io,phs
tshark -r dns.cap -Y dns -T fields \
  -e frame.number -e dns.flags.response -e dns.count.queries -e dns.count.answers
```

## Observed protocol summary

| Measure | Result |
|---|---:|
| Total frames | 38 |
| Ethernet frames | 38 |
| IPv4 frames | 38 |
| UDP frames | 38 |
| DNS frames | 38 |
| DNS queries | 19 |
| DNS responses | 19 |

The capture contains matched DNS request/response traffic over UDP. This supports practice identifying DNS protocol fields and response flags. It does **not** establish that a resolver is securely configured, that its answers are trusted, or that the capture represents normal traffic for another network.

## Suggested Wireshark exercises

1. Apply `dns`; compare query packets with response packets using `dns.flags.response`.
2. Add columns for transaction ID, query name, response code, and answer count **only in a local viewer**; do not export sensitive values.
3. Use **Statistics → Conversations** and **Statistics → Endpoints** to understand the flow, then discard any identifiers from notes.
4. Record facts (“19 responses observed”) separately from assumptions (“the resolver is healthy”).
