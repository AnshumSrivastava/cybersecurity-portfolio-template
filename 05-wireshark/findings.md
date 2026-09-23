# Wireshark Network Investigation Findings

A thorough packet analysis report applying evidence-based inspection methodologies to network traffic traces.

---

## 1. Investigation Overview

* **Capture File:** `captures/investigation.pcapng`
* **Analysis Scope:** Traffic generated between test workstation (`192.168.1.105`), internal lab server (`192.168.1.50`), and default gateway/DNS resolver (`192.168.1.1`).
* **Objective:** Detect cleartext credential exposure, investigate TCP handshake dynamics, analyze DNS queries, and detect reconnaissance activity in the packet stream.

---

## 2. Investigation Case Studies

### Case Study 1: DNS Reconnaissance & Resolution
* **Observation:** Outbound UDP queries generated to resolve internal domain names.
* **Evidence:** Packet #14 — Source `192.168.1.105:51423` sent standard query `0x0a12` for `internal-portal.lab`. Destination: `192.168.1.1:53`. Response packet #15 confirmed A record `192.168.1.50`.
* **Filter Used:**
  ```text
  dns && ip.addr == 192.168.1.105
  ```
* **Protocol Breakdown:**
  * Transport: UDP (low latency, connectionless)
  * Transaction ID: `0x0a12`
  * Flags: Standard query (`0x0100`), Recursion Desired
* **Security Meaning:** Unencrypted DNS exposes browsing habits and internal host naming conventions to local network observers. DNS query logging is critical for identifying Command and Control (C2) beaconing and Domain Generation Algorithms (DGA).

---

### Case Study 2: TCP Three-Way Handshake & Window Sizing
* **Observation:** Full TCP connection establishment verified prior to application payload transfer.
* **Evidence:**
  * **Packet #21:** `192.168.1.105` → `192.168.1.50:80` `[SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1`
  * **Packet #22:** `192.168.1.50` → `192.168.1.105` `[SYN, ACK] Seq=0 Ack=1 Win=65160 Len=0 MSS=1460`
  * **Packet #23:** `192.168.1.105` → `192.168.1.50:80` `[ACK] Seq=1 Ack=1 Win=64240 Len=0`
* **Filter Used:**
  ```text
  tcp.flags.syn == 1 && tcp.port == 80
  ```
* **Security Meaning:** Normal connection negotiation establishes sequence and acknowledgment numbers. Tracking handshake patterns distinguishes legitimate client connections from half-open SYN flood denial-of-service attacks.

---

### Case Study 3: Cleartext Credential Exfiltration over HTTP POST
* **Observation:** Unencrypted user credentials and session identifiers transmitted over cleartext port 80.
* **Evidence:** Packet #48 — `POST /login.php HTTP/1.1` from `192.168.1.105` containing form URL-encoded body:
  ```http
  POST /login.php HTTP/1.1
  Host: internal-portal.lab
  User-Agent: Mozilla/5.0 (X11; Linux x86_64)
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 38

  username=admin&password=Password123!
  ```
* **Filter Used:**
  ```text
  http.request.method == "POST"
  ```
* **Stream Reconstruction:** Right-click packet → `Follow` → `TCP Stream`.
* **Security Meaning:** In cleartext protocols, any entity on the same broadcast domain or inline transit path can extract usernames, passwords, cookies, and tokens without needing cryptographic keys.

---

### Case Study 4: Port Scan Signature & TCP RST Anomalies
* **Observation:** Repeated inbound TCP SYN packets to closed ports followed by immediate TCP RST (Reset) packets.
* **Evidence:** Packets #112–118 — Consecutive SYN requests from `192.168.1.105` targeting ports 21, 23, 25, 110, 139, 445 on `192.168.1.50`. Target host returned `[RST, ACK]` within 0.1ms for each request.
* **Filter Used:**
  ```text
  tcp.flags.reset == 1 && ip.src == 192.168.1.50
  ```
* **Security Meaning:** High frequencies of RST packets originating from a single target to one source within a narrow time window are signatures of automated port scanning (e.g. Nmap or masscan).

---

## 3. Wireshark Filter Cheat Sheet for Security Analysts

| Analysis Goal | Wireshark Display Filter |
| :--- | :--- |
| **Cleartext HTTP Credentials** | `http.request.method == "POST"` |
| **All DNS Queries & Responses** | `dns` |
| **Failed DNS Lookups (NXDOMAIN)** | `dns.flags.rcode == 3` |
| **TCP SYN Packets (Connection Initiation)** | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| **Connection Rejections (Port Scan Indicators)** | `tcp.flags.reset == 1` |
| **Isolate Specific IP Conversations** | `ip.addr == 192.168.1.50 && ip.addr == 192.168.1.105` |
| **Filter by Application Port** | `tcp.port in {80, 443, 22, 3306}` |
| **Detect Suspicious HTTP User-Agents** | `http.user_agent matches "(?i)(nmap|sqlmap|nikto|curl)"` |
