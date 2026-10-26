# Wireshark Analysis Guide — Authorized Lab Only

## Capture safety plan

Use an instructor-provided PCAP or traffic you generated between your own lab systems. Set a short capture window and narrow capture filter before collecting. Do not capture shared Wi-Fi, neighbors’ traffic, real credentials, or personal conversations. Prefer an offline sample from the [Wireshark Sample Captures collection](https://wiki.wireshark.org/SampleCaptures) when a live capture is unnecessary.

**Important:** capture filters and display filters are different languages. Use a capture filter to limit collection (for example `host 192.0.2.25 and (port 53 or tcp port 443)`) and a display filter to inspect an already-collected trace (for example `dns` or `tls`). Confirm the filter against the current Wireshark documentation before use.

## Analysis worksheet

| Goal | Display filter | Record as a fact | Do not conclude |
|---|---|---|---|
| Find name resolution | `dns` | Query/response count, labels, response code, endpoint aliases | That DNS is secure or all traffic used DNS |
| Find connection attempts | `tcp.flags.syn == 1 && tcp.flags.ack == 0` | Client/server aliases, destination port, whether a later SYN/ACK appears | That the remote application is healthy or authorized |
| Follow a TCP conversation | `tcp.stream eq N` | Handshake, teardown/reset, retransmission indicators, duration | Why a retransmission occurred without corroboration |
| Identify encrypted sessions | `tls` | Handshake record types, endpoint aliases, port | Certificate validity, cipher strength, payload safety, or user intent |
| Locate unencrypted HTTP in a self-generated lab capture | `http` | Request method/status and safe lab path | That plaintext equals a vulnerability without context |

## Completed exercise data

This project deliberately uses [capture-summary.csv](../data/capture-summary.csv) rather than a raw PCAP. Recreate the completed observation table only from the listed three records; do not invent packet fields that are absent from the source.

## Analyst quality checks

- State whether a filter was a capture filter or display filter.
- Record local time zone and source interface for live data.
- Count packets/flows before sampling individual frames.
- Keep frame numbers and stream identifiers only in protected working notes if they could identify users.
- Write “not assessed” when a fact cannot be established from the capture.
