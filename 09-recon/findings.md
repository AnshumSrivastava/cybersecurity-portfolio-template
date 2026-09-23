# Reconnaissance Findings Report

A comprehensive intelligence report synthesizing passive OSINT, DNS zone enumeration, TLS certificate transparency inspection, and HTTP perimeter headers.

---

## 1. Executive Summary

A non-intrusive reconnaissance assessment was conducted against `internal-target.lab` (IP: `192.168.1.50`). The assessment adhered strictly to passive and semi-passive discovery techniques to map the external attack surface without triggering active IDS/IPS alerts or violating engagement boundaries.

---

## 2. DNS Infrastructure & Mail Footprinting

* **A Records:** `internal-target.lab` → `192.168.1.50`
* **Name Servers (NS):** `ns1.internal-target.lab` (`192.168.1.1`)
* **Mail Exchange (MX):**
  * `mail.internal-target.lab` (Preference 10) → `192.168.1.25`
  * Demonstrates presence of a dedicated mail gateway within the target organization.
* **Sender Policy Framework (SPF):**
  * Record: `v=spf1 mx ip4:192.168.1.0/24 -all`
  * Meaning: Hard fail (`-all`) prevents unauthorized mail spoofing from IPs outside the specified range.
* **DNS Zone Transfer Check:**
  * Command: `dig axfr @192.168.1.1 internal-target.lab`
  * Result: `Transfer failed: REFUSED` (Secured against unauthorized zone dumps).

---

## 3. Web Perimeter & HTTP Response Headers

A non-intrusive HEAD request to port 80 and 443 yielded:

```http
HTTP/1.1 200 OK
Date: Wed, 23 Sep 2026 08:30:00 GMT
Server: Apache/2.4.52 (Ubuntu)
X-Powered-By: PHP/8.1.2
Content-Type: text/html; charset=UTF-8
```

### Security Header Audit Table

| HTTP Header | Status | Recommended Value | Security Purpose |
| :--- | :--- | :--- | :--- |
| **Strict-Transport-Security** | Missing | `max-age=31536000; includeSubDomains` | Enforces HTTPS; prevents SSL stripping. |
| **Content-Security-Policy** | Missing | `default-src 'self'` | Prevents Cross-Site Scripting (XSS) and data injection. |
| **X-Frame-Options** | Missing | `DENY` or `SAMEORIGIN` | Defends against Clickjacking attacks. |
| **X-Content-Type-Options** | Missing | `nosniff` | Prevents MIME-type sniffing vulnerabilities. |
| **Referrer-Policy** | Missing | `strict-origin-when-cross-origin` | Protects leakage of sensitive URLs to third parties. |
| **Server / X-Powered-By** | **EXPOSED** | *Suppress completely* | Leaks exact daemon & runtime version details. |

---

## 4. TLS Certificate Analysis

* **Subject:** `CN=internal-target.lab, O=Lab Security Team`
* **Issuer:** Lab Internal CA
* **Validity Period:** 2026-01-01 to 2027-01-01
* **Public Key Algorithm:** RSA 2048-bit (SHA-256 with RSA Signature)
* **Subject Alternative Names (SANs):**
  * `internal-target.lab`
  * `vpn.internal-target.lab`
  * `dev.internal-target.lab`
  * `portal.internal-target.lab`
* **Intelligence Takeaway:** The SAN extension reveals internal hostnames (`vpn`, `dev`, `portal`), giving security teams valuable targets for defensive perimeter audits.

---

## 5. Recommended Defensive Action Items

1. **Information Leakage Suppression:** Disable verbose server headers in web daemon configuration (`ServerTokens Prod`, `ServerSignature Off`, `expose_php = Off`).
2. **Perimeter Hardening:** Apply strict HTTP security headers via Apache/Nginx reverse proxy configurations.
3. **Subdomain Isolation:** Ensure staging/dev subdomains (`dev.internal-target.lab`) are isolated from public routing and require MFA authentication.
