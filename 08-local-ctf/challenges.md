# Local CTF Challenges

Detailed description of challenges, vulnerability categories, target artifacts, solutions, and learning outcomes.

---

## Challenge 1: The Hidden Variable

* **Category:** Linux / Environment & Hidden Files
* **Points:** 100
* **Objective:** Discover a flag hidden inside user environment profiles or dotfiles.
* **Target File:** `server/files/.user_profile`
* **Hint:** Look at hidden configuration files (`.*`) in user home or project directories.
* **Walkthrough Solution:**
  ```bash
  ls -la server/files/
  grep -rn "FLAG{" server/files/
  ```
* **Discovered Flag:** `FLAG{h1dd3n_d0tf1l3s_r3v34l_s3cr3ts}`
* **Vulnerability Concept:** Storing sensitive secrets, API keys, and environment variables in plaintext dotfiles inside shared directory trees.

---

## Challenge 2: Network Whisperer

* **Category:** Networking / Sockets & Banner Grabbing
* **Points:** 150
* **Objective:** Connect to a listening local port broadcasting flag fragments.
* **Target Port:** TCP 9001 (or local mock server)
* **Hint:** Use socket inspection utilities to locate non-standard listening ports and raw connection tools to retrieve service banners.
* **Walkthrough Solution:**
  ```bash
  # Step 1: Discover listening TCP ports
  ss -tuln | grep "9001"
  # Step 2: Connect using Netcat to extract banner
  nc 127.0.0.1 9001
  ```
* **Discovered Flag:** `FLAG{b4nn3r_gr4bb1ng_l1k3_4_pr0}`
* **Vulnerability Concept:** Exposed unauthenticated network daemon leaking operational data through default connection banners.

---

## Challenge 3: Insecure Directory Permissions & Backup Discovery

* **Category:** File Systems / Insecure File Permissions
* **Points:** 200
* **Objective:** Locate a sensitive database backup file stored with overly permissive world-readable permissions.
* **Target File:** `server/files/backup_2026.sql`
* **Hint:** Use `find` to search for files with specific permission masks or `.sql` extensions.
* **Walkthrough Solution:**
  ```bash
  # Find files readable by everyone
  find server/files -type f -perm -o=r -name "*.sql"
  grep -i "FLAG{" server/files/backup_2026.sql
  ```
* **Discovered Flag:** `FLAG{w0rld_r34d4bl3_b4ckup_d4t4}`
* **Vulnerability Concept:** Broken Access Control (OWASP A01). Sensitive production backups must use restrictive permissions (`chmod 600` or `700`) and reside outside publicly accessible directories.

---

## Challenge 4: Insecure Direct Object Reference (IDOR) in Web Portal

* **Category:** Web Application Security
* **Points:** 250
* **Objective:** Exploit an insecure user ID parameter in the web service to access another user's invoice receipt.
* **Target Service:** `server/web/invoice.php?user_id=102`
* **Hint:** Inspect client requests in browser dev tools or curl, and tamper with sequential object identifiers.
* **Walkthrough Solution:**
  ```bash
  curl -s "http://127.0.0.1:8080/invoice.php?user_id=1"
  ```
* **Discovered Flag:** `FLAG{1d0r_p4r4m_t4mp3r1ng_pwn}`
* **Vulnerability Concept:** Lack of server-side authorization checks when accessing database records via user-supplied parameters.
