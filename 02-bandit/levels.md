# Bandit Challenge Walkthrough

Detailed documentation of Bandit levels, problem breakdowns, command sequences, reasoning, and security concepts.

---

## Level 0 → Level 1

* **Problem:** Password is stored in a file called `readme` in the home directory.
* **Command(s):**
  ```bash
  cat readme
  ```
* **Reasoning:** Standard file read via `cat` displays plaintext contents.
* **Result:** Password retrieved.
* **What I learned:** Basic file inspection over SSH.

---

## Level 1 → Level 2

* **Problem:** Password is stored in a file named `-`.
* **Command(s):**
  ```bash
  cat ./-
  ```
* **Reasoning:** Standard utilities interpret `-` as standard input (STDIN). Using `./-` specifies relative path context so `cat` treats it as a filename.
* **Result:** Password retrieved.
* **What I learned:** How Linux handles file flags vs relative file paths.

---

## Level 2 → Level 3

* **Problem:** Password is stored in a file named `spaces in this filename`.
* **Command(s):**
  ```bash
  cat "spaces in this filename"
  # or cat spaces\ in\ this\ filename
  ```
* **Reasoning:** Shell words are split by whitespace unless quoted or escaped with backslashes.
* **Result:** Password retrieved.
* **What I learned:** Shell parameter escaping and quotation rules.

---

## Level 3 → Level 4

* **Problem:** Password is stored in a hidden file in the `inhere` directory.
* **Command(s):**
  ```bash
  ls -la inhere/
  cat inhere/.hidden
  ```
* **Reasoning:** Files prefixed with `.` are hidden by default in `ls`. The `-a` flag reveals all entries.
* **Result:** Password retrieved.
* **What I learned:** Linux convention for hidden configuration and sensitive files.

---

## Level 4 → Level 5

* **Problem:** Password is stored in the only human-readable file in the `inhere` directory among multiple binary files.
* **Command(s):**
  ```bash
  file inhere/*
  cat inhere/-file07
  ```
* **Reasoning:** `file` command inspects magic bytes to identify ASCII text vs binary data.
* **Result:** Password retrieved.
* **What I learned:** Distinguishing binary files from human-readable text.

---

## Level 5 → Level 6

* **Problem:** File properties: human-readable, 1033 bytes in size, not executable.
* **Command(s):**
  ```bash
  find inhere/ -type f -size 1033c ! -executable -exec cat {} +
  ```
* **Reasoning:** `find` queries the filesystem by exact metadata predicates (`-size 1033c`, `! -executable`).
* **Result:** Password retrieved.
* **What I learned:** Powerful filtering techniques using `find`.

---

## Level 6 → Level 7

* **Problem:** Password is owned by user `bandit7`, group `bandit6`, and is 33 bytes in size somewhere on the server.
* **Command(s):**
  ```bash
  find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
  ```
* **Reasoning:** Searching root `/` produces permission denied warnings on other user directories. `2>/dev/null` silences STDERR noise.
* **Result:** File identified at `/var/lib/dpkg/info/bandit7.password`.
* **What I learned:** File ownership filtering and redirecting STDERR (`2>`).

---

## Level 7 → Level 8

* **Problem:** Password is next to the word "millionth" in `data.txt`.
* **Command(s):**
  ```bash
  grep "millionth" data.txt
  ```
* **Reasoning:** Fast text filtering with `grep` extracts the target row from a large dataset.
* **Result:** Password retrieved.
* **What I learned:** Pattern matching against large datasets.

---

## Level 8 → Level 9

* **Problem:** Password is the only line of text that occurs only once in `data.txt`.
* **Command(s):**
  ```bash
  sort data.txt | uniq -u
  ```
* **Reasoning:** `uniq` only detects adjacent duplicate lines, so input must be sorted first. `-u` prints unique lines only.
* **Result:** Password retrieved.
* **What I learned:** Sorting and deduplication pipelines in Unix.

---

## Level 9 → Level 10

* **Problem:** Password is stored in `data.txt` in one of the few human-readable strings, preceded by several '=' characters.
* **Command(s):**
  ```bash
  strings data.txt | grep "==="
  ```
