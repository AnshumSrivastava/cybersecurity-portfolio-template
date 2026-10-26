# Web Application Penetration Test Report Format

> Use only for a deliberately vulnerable application or a target covered by written authorization. This is a reporting format, not a permission to test.

## 0. Document control

| Field | Value |
|---|---|
| Client / lab owner | |
| Target and environment | |
| Assessment type | Black-box / gray-box / white-box |
| Assessment window | |
| Report version / classification | |
| Author / reviewer | |
| Written authorization reference | |

## 1. Executive summary (non-technical)

State why the assessment occurred, the exact assessed application, overall risk, the three most important outcomes, and the first remediation actions. Do not use unexplained acronyms, raw URLs containing secrets, or proof-of-concept payloads. Keep this section to one page.

**Fill-in pattern:** “Testing of `[target]` during `[window]` identified `[number]` confirmed findings: `[highest-priority themes]`. The immediate priority is `[action]` because `[business impact]`. Testing did not assess `[key exclusions]`.”

## 2. Scope and rules of engagement

| Area | Record |
|---|---|
| In-scope URLs/features/APIs | |
| Test accounts and roles | |
| Permitted methods and request limits | |
| Out-of-scope assets/actions | |
| Data handling / retention | |
| Stop conditions and escalation contact | |

Attach the signed/approved scope record; never assume a public site, parent domain, or IP range is included.

## 3. Methodology and limitations

Describe the approach in enough detail that an owner understands coverage without turning the report into an attack guide: application mapping, normal-user workflow review, authentication/session review, authorization checks with supplied lab accounts, input handling, configuration/error behavior, evidence collection, and risk rating. Name tool versions and dates. Explicitly list categories, paths, user roles, APIs, source code, infrastructure, or time windows that were not assessed.

## 4. Findings overview

| ID | Title | OWASP/CWE mapping | Affected component | Severity | Confidence | Owner | Status |
|---|---|---|---|---|---|---|---|
| F-01 | | | | Critical / High / Medium / Low / Info | High / Medium / Low | | Open / Accepted / Fixed / Retest |

Risk needs two dimensions: a reproducible technical score (for example, a clearly stated CVSS version/vector) and the environment-specific business decision. State both where they differ.

## 5. Detailed finding format — copy once per issue

### F-XX · Short, consequence-oriented title

| Field | Record |
|---|---|
| Severity / confidence | |
| CVSS version, vector, score, and source/calculator date | |
| OWASP category / CWE (if applicable) | |
| Affected URL, feature, role, version | |
| Evidence IDs | |
| Finding status | Confirmed / unconfirmed / accepted risk / retest passed |

**Description.** What security property failed, in plain language? Separate direct observations from inference.

**Expected vs actual behavior.** Write the authorization/validation/security expectation first, then the observed lab behavior.

**Minimal safe reproduction.** State preconditions, a high-level sequence, and what result confirmed the issue. Reference redacted evidence. Do not include reusable secrets, other users’ data, destructive instructions, or payloads that are unnecessary for the owner to reproduce in their controlled test environment.

**Impact and likelihood.** Explain the affected data/action, prerequisites, user interaction, scope boundaries, and what was not demonstrated. Avoid claiming full compromise from a narrow observation.

**Root cause (confirmed or suspected).** Identify the implementation/control gap and label any assumption.

**Remediation.** Provide one primary fix, defense-in-depth option, accountable owner, and implementation caveat.

**Retest.** Define the specific safe test that must pass after remediation, expected result, and evidence to retain.

## 6. Remediation roadmap

| Priority | Action | Finding(s) | Owner | Dependency / change risk | Due date | Retest evidence |
|---:|---|---|---|---|---|---|
| 1 | | | | | | |

## 7. Conclusion, limitations, and appendix

Restate residual risk after planned fixes. Include an evidence index (ID, collection time, source, redaction), tool list/versions, a test coverage matrix, risk-rating rationale, and a change/retest log. Keep raw proxy histories, tokens, credentials, and sensitive payloads out of the final report.
