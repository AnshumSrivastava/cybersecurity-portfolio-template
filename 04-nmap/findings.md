# Nmap Reconnaissance & Vulnerability Assessment Findings

A comprehensive technical report detailing network mapping, port discovery, banner grabbing, NSE script auditing, and defensive remediation guidance.

---

## 1. Executive Summary

A systematic, authorized port and service enumeration assessment was performed across the `192.168.1.0/24` lab subnet. The primary target identified was `192.168.1.50` (Linux/Ubuntu 22.04 LTS host). The scan uncovered exposed remote administration (SSH), web services (HTTP/HTTPS), and an externally reachable relational database daemon (MySQL).

---

## 2. Methodology & Progression

The reconnaissance workflow followed the four standard stages:

```text
Stage 1: Host Discovery (Ping Sweep / ARP Probes)
           ↓
Stage 2: Port Enumeration (Full Range SYN Stealth Scan)
           ↓
Stage 3: Service & Version Fingerprinting (-sV + Banner Grabbing)
           ↓
Stage 4: Automated Vulnerability & Configuration Scripts (-sC / --script vuln)
```

---

## 3. Stage-by-Stage Breakdown & Results

### Stage 1: Host Discovery
* **Command:** `nmap -sn -PE -PP -PS22,80,443 -PA80,3389 -PU53 192.168.1.0/24`
* **Log Reference:** [`scans/host-discovery.txt`](./scans/host-discovery.txt)
* **Technical Details:**
  * Uses ARP requests for local ethernet segments (Layer 2) and ICMP Echo (`-PE`) / Timestamp (`-PP`) / TCP SYN/ACK probes across routed boundaries.
  * Identified active nodes:
    * `192.168.1.1` — Network Gateway (Latency: 1.2ms)
    * `192.168.1.50` — Primary Target Server (Latency: 0.4ms)
    * `192.168.1.105` — Lab Testing Workstation (Latency: 0.1ms)

### Stage 2: Port Scanning (SYN Stealth)
* **Command:** `nmap -sS -p- -T4 --min-rate 1000 -v -n 192.168.1.50 -oN scans/port-scan.txt`
* **Log Reference:** [`scans/port-scan.txt`](./scans/port-scan.txt)
* **Technical Details:**
  * Uses half-open SYN packets (`SYN` sent → target responds `SYN/ACK` → Nmap sends `RST`). Connections are never completed, avoiding full handshake logging on legacy socket monitors.
  * Discovered Open Ports:
    * `22/tcp` (State: open)
    * `80/tcp` (State: open)
    * `443/tcp` (State: open)
    * `3306/tcp` (State: open)

### Stage 3: Service & Version Detection
* **Command:** `nmap -sV --version-intensity 7 -p 22,80,443,3306 192.168.1.50`
* **Log Reference:** [`scans/service-scan.txt`](./scans/service-scan.txt)
* **Fingerprinted Versions:**
  * **Port 22/tcp:** `OpenSSH 8.9p1 Ubuntu 3ubuntu0.6` (Ubuntu Linux; Protocol 2.0)
  * **Port 80/tcp:** `Apache httpd 2.4.52` ((Ubuntu))
  * **Port 443/tcp:** `Apache httpd 2.4.52` ((Ubuntu)) OpenSSL/3.0.2
  * **Port 3306/tcp:** `MySQL 8.0.35` (Protocol 10, Auth plugin: `caching_sha2_password`)

### Stage 4: NSE Script Engine Analysis
* **Command:** `nmap --script "default,vuln" -p 22,80,443,3306 192.168.1.50`
* **Key Observations:**
  * `http-enum`: Discovered directories `/admin/`, `/phpmyadmin/`, `/backup/`.
  * `ssl-cert`: Certificate valid for `*.internal-target.lab`, self-signed, expiring in 365 days. Weak TLS 1.0/1.1 disabled; TLS 1.2 and TLS 1.3 supported.
  * `mysql-vuln-cve2012-2122`: Not vulnerable to authentication bypass.
  * `ssh2-enum-algos`: Key exchange algorithms include modern Curve25519 and Diffie-Hellman group 14.

---

## 4. Threat Matrix & Risk Scoring

| Port | Service | Software Version | Risk Level | Threat Scenario |
| :--- | :--- | :--- | :--- | :--- |
| **22** | SSH | OpenSSH 8.9p1 | Medium | Password brute-force if password auth enabled; potential credential stuffing. |
| **80** | HTTP | Apache 2.4.52 | Medium | Cleartext credentials transmission; unencrypted web traffic susceptible to interception. |
| **443**| HTTPS | Apache 2.4.52 | Low | Web application attack vectors (OWASP Top 10) on underlying code. |
| **3306**| MySQL | MySQL 8.0.35 | High | Direct exposure of database port to network perimeter; risks authentication brute force. |

---

## 5. Defensive Remediation & Hardening Plan

1. **Remediate Database Exposure (Port 3306):**
   * Edit `/etc/mysql/mysql.conf.d/mysqld.cnf`:
     ```ini
     bind-address = 127.0.0.1
     ```
   * Enforce firewall isolation via `iptables` or `ufw`:
     ```bash
     sudo ufw deny 3306/tcp
     ```

2. **Harden Remote SSH Administration (Port 22):**
   * Enforce key-based login and disable root login in `/etc/ssh/sshd_config`:
     ```text
     PermitRootLogin no
     PasswordAuthentication no
     MaxAuthTries 3
     ```
   * Implement fail2ban to mitigate brute-force attempts.

3. **Enforce HTTPS Encryption (Port 80 → 443):**
   * Configure Apache virtual host with mandatory 301 redirection:
     ```apache
     <VirtualHost *:80>
         ServerName internal-target.lab
         Redirect permanent / https://internal-target.lab/
     </VirtualHost>
     ```
   * Enable HSTS header:
     ```apache
     Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains"
     ```

4. **Information Leakage Suppression:**
   * Disable Apache server signature in `/etc/apache2/conf-enabled/security.conf`:
     ```apache
     ServerTokens Prod
     ServerSignature Off
     ```
