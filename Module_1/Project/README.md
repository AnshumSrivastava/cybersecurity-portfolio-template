# Module 1 · Home/Lab Network Security Audit

This is a complete, safe training project. It deliberately separates the finished submission from source data and instructions so that learners can understand what is evidence, what is process, and what is final reporting.

## Folder map

| Folder | Purpose | Start here when… |
|---|---|---|
| [completed-project/](completed-project/) | The finished, populated submission: report, scope, topology, inventory, risk/remediation, retest, and handoff. | You want to review or submit the complete project. |
| [data/](data/) | Sanitized Nmap-format output, capture summaries, completed observations, and a public-PCAP analysis. | You need to inspect the supporting data. |
| [instructions/](instructions/) | Scope/method guidance, scan plan, Wireshark guide, provenance rules, report template, and sources. | You are performing the project in your own authorized lab. |
| [tools/](tools/) | Local-only report generator. | You want to reproduce the generated evidence summary. |

## Recommended paths

**Review the completed project:** open [completed-project/final-report.md](completed-project/final-report.md), then review its linked evidence and handoff documents.

**Perform the project yourself:** read [instructions/operations-guide.md](instructions/operations-guide.md), complete a copy of [completed-project/scope.md](completed-project/scope.md), and use only your own authorized lab or an instructor-provided capture.

**Reproduce the included evidence summary:**

```bash
cd Module_1/Project
python3 tools/build_baseline_report.py
```

This command reads only `data/` files and rewrites `completed-project/generated-baseline.md`; it performs no network activity.

## Safety boundary

Do not scan public hosts, shared networks, neighbors’ devices, campus infrastructure, or any target outside written authorization. Do not commit raw captures, credentials, cookies, private addresses, personal data, or real device names.
