# MyAnatomy Cybersecurity Portfolio Guide

This repository contains course modules, class notes, project kits, and learner side-project spaces. It is designed so a reviewer can quickly distinguish a completed project submission from its supporting data, instructions, and automation.

## Start here

| Need | Go to |
|---|---|
| Course landing page | [index.html](index.html) |
| Module 1 complete network audit | [Module_1/Project/README.md](Module_1/Project/README.md) |
| Module 2 complete hardening toolkit | [Module_2/Project/README.md](Module_2/Project/README.md) |
| Module 3 report format and public examples | [Module_3/Project/README.md](Module_3/Project/README.md) |
| Later modules | [Module 4](Module_4/README.md) · [Module 5](Module_5/README.md) · [Module 6](Module_6/README.md) |

## Repository layout

Each module generally contains:

| Folder | Meaning |
|---|---|
| `Class_Notes/` | HTML lesson/revision materials. |
| `Project/` | The module’s guided project and associated artifacts. |
| `Side_Project/` | Space for independent learner work. |

The completed projects in Modules 1 and 2 use a consistent internal structure:

| Project folder | Contents | Intended audience |
|---|---|---|
| `completed-project/` | Finished report/submission, scope, remediation/retest and owner-handoff artifacts. | Assessor, reviewer, owner |
| `data/` | Sanitized fixtures, evidence, and derived observations. | Analyst / reviewer |
| `instructions/` | Method, safety rules, templates, runbooks, and references. | Learner / analyst |
| `tools/` | Local scripts and tests that reproduce reports from the supplied data. | Learner / maintainer |

## Module 1 — Home/Lab Network Security Audit

The Module 1 project is a completed, evidence-based network baseline using documentation-only addresses and synthetic/sanitized evidence.

- Read the [finished report](Module_1/Project/completed-project/final-report.md).
- Review the [evidence/data guide](Module_1/Project/data/README.md).
- Follow the [operations guide](Module_1/Project/instructions/operations-guide.md) only in an authorized lab.
- Rebuild the local evidence summary:

```bash
cd Module_1/Project
python3 tools/build_baseline_report.py
```

The command reads local data only. It does not invoke Nmap, Wireshark, or make network connections.

## Module 2 — Automated Log Monitoring & Hardening Toolkit

The Module 2 project is a complete read-only Linux baseline and authentication-log triage workflow. Its supplied data is a staged Linux root and a synthetic auth log.

- Read the [finished assessment](Module_2/Project/completed-project/final-hardening-assessment.md).
- Review the [fixture guide](Module_2/Project/data/README.md).
- Read the [control catalogue and runbooks](Module_2/Project/instructions/README.md).
- Reproduce the complete safe fixture run:

```bash
cd Module_2/Project
tools/run_audit.sh --root data/lab-root --log data/auth.log \
  --output-dir completed-project/generated-evidence
python3 -m unittest discover -s tools/tests -v
```

This creates reports only from local synthetic files. It does not change configuration, restart services, install packages, or send data over the network.

## Module 3 — Web Assessment Format and Examples

Module 3 intentionally provides a reusable report format and public learning/report examples rather than an invented assessment. Begin with [REPORT-FORMAT.md](Module_3/Project/REPORT-FORMAT.md), then read [PUBLIC-EXAMPLES.md](Module_3/Project/PUBLIC-EXAMPLES.md).

Use only a deliberately vulnerable application or a target for which you have written authorization. Do not test public websites, school systems, shared infrastructure, or other people’s applications.

## Safe use and data handling

1. Obtain written authorization before any scan, capture, or test of a real system.
2. Keep target lists narrow; use low-impact, approved methods only.
3. Store raw PCAPs, full logs, tokens, passwords, cookies, and real identifiers outside this repository.
4. Commit only the minimum sanitized evidence necessary to support a claim.
5. Treat `NOT ASSESSED` as unknown—not as secure—and treat tool output as evidence to review, not a conclusion by itself.
6. Route all remediation through the owner’s normal change-management and rollback process.

## Verification status

| Project | Verification |
|---|---|
| Module 1 | Local evidence-report generator runs successfully against supplied XML/CSV data. |
| Module 2 | Bash syntax check, Python fixture tests, and combined baseline/log/manifest workflow pass. |
| Module 3 | Report format and links are documentation resources; no live assessment is performed. |
