# 08 — Local Cybersecurity CTF

## Objective

Combine Linux, networking, and reconnaissance techniques into one controlled, offline challenge:

```text
Student Laptop
      │
      │
      ▼
Local Cybersecurity Server
      │
      ├── Web service
      ├── Files
      ├── Flags
      └── Challenges
```

---

## What Problem Were We Solving?
Applying multi-disciplinary cybersecurity skills (investigation, parameter analysis, source code inspection, privilege analysis) to solve controlled challenges and capture security flags.

## Challenge Rules & Architecture
* Fully self-contained local environment operating without internet dependency.
* Teams identify vulnerability vectors and capture flags conforming to the format: `FLAG{...}`.

---

## Directory Contents

* [`rules.md`](./rules.md) — Scope, rules of engagement, and scoring criteria.
* [`challenges.md`](./challenges.md) — Challenge descriptions, hints, and objectives.
* [`server/`](./server/)
  * `files/` — Local artifacts and configuration files for challenge inspection.
  * `web/` — Minimal web service challenge files.
* [`submissions/`](./submissions/) — Documented flags with command traces, evidence, and vulnerability root causes.
