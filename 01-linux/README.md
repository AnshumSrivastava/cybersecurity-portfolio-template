# 01 — Linux Fundamentals

## Overview

Linux forms the backbone of servers, cloud environments, and security tooling. Operating Linux from the command line is an essential foundation for any cybersecurity practitioner, transitioning away from reliance on graphical interfaces toward precise, reproducible command-line interactions.

---

## What Problem Were We Solving?
Navigating systems, managing administrative configurations, and inspecting active machine state without graphical user interfaces. Understanding low-level filesystem structure, file permissions, and core system utilities.

## What Was Practiced
* Directory navigation & file inspection (`pwd`, `ls`, `cd`, `cat`, `less`, `head`, `tail`)
* Filesystem manipulation (`mkdir`, `touch`, `cp`, `mv`, `rm`)
* Searching & filtering data (`grep`, `find`, `sort`, `uniq`, `wc`)
* Access control & permission management (`chmod`, `chown`)
* Process monitoring & inspection (`ps`, `top`, `kill`)
* Network interface & socket status inspection (`ip`, `ss`)

## What Was Learned
* How Linux represents all devices and abstractions as files.
* How file permissions (`rwx` for owner, group, other) enforce security boundaries.
* How pipes (`|`) and stream redirection (`>`, `>>`) allow chaining small, specialized tools to build powerful investigative pipelines.

---

## Directory Contents

* [`commands.md`](./commands.md) — Comprehensive command reference documenting syntax, purpose, examples, and observations.
* [`tasks.md`](./tasks.md) — Hands-on problem-solving exercises completed via CLI.
* `evidence/` — Terminal session logs and command outputs.
