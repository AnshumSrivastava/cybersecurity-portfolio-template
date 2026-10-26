# Home/Lab Network Security Baseline Assessment

| Document control | Value |
|---|---|
| Assessment ID | NETSEC-LAB-01 / baseline-2026-10-20 |
| Assessment type | Authorized, non-destructive home/lab network security baseline |
| Assessment window | 2026-10-20 09:00–11:00 UTC |
| Assessor | Training Team Alpha |
| Owner / approver | Lab Owner — `LAB-AUTH-2026-10-20` |
| Classification | Training dataset; documentation-only addresses |
| Version | 1.0 |

## 1. Executive summary

This assessment reviewed the exposed services and a short, sanitized packet-observation dataset for `NETSEC-LAB-01`, a four-asset training network. The review confirmed that `LAB-WEB-01` exposed TCP 80 and TCP 443 during the authorized window; TCP 22 was closed from the approved assessment position. The supplied capture summary showed normal DNS request/response traffic, a completed TCP three-way handshake to HTTPS, and a TLS handshake.

The primary risk is **medium**: an HTTP listener exists alongside HTTPS, but this baseline did not establish whether it redirects safely, serves content, or accepts credentials. The immediate actions are to verify HTTPS-only behavior, maintain a documented allowlist firewall policy, and introduce periodic patch/certificate review. No exploitation, credential testing, vulnerability scanning, traffic decryption, or changes to network devices occurred.

This report is an evidence-based snapshot—not a penetration test, vulnerability certification, or proof that unobserved systems are secure.

## 2. Scope, authorization, and exclusions

The completed authorization record is [scope.md](scope.md). In scope were only `LAB-WEB-01`, the documented topology, and an instructor-provided sanitized capture summary. The source was `ANALYST-01`; the approved methods were a limited TCP connect/service check for ports 22, 80, and 443, document review, and packet analysis.

The Internet, campus/shared networks, neighbours' devices, full port ranges, UDP, password testing, scripts, exploitation, denial of service, raw personal traffic, and any configuration changes were expressly excluded. Assessment stopped at the first evidence needed for each observation.

## 3. Environment and data provenance

The asset record is [inventory.csv](inventory.csv) and the network diagram is [topology.mmd](topology.mmd). All addresses use the `192.0.2.0/24` documentation block and labels, not routable or personal network identifiers. The evidence register and source handling rules are in [data-provenance.md](../instructions/data-provenance.md).

| Zone | Assets | Security boundary | Expected role |
|---|---|---|---|
| Edge | `LAB-RTR` | NAT/firewall between lab and upstream | Enforce documented inbound/outbound policy |
| Lab user | `ANALYST-01` | User-to-server access boundary | Authorized assessment workstation only |
| Lab server | `LAB-WEB-01` | Web-service exposure boundary | HTTP redirect / HTTPS application service |
| Infrastructure | `LAB-DNS` | Name-resolution boundary | Lab-only resolver |

## 4. Methodology

### 4.1 Inventory and topology review

Assets, owner, zone, criticality, expected service, and review state were documented before observation. Known information is shown as fact; assumed policy intent is explicitly marked as an assumption.

### 4.2 Limited service observation

The exact approved command and execution record are in [scan-plan.md](../instructions/scan-plan.md). It used a TCP connect scan, targeted only three approved ports, and requested light service/version identification:

```text
nmap -sT -sV --version-light --reason -Pn -p 22,80,443 LAB-WEB-01
```

The original training XML is [lab-web-01-nmap.xml](../data/lab-web-01-nmap.xml). `-sV` uses service probes to identify what responds; `--version-light` deliberately uses a lower-intensity probe set, so this evidence is useful for inventory but does not prove a service identity or patch level.

### 4.3 Packet observation

No live capture was taken for this completed example. The analysis used the sanitized three-event record in [capture-summary.csv](../data/capture-summary.csv) and the completed observation worksheet in [wireshark-observations-completed.md](../data/wireshark-observations-completed.md). Filters and analyst questions are documented in [wireshark-analysis-guide.md](../instructions/wireshark-analysis-guide.md). Packet content, endpoint MAC addresses, private addresses, and session identifiers were not retained.

### 4.4 Evidence quality rules

Each conclusion names the source, direct observation, confidence, and limitation. A TCP state is not a vulnerability; a service label is not a version guarantee; TLS handshake packets do not validate certificate trust or application security.

## 5. Results

### 5.1 Service exposure

| Evidence ID | Target | TCP port | State | Nmap service label | Direct conclusion | Confidence |
|---|---|---:|---|---|---|---|
| NMAP-01 | LAB-WEB-01 | 22 | closed | ssh | No TCP listener was reachable from `ANALYST-01` during this observation. | High |
| NMAP-02 | LAB-WEB-01 | 80 | open | http | A TCP service answered on the standard HTTP port. | High |
| NMAP-03 | LAB-WEB-01 | 443 | open | https | A TCP service answered on the standard HTTPS port. | High |

