# Wireshark observation worksheet

Capture source: instructor-provided PCAP / self-generated lab traffic  
Capture time (UTC):  
Sanitization performed:

| Question | Display filter used | Observation (facts only) | Evidence reference | Limitation |
|---|---|---|---|---|
| Which hosts exchanged DNS traffic? | `dns` | | | |
| Which TCP conversations were established? | `tcp.flags.syn == 1 && tcp.flags.ack == 0` | | | |
| Is traffic encrypted in transit? | `tls or quic` | | | |

Do not include raw credential-bearing traffic, real addresses, device names, or unrelated payloads.
