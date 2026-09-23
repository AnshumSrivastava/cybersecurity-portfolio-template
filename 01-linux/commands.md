# Linux Commands Reference

Documenting essential Linux CLI commands with observed outputs and purpose.

---

### Command: `pwd`
* **Purpose:** Print current working directory
* **Syntax:** `pwd`
* **Example:**
  ```bash
  pwd
  ```
* **What I observed:** Returns absolute path from root `/` to current directory (e.g. `/home/user/workspace`).

---

### Command: `ls`
* **Purpose:** List directory contents
* **Syntax:** `ls [options] [path]`
* **Example:**
  ```bash
  ls -la
  ```
* **What I observed:** Shows hidden files (starting with `.`), permissions, ownership, byte size, and last modified timestamps.

---

### Command: `cd`
* **Purpose:** Change directory
* **Syntax:** `cd [path]`
* **Example:**
  ```bash
  cd /var/log && pwd
  ```
* **What I observed:** Moves shell environment context into target path. `cd ..` navigates to parent directory.

---

### Command: `mkdir`
* **Purpose:** Make directories
* **Syntax:** `mkdir [options] <directory_name>`
* **Example:**
  ```bash
  mkdir -p cyber-lab/evidence
  ```
* **What I observed:** Creates directory structure; `-p` flag automatically creates missing parent directories without throwing errors.

---

### Command: `touch`
* **Purpose:** Create empty files or update timestamps
* **Syntax:** `touch <filename>`
* **Example:**
  ```bash
  touch cyber-lab/notes.txt
  ```
* **What I observed:** Instantly creates a 0-byte file if it doesn't already exist, or touches access/modification timestamps if it does.

---

### Command: `cp`
* **Purpose:** Copy files and directories
* **Syntax:** `cp [options] <source> <destination>`
* **Example:**
  ```bash
  cp cyber-lab/notes.txt cyber-lab/notes_backup.txt
  ```
* **What I observed:** Duplicates file content into a distinct target inode.

---

### Command: `mv`
* **Purpose:** Move or rename files and directories
* **Syntax:** `mv <source> <destination>`
* **Example:**
  ```bash
  mv cyber-lab/notes_backup.txt cyber-lab/notes_archive.txt
  ```
* **What I observed:** Renames file instantly within same filesystem without re-copying data blocks.

---

### Command: `rm`
* **Purpose:** Remove files or directories
* **Syntax:** `rm [options] <target>`
* **Example:**
  ```bash
  rm cyber-lab/notes_archive.txt
  ```
* **What I observed:** Deletes directory entry and unlinks inode; file is permanently deleted from filesystem.

---

### Command: `cat`
* **Purpose:** Concatenate and display file content
* **Syntax:** `cat <filename>`
* **Example:**
  ```bash
  cat /etc/os-release
  ```
* **What I observed:** Streams whole file content directly into STDOUT.

---

### Command: `head` & `tail`
* **Purpose:** Display beginning or end lines of text
* **Syntax:** `head -n <N> <file>`, `tail -n <N> <file>`
* **Example:**
  ```bash
  head -n 5 /etc/passwd
  tail -n 5 /var/log/syslog
  ```
* **What I observed:** Inspects specific line counts without loading huge files into memory.

---

### Command: `grep`
* **Purpose:** Search for pattern matches in text streams
* **Syntax:** `grep [options] "<pattern>" <file>`
* **Example:**
  ```bash
  grep -i "error" /var/log/syslog
  ```
* **What I observed:** Isolates lines matching criteria. Supports case-insensitivity (`-i`), line numbering (`-n`), and recursive search (`-r`).

---

### Command: `find`
* **Purpose:** Search for files in a directory hierarchy
* **Syntax:** `find <path> -name "<pattern>"`
* **Example:**
  ```bash
  find /var/log -name "*.log"
  ```
* **What I observed:** Recursively traverses paths matching file names, permissions, size, or modification timestamps.

---

### Command: `chmod`
* **Purpose:** Change file mode bits (permissions)
* **Syntax:** `chmod <octal_or_symbolic> <file>`
* **Example:**
  ```bash
  chmod 700 secret.txt
  ```
* **What I observed:** `700` (`rwx------`) restricts reading, writing, and execution strictly to file owner.

---

### Command: `ps`
* **Purpose:** Report snapshot of current processes
* **Syntax:** `ps [options]`
* **Example:**
  ```bash
  ps aux
  ```
* **What I observed:** Lists PID, user, CPU%, memory%, and command strings for every active process.

---

### Command: `ip` & `ss`
* **Purpose:** Show network configuration and socket statistics
* **Syntax:** `ip addr`, `ss -tuln`
* **Example:**
  ```bash
  ip addr
  ss -tuln
  ```
* **What I observed:** `ip addr` reveals network interfaces and IP addresses; `ss -tuln` shows active TCP/UDP listening ports and sockets.