**Interpretation:** The intended application exposure may be HTTPS-only with port 80 used for redirects; that is an owner assertion to validate, not a conclusion of the scan. The limited port list does not characterize every service, filtering rule, VLAN path, UDP service, or host on the network.

### 5.2 Capture observations

| Evidence ID | Filter / source | Direct observation | Security relevance | Limitation |
|---|---|---|---|---|
| PCAP-01 | `dns` / capture summary row 1 | DNS request and response were recorded between `ANALYST-01` and `LAB-DNS`. | Confirms name resolution occurred in this sample. | Does not assess resolver recursion, DNSSEC, logging, or all client traffic. |
| PCAP-02 | Initial SYN filter / row 2 | SYN, SYN/ACK, ACK sequence completed from `ANALYST-01` to `LAB-WEB-01:443`. | Confirms a TCP connection was established in the sample. | Does not prove user authorization or application request success. |
| PCAP-03 | `tls` / row 3 | TLS ClientHello and ServerHello were recorded. | Confirms negotiation traffic was visible. | Does not validate protocol version, cipher suite, certificate chain, hostname validation, or encrypted payload. |

## 6. Security posture and risk register

Risk scores are a local prioritization aid: **Risk = likelihood (1–5) × impact (1–5)**. They are not CVSS scores and do not represent a vulnerability scanner result.

| ID | Condition / evidence | Likelihood | Impact | Score | Rating | Rationale | Owner |
|---|---|---:|---:|---:|---|---|---|
| R-01 | HTTP is reachable on TCP 80 (NMAP-02); redirect/content behavior unverified. | 3 | 3 | 9 | Medium | If non-redirect content or authentication is available over HTTP, confidentiality/session risk increases. | Web Owner |
| R-02 | HTTPS is reachable (NMAP-03), but TLS/certificate policy was not assessed. | 2 | 3 | 6 | Medium | Encryption was observed but quality and lifecycle are unknown. | Web Owner |
| R-03 | Service/firewall inventory is only partially documented. | 3 | 3 | 9 | Medium | Undocumented exceptions make least-privilege review difficult. | Network Owner |
| R-04 | Patch, backup, account, wireless, and endpoint controls were out of scope. | 2 | 4 | 8 | Medium | Important risk areas have no evidence in this baseline. | System Owner |

## 7. Recommendations and remediation plan

| Priority | Action | Evidence / risk | Implementation notes | Owner | Target | Validation / rollback |
|---:|---|---|---|---|---|---|
| 1 | Validate and enforce HTTPS-only application behavior. Redirect HTTP to HTTPS; enable HSTS only after compatibility approval. | R-01 / NMAP-02 | Do not assume a redirect is safe: ensure no login, session, or sensitive content is returned over HTTP. | Web Owner | 14 days | Approved browser request to port 80 returns a redirect with no sensitive body. Roll back via approved web configuration. |
| 2 | Create an allowlist firewall/service matrix for edge and host controls. Default-deny non-required inbound flows. | R-03 | Document source zone, destination, port/protocol, business owner, review date, and expiry for every allow rule. | Network Owner | 30 days | Compare approved matrix to rules; repeat the limited scan from approved vantage point. Keep console access and approved previous rules for rollback. |
| 3 | Establish a recurring patch and TLS certificate review. | R-02/R-04 | Track owner, maintenance window, severity, certificate expiry, and exception expiry. | System + Web Owners | 30 days | Change record plus package/certificate review; do not infer patch state from Nmap output. |
| 4 | Repeat this baseline after topology, router, ISP, web-service, or firewall change. | All | Preserve only sanitized derived evidence. | Network Owner | Quarterly / change-driven | Compare inventory, approved service matrix, and observation deltas. |

## 8. Limitations and next assessment scope

The assessment covered one source point, one server, three TCP ports, and a short derived capture record. It did not test IPv6, Wi-Fi configuration, router administration, DNS security, host firewall rules, TLS configuration, software versions, credentials, application behavior, UDP, segmentation, monitoring, backups, or incident response. Any risk outside these observations remains unknown—not low.

The next approved assessment should validate the HTTP redirect behavior, TLS certificate/protocol configuration, rule-to-service matrix, host patch state, and Wi-Fi/router administration controls. Those checks require separate scope and may need owners from network, web, and endpoint teams.

## 9. Final assessment statement

The lab has a documented starting baseline and no confirmed compromise was observed. The evidence supports focused configuration validation and governance improvements, especially around HTTP exposure and service/firewall documentation. The recommendation plan should be implemented through normal owner approval and change control, then retested with the same limited, authorized method.
