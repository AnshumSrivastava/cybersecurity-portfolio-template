# Flag Submission & Proof of Concept

Evidence and root-cause analysis for flags captured during the Local Cybersecurity CTF.

---

### Submission: Challenge 1 — The Hidden Variable

* **Flag:** `FLAG{h1dd3n_d0tf1l3s_r3v34l_s3cr3ts}`
* **How I Found It:** Inspected the `server/files/` directory using `ls -la`. Noticed the hidden `.user_profile` configuration file. Ran `grep` to extract the flag pattern.
* **Commands Used:**
  ```bash
  ls -la server/files/
  grep "FLAG" server/files/.user_profile
  ```
* **Evidence:**
  ```text
  export DB_PASSWORD="SuperSecretPassword123"
  export CTF_FLAG="FLAG{h1dd3n_d0tf1l3s_r3v34l_s3cr3ts}"
  ```
* **Concept Involved:** Secrets management in configuration profiles. Sensitive variables should be loaded from encrypted secret vaults or securely isolated keyrings, not tracked in plaintext dotfiles.

---

### Submission: Challenge 2 — Network Whisperer

* **Flag:** `FLAG{b4nn3r_gr4bb1ng_l1k3_4_pr0}`
* **How I Found It:** Ran a local socket inspection using `ss -tuln` to locate unconventional open TCP ports. Discovered port `9001` in a LISTEN state. Interacted with it via Netcat to trigger the welcome banner.
* **Commands Used:**
  ```bash
  ss -tuln | grep ":9001"
  nc 127.0.0.1 9001
  ```
* **Evidence:**
  ```text
  === WELCOME TO INTERNAL TEST DAEMON ===
  DEBUG SERVICE ACTIVE. KEY: FLAG{b4nn3r_gr4bb1ng_l1k3_4_pr0}
  ```
* **Concept Involved:** Unauthenticated debugging daemons left exposed on network interfaces. Services should bind exclusively to required interfaces and authenticate clients.

---

### Submission: Challenge 3 — Insecure Directory Permissions

* **Flag:** `FLAG{w0rld_r34d4bl3_b4ckup_d4t4}`
* **How I Found It:** Identified unhardened file permissions allowing global read access (`-rw-r--r--`) on database dump files.
* **Commands Used:**
  ```bash
  find server/files -type f -perm -o=r -name "*.sql"
  grep -i "FLAG{" server/files/backup_2026.sql
  ```
* **Evidence:**
  ```sql
  INSERT INTO system_config (param_name, param_value) VALUES ('ctf_flag', 'FLAG{w0rld_r34d4bl3_b4ckup_d4t4}');
  ```
* **Concept Involved:** Principle of Least Privilege and access control misconfigurations. Production backups containing sensitive data must have strict file permissions (`600`) and reside outside world-accessible locations.