* **Reasoning:** `strings` extracts sequences of printable characters from binary/mixed data files, while `grep` isolates the target line with equal signs.
* **Result:** Password retrieved.
* **What I learned:** Extracting embedded ASCII strings from compiled or corrupted binary payloads.

---

## Level 10 → Level 11

* **Problem:** Password is stored in `data.txt`, which contains base64 encoded data.
* **Command(s):**
  ```bash
  base64 -d data.txt
  ```
* **Reasoning:** The `base64` utility with the `-d` (decode) flag reverses base64 ASCII armoring back into plaintext.
* **Result:** Password retrieved.
* **What I learned:** Encoding is not encryption; base64 is an encoding format designed for transport, easily reversed.

---

## Level 11 → Level 12

* **Problem:** Password is stored in `data.txt`, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions (ROT13).
* **Command(s):**
  ```bash
  cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
  ```
* **Reasoning:** `tr` replaces characters in set 1 with corresponding characters in set 2. Rotating characters by 13 decodes Caesar cipher / ROT13.
* **Result:** Password retrieved.
* **What I learned:** Substitution ciphers and character transliteration using `tr`.

---

## Level 12 → Level 13

* **Problem:** Password is stored in `data.txt`, which is a hexdump of a file that has been repeatedly compressed with multiple formats (gzip, bzip2, tar).
* **Command(s):**
  ```bash
  mkdir -p /tmp/work && cp data.txt /tmp/work && cd /tmp/work
  xxd -r data.txt decompressed
  file decompressed
  # Progressively inspect magic bytes with 'file' and decompress:
  # mv decompressed file.gz && gunzip file.gz
  # mv file file.bz2 && bunzip2 file.bz2
  # mv file file.tar && tar -xf file.tar
  ```
* **Reasoning:** `xxd -r` restores binary from hexdump. Identifying actual compression headers with `file` avoids relying on misleading file extensions.
* **Result:** Original password ASCII file unpacked.
* **What I learned:** Magic bytes file identification and multi-layer decompression workflows.

---

## Level 13 → Level 14

* **Problem:** Password for bandit14 can be retrieved by logging in using an SSH private key stored at `sshkey.private`.
* **Command(s):**
  ```bash
  ssh -i sshkey.private bandit14@localhost -p 2220
  cat /etc/bandit_pass/bandit14
  ```
* **Reasoning:** SSH supports asymmetric public-key cryptography. Passing private key identity via `-i` authenticates without interactive password prompt.
* **Result:** User authenticated as bandit14 and password read.
* **What I learned:** SSH key-based authentication and secure identity management.

---

## Level 14 → Level 15

* **Problem:** Password can be retrieved by submitting the current level's password to port 30000 on `localhost`.
* **Command(s):**
  ```bash
  nc localhost 30000
  # or: echo "<bandit14_password>" | nc localhost 30000
  ```
* **Reasoning:** Netcat (`nc`) connects to raw TCP sockets, streams input directly to the listening port, and receives response data.
* **Result:** Server validated password and returned bandit15 password.
* **What I learned:** Interacting with TCP network daemons without high-level protocols.

---

## Level 15 → Level 16

* **Problem:** Password retrieved by submitting current password to port 30001 on `localhost` using SSL/TLS encryption.
* **Command(s):**
  ```bash
  openssl s_client -connect localhost:30001
  # enter <bandit15_password>
  ```
* **Reasoning:** Standard Netcat speaks unencrypted TCP. `openssl s_client` establishes an encrypted TLS session before data transmission.
* **Result:** SSL handshake verified; server transmitted bandit16 credentials.
* **What I learned:** Encrypted socket communications and TLS certificate handshakes.

---

## Level 16 → Level 17

* **Problem:** Credentials located on an unknown port between 31000 and 32000 on `localhost` listening with SSL.
* **Command(s):**
  ```bash
  nmap -p 31000-32000 --open -sV localhost
  openssl s_client -connect localhost:<port>
  ```
* **Reasoning:** Nmap sweeps the designated port range to find open SSL services. Connecting via OpenSSL provides the next stage SSH private key.
* **Result:** Identified listening SSL port and retrieved private key.
* **What I learned:** Port range discovery and combining reconnaissance with encryption tools.
