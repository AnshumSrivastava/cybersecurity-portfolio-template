# Completed Submission Checklist — NETSEC-LAB-01

| Deliverable | Artifact | Completion evidence |
|---|---|---|
| Authorization / scope | `scope.md` | Approved lab labels, limited window, exclusions, and stop conditions recorded. |
| Asset and topology map | `inventory.csv`, `topology.mmd` | Four lab assets, zones, owners, and service roles identified. |
| Nmap evidence | `../instructions/scan-plan.md`, `../data/lab-web-01-nmap.xml` | Exact low-impact command, scope, version, and sanitized results recorded. |
| Wireshark analysis | `../data/wireshark-observations-completed.md`, `../data/capture-summary.csv` | DNS, TCP handshake, and TLS observations separated from inference. |
| Reproducible analysis | `tools/build_baseline_report.py` | Parses only supplied sanitized evidence; performs no network activity. |
| Security posture report | `final-report.md` | Executive summary, three observations, prioritized actions, owners, validation, and limitations. |

## Quality review

- [x] No public/campus/neighbor target is named.
- [x] No raw PCAP, credential, cookie, real device name, or personal identifier is retained.
- [x] Every technical conclusion is qualified by scope and limitation.
- [x] Recommendations name a responsible owner and a safe validation approach.
