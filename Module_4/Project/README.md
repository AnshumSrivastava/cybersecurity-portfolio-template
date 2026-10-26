# Project 4 · Vulnerability Assessment and Remediation Roadmap

## Scenario and goal
Act as an assessment team for a small, isolated training network. Produce an evidence-based inventory of potential vulnerabilities and a prioritized remediation plan for technical owners and managers. The project is a vulnerability assessment, not an exploitation contest.

## Scope and safety
Use only an instructor-provided VM/network or assets you own with written permission. Complete `scope.md` before any scan. Record exact targets, exclusions, scan window/rate, allowed checks, credential handling, data retention, and stop conditions. Keep the environment isolated. Do not exploit findings, run disruptive checks, scan public systems, or submit malware.

## Workflow
1. Inventory assets, owners, business roles, exposed services, and criticality.
2. Run one approved authenticated scan and save its full output only in the protected lab.
3. Create a sanitized summary using `evidence/sample-scan-results.csv` as an exercise dataset.
4. Validate representative results non-destructively with host package/configuration facts and vendor advisories. A scanner result is a lead, not proof.
5. Match applicable software issues to current CVE/vendor records. Record CVSS version/vector and source date. Add asset context and threat information to local priority.
6. Build `roadmap.md` with accountable owner, due date, dependency, temporary control, and objective retest.
7. Present a management summary and technical appendix, including false positives and coverage gaps.

## Exercise dataset
`evidence/sample-scan-results.csv` is synthetic. LAB-01 through LAB-04 are exercise identifiers, not real CVEs. Use it to practice validation, prioritization, and communicating uncertainty; do not treat the example claims as facts about real systems.

## Deliverables
- Approved scope and sanitized inventory
- Scan policy, tool/version/feed date, target list, and authentication coverage
- Five triaged records (the synthetic set may be extended), including one unconfirmed/false-positive result
- Prioritized remediation roadmap and retest evidence
- Two-page management summary and technical appendix

## Assessment · 100 points
Scope/safety 20 · coverage/reproducibility 20 · validation 20 · risk priority 20 · remediation/retest 15 · communication 5.

## References
[Greenbone documentation](https://greenbone.github.io/docs/latest/) · [NIST NVD](https://nvd.nist.gov/vuln/search) · [FIRST CVSS v4.0](https://www.first.org/cvss/v4.0/) · [NIST patch-management guide](https://csrc.nist.gov/pubs/sp/800/40/r4/final).
