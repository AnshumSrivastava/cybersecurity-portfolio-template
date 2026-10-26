# Public Report Examples and Learning References

These links are for report structure and learning only. Do not copy claims, credentials, screenshots, or exploit steps into a submission; verify any finding independently in an authorized lab.

| Resource | Why it is useful | Notes |
|---|---|---|
| [OWASP Penetration Test Reporting Standard (OPTRS)](https://github.com/OWASP/www-project-penetration-test-reporting-standard) | OWASP-maintained, machine-readable report structure and schema; its repository links a sample report. | Best reference for a structured data/reporting model. |
| [Sample web pentest report — Ryan-Sapone](https://github.com/Ryan-Sapone/Web-Pentest-Report) | Public PDF sample of a web-app report from a training capstone. | Contains course spoilers; read only if that is acceptable. |
| [Juice Shop local-lab report — ssung099](https://github.com/ssung099/web-app-pentest-report) | Example of executive summary, scope, methodology, finding tables, evidence links, and remediation in Markdown. | Public third-party work; validate its CVSS/finding claims rather than adopting them. |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) | Authorized interactive labs and current topic learning paths. | Use its labs rather than public sites for practice. |
| [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) | Methodology reference for test coverage and terminology. | Select only tests within the engagement rules. |

## How to learn from an example responsibly

1. Compare the example’s table of contents against `REPORT-FORMAT.md`; borrow structure, not text.
2. Rebuild the executive summary from your own scope, findings, and limitations.
3. Keep only minimal, redacted evidence. Examples may include unsafe detail that a client-facing report does not need.
4. Recalculate risk for the target environment and state the CVSS version/vector and local business rationale.
5. Test only your local deliberately vulnerable application or written-authorized target.
