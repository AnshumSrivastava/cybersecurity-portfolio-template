# Networking Commands & Local Investigation

Investigative command reference used to document local network configuration and state.

---

### 1. Host IP Configuration: `ip addr`
* **Command:** `ip -c addr`
* **Purpose:** Displays network interfaces, MAC addresses, IPv4/IPv6 addresses, and interface state (UP/DOWN).
* **Investigation Findings:**
  * Loopback interface `lo`: `127.0.0.1/8`
  * Active ethernet/wireless interface: Identifies assigned internal IP and subnet mask (e.g. `/24`).

---

### 2. Routing Table & Gateway: `ip route`
* **Command:** `ip route`
* **Purpose:** Shows kernel IP routing table.
* **Key Entry:** `default via <gateway_ip> dev <interface>` identifies default router for outbound traffic.

---

### 3. Reachability & Latency: `ping`
* **Command:** `ping -c 4 <target_ip_or_domain>`
* **Purpose:** Tests Layer 3 ICMP echo request/reply reachability and round-trip time.
* **Security Insight:** Some firewalls drop ICMP packets even if TCP ports are active.

---

### 4. ARP / Neighbor Cache: `ip neigh`
* **Command:** `ip neigh`
* **Purpose:** Shows IPv4 ARP table and IPv6 neighbor discovery cache mapping IP addresses to physical MAC addresses on the local link.

---

### 5. Listening Ports & Sockets: `ss -tuln`
* **Command:** `ss -tuln`
* **Flags:**
  * `-t`: TCP sockets
  * `-u`: UDP sockets
  * `-l`: Listening sockets only
  * `-n`: Numeric output (do not resolve port numbers to service names)
* **Purpose:** Discovers exposed network attack surfaces on the local system.

---

### 6. DNS Name Resolution: `nslookup` / `dig`
* **Command:** `nslookup example.com` or `dig example.com`
* **Purpose:** Queries DNS servers to resolve hostnames to IP addresses and verify DNS server responsiveness.
