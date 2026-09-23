# Networking Notes & Core Concepts

A structured breakdown of core networking fundamentals for cybersecurity analysis.

---

## 1. Device to Service Model

When an application communicates across a network, traffic flows through a layered model:

```text
Device        (Host / Physical Node)
   ↓
IP Address    (Layer 3 Logical Addressing — e.g. 192.168.1.50)
   ↓
Network       (Subnet & Broadcast Domain — e.g. 192.168.1.0/24)
   ↓
Port          (Layer 4 Endpoint Identifier — e.g. 443)
   ↓
Protocol      (Transport & Application rules — TCP, UDP, TLS, HTTP)
   ↓
Service       (Active process handling the connection — e.g. nginx, sshd)
```

---

## 2. IP Address vs Port

* **IP Address (Layer 3):** Identifies the **host** on a network (like a building's street address).
* **Port (Layer 4):** Identifies the specific **application / process** running on that host (like an apartment number within the building). Ports range from `0` to `65535`:
  * `0 - 1023`: Well-known ports (HTTP 80, HTTPS 443, SSH 22, DNS 53).
  * `1024 - 49151`: Registered ports.
  * `49152 - 65535`: Dynamic / Ephemeral ports used by clients for outbound sessions.

---

## 3. TCP vs UDP

| Feature | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Connection** | Connection-oriented (3-way handshake) | Connectionless |
| **Reliability** | Guarantees delivery (ACKs, retransmissions) | Best effort (no delivery guarantees) |
| **Ordering** | Guarantees sequential order | Packets may arrive out of order |
| **Overhead** | Higher (20-byte header, state tracking) | Lower (8-byte header, minimal latency) |
| **Common Uses**| Web browsing (HTTP/HTTPS), SSH, SFTP, email | DNS queries, video streaming, VoIP, gaming |

### The TCP Three-Way Handshake
1. **SYN**: Client sends Synchronize packet (`SYN=1`, random `Seq=X`).
2. **SYN-ACK**: Server responds with Synchronize + Acknowledge (`SYN=1, ACK=1`, `Seq=Y`, `Ack=X+1`).
3. **ACK**: Client acknowledges (`ACK=1`, `Ack=Y+1`). Connection established.

---

## 4. Default Gateway & Routing

* **Default Gateway:** The router IP that forwards packets destined for outside the local subnet.
* Without a default gateway, a host can only reach devices on its immediate local network broadcast domain.
