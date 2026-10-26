# Completed Wireshark observation record — synthetic lab exercise

Source: instructor-provided, sanitized PCAP (`LAB-PCAP-01`)  
Analysis time: 2026-10-20 10:05 UTC  
Capture scope: traffic generated between `ANALYST-01`, `LAB-WEB-01`, and the configured lab resolver. No payloads retained.

| Question | Display filter | Direct observation | Interpretation | Limitation |
|---|---|---|---|---|
| Was name resolution present? | `dns` | `ANALYST-01` made 4 standard DNS queries to `LAB-DNS`; each received one response. | DNS was observable for this short window. | Does not prove all application traffic used DNS or that resolver policy is secure. |
| Was a web connection established? | `tcp.flags.syn == 1 && tcp.flags.ack == 0` | One SYN from `ANALYST-01` to `LAB-WEB-01:443` was followed by SYN/ACK and ACK. | TCP setup succeeded during capture. | A successful handshake does not establish application authorization or content safety. |
| Was encryption negotiated? | `tls.handshake.type == 1 or tls.handshake.type == 2` | ClientHello and ServerHello frames were present for the port-443 session. | TLS negotiation was observed. | This worksheet did not validate certificate trust, protocol version, cipher policy, or payload security. |

Privacy note: packet contents, MAC addresses, timestamps below minute granularity, and raw capture were intentionally excluded.
