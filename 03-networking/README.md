# 03 — Networking Fundamentals

## Objective

Understand what actually happens when computers communicate across local and wide-area networks.

```text
Device
  ↓
IP
  ↓
Network
  ↓
Port
  ↓
Protocol
  ↓
Service
```

---

## What Problem Were We Solving?
Moving from treating network connections as abstract "magic" to systematically diagnosing host interfaces, IP subnets, routing tables, DNS resolution, and active transport-layer sockets.

## Key Areas Investigated
* Local network configuration: IP address assignment, subnets, broadcast domains
* Routing & default gateways: `ip route` and packet transit
* Address Resolution Protocol (ARP): Mapping Layer 3 IP addresses to Layer 2 MAC addresses (`ip neigh`)
* Socket states & listening ports: `ss -tuln`
* Domain Name Resolution (DNS): Hierarchical queries, record types (A, AAAA, MX, NS) via `nslookup` / `dig`
* Layer 4 Transport Protocols: TCP 3-way handshake, statefulness, reliability vs UDP connectionless datagrams

---

## Directory Contents

* [`networking-notes.md`](./networking-notes.md) — Core conceptual notes covering IP addressing, ports, protocols, TCP vs UDP.
* [`commands.md`](./commands.md) — Command reference and investigative queries executed on the local environment.
* `evidence/` — Command execution outputs, routing tables, and interface dumps.
