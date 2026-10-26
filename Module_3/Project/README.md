# Project 3 · Web Application Security Assessment Format & Public Examples

## Objective
Use a professional, safe report format for an instructor-assigned deliberately vulnerable application, then study public examples for presentation and evidence organization. This project folder intentionally contains no fictional completed assessment or exploit record.

Start with [REPORT-FORMAT.md](REPORT-FORMAT.md), then use [PUBLIC-EXAMPLES.md](PUBLIC-EXAMPLES.md) to review public resources.

## Scope and authorization
Use OWASP Juice Shop, DVWA, or the exact TryHackMe room assigned by the instructor, in its intended lab environment. Your scope record must identify the exact lab URL/instance, allowed dates, accounts, features, and techniques. Do not test public websites, school systems, classmates’ projects, or an unassigned room. No denial-of-service, persistence, destructive changes, phishing messages, or real credentials.

## Assessment questions
- Does the server enforce object ownership and role authorization on every request?
- Does untrusted input remain data, rather than changing query or command behavior?
- Are authentication, session, configuration, and error behaviors consistent with the expected security design?

Use `test-plan.md` to map each applicable category to a safe test and outcome. Investigate three focused questions in depth, including one access-control, one input-handling, and one authentication/session or configuration question where the assigned lab supports it. Use two supplied test accounts for access-control tests. Use harmless test values and stop after the minimum evidence needed to confirm a lab finding. If another user’s data appears, stop and report it to the instructor without browsing further.

## Method
1. Complete `scope.md` and get the instructor’s approval.
2. Map one ordinary user journey and its trust boundaries.
3. Use browser inspection/proxy tools for manual testing; keep requests low volume and non-destructive.
4. Record expected behavior before testing, then actual behavior with sanitized request/response evidence.
5. Complete `finding-template.md` for each issue. State confidence, root cause, impact, recommendation, and testable retest criteria.
6. Rate severity using **CVSS v4.0** when appropriate; include the vector and explain local risk separately. A numeric score does not replace business context.
7. Produce a report and five-minute presentation. Include one confirmed issue and one suspected issue that was not confirmed, with honest limitations.

## Deliverables
- Approved scope and test plan
- Three detailed finding records, including at least one confirmed and one unconfirmed result
- Sanitized evidence index
- Report using `report-template.md`
- Remediation plan and retest criteria
- Short demo and reflection

## Assessment · 100 points
Scope and safe practice 20 · reproducibility and evidence 20 · finding accuracy and risk 25 · remediation/retest 20 · communication and reflection 15.

## Submission checklist
- [ ] Only the assigned lab and accounts were used
- [ ] Every finding names the expected and actual behavior
- [ ] Evidence is minimal and has secrets/personal data redacted
- [ ] Severity names the CVSS version/vector and local context
- [ ] Fixes are specific and retestable
- [ ] No cookies, tokens, passwords, flags, or real user data are committed

## References
[OWASP Top 10:2025](https://top10.owasp.org/2025/) · [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) · [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) · [FIRST CVSS v4.0](https://www.first.org/cvss/v4.0/).
