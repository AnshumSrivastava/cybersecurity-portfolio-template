# Practical Linux Tasks

Hands-on problem-solving exercises executed from the command line.

---

## Task 1: Directory & File Lifecycle

**Challenge:** Create a directory called `cyber-lab`, create three files inside it, rename one, copy one, and delete one.

### Execution:

1. Create directory structure:
   ```bash
   mkdir -p cyber-lab
   ```
2. Create 3 files:
   ```bash
   touch cyber-lab/file1.txt cyber-lab/file2.txt cyber-lab/file3.txt
   ```
3. Rename one file:
   ```bash
   mv cyber-lab/file1.txt cyber-lab/renamed_file1.txt
   ```
4. Copy one file:
   ```bash
   cp cyber-lab/file2.txt cyber-lab/copied_file2.txt
   ```
5. Delete one file:
   ```bash
   rm cyber-lab/file3.txt
   ```
6. Verify result:
   ```bash
   ls -la cyber-lab
   ```

**Observation:**
The directory contains `renamed_file1.txt`, `file2.txt`, and `copied_file2.txt`, while `file3.txt` is removed.

---

## Task 2: Permission Hardening

**Challenge:** Create a confidential document and restrict all permissions so only the owner can read and write to it.

### Execution:
```bash
echo "CONFIDENTIAL: API_KEY=xyz123" > cyber-lab/credentials.env
chmod 600 cyber-lab/credentials.env
ls -l cyber-lab/credentials.env
```

**Observation:**
Permissions change to `-rw-------`, preventing read/write access from any other system user or group.

---

## Task 3: Text Search & Extraction Pipeline

**Challenge:** Count total occurrences of failed login entries in system log data.

### Execution:
```bash
grep -i "failed" /var/log/auth.log 2>/dev/null | wc -l
```

**Observation:**
Chaining `grep` with `wc -l` via a pipe filters matching lines and yields line counts directly.
