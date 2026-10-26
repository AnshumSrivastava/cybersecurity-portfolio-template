# Authorized web assessment test plan

Lab target:  
Authorization reference / window:  
Accounts: `student_a`, `student_b` (replace only with supplied lab accounts)

| OWASP area | Safe black-box question | Minimal evidence | Status / notes |
|---|---|---|---|
| Broken access control | Does changing an object reference expose another lab account's object? | One sanitized request/response pair; stop at first confirmation | |
| Injection | Does harmless malformed input change server-side behavior unexpectedly? | Request, expected vs actual response, no data extraction | |
| Authentication failures | Are login/session controls consistent with lab policy? | Normal workflow and one permitted negative test | |
| Security misconfiguration | Do errors/headers expose unnecessary configuration detail? | Sanitized response headers/error page | |
| Vulnerable components | Does the lab disclose an intentionally outdated component? | Version/notice only; do not exploit | |
| Logging/monitoring | Does the lab surface a relevant audit event where available? | Event indicator or documented limitation | |

## Stop conditions

Stop immediately on unanticipated real data, instability, rate limiting, a request outside the approved route list, or uncertainty about authorization. Record the event and notify the instructor; do not continue browsing the data.
