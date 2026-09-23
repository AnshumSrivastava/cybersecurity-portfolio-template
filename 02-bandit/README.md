# 02 — Linux Bandit Challenge

## Objective

Use command-line utilities and shell techniques to solve progressively difficult cybersecurity challenges on OverTheWire Bandit:

> *"You have information, but you don't know where it is or how it is encoded."*

---

## What Problem Were We Solving?
Navigating obscured environments, locating hidden files, decoding multi-format data streams (base64, rot13, hex, compressed archives), and analyzing permissions.

## Key Concepts Practiced
* Finding hidden and special files (`.hidden`, `-filename`, spaces in filenames)
* Data filtering by size, owner, and readability attributes (`find . -size 1033c ! -executable`)
* Identifying unique strings (`sort | uniq -u`)
* Decoding text and uncompressing data formats (`base64 -d`, `tr 'A-Za-z' 'N-ZA-Mn-za-m'`, `xxd -r`, `tar`, `gzip`, `bzip2`)
* Inspecting listening ports and SSL connections (`nc`, `openssl s_client`, `ssh`)

---

## Directory Contents

* [`levels.md`](./levels.md) — Detailed level-by-level walkthrough documenting problems, commands, reasoning, results, and learnings.
* `evidence/` — Challenge completion evidence and terminal outputs.
