#!/usr/bin/env python3
"""Small read-only CIS-style baseline checker for an authorized Linux host."""
from __future__ import annotations
import argparse, json, shutil, stat, subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

@dataclass
class Result:
    id: str; title: str; status: str; evidence: str; remediation: str

def read_text(root: Path, name: str) -> str | None:
    try: return (root / name.lstrip("/")).read_text(errors="replace")
    except (OSError, PermissionError): return None

def mode_check(root: Path, name: str, maximum: int, control: str, title: str) -> Result:
    try:
        actual = stat.S_IMODE((root / name.lstrip("/")).stat().st_mode)
        status = "PASS" if actual <= maximum else "FAIL"
        evidence = f"{name} mode is {actual:04o}; expected no more permissive than {maximum:04o}."
    except FileNotFoundError: status, evidence = "NOT ASSESSED", f"{name} was not present in the assessed root."
    except PermissionError: status, evidence = "NOT ASSESSED", f"No permission to inspect {name}."
    return Result(control, title, status, evidence, f"Set ownership and permissions for {name} according to the approved OS baseline.")

def ssh_check(root: Path) -> list[Result]:
    text = read_text(root, "/etc/ssh/sshd_config")
    if text is None: return [Result("SSH-01", "SSH daemon policy", "NOT ASSESSED", "sshd_config unavailable.", "Confirm whether OpenSSH server is installed and inspect its effective configuration.")]
    settings = {}
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if line and len(line.split(None, 1)) == 2:
            key, value = line.split(None, 1); settings[key.lower()] = value.lower()
    checks = [("SSH-01", "PermitRootLogin", "no", "Disable direct SSH root login."), ("SSH-02", "PasswordAuthentication", "no", "Use managed key-based authentication where compatible.")]
    return [Result(cid, key, "PASS" if settings.get(key.lower()) == expected else ("REVIEW" if key.lower() not in settings else "FAIL"), f"Configured value: {settings.get(key.lower(), 'not explicitly set')}; expected {expected}.", fix) for cid,key,expected,fix in checks]

def command_result(command: list[str]) -> tuple[int | None, str]:
    if not shutil.which(command[0]): return None, f"{command[0]} not installed"
    try:
        p = subprocess.run(command, text=True, capture_output=True, timeout=8, check=False)
        return p.returncode, (p.stdout + p.stderr).strip()[:300]
    except (OSError, subprocess.TimeoutExpired) as exc: return None, str(exc)

def live_checks(root: Path) -> list[Result]:
    if root != Path("/"): return [Result("HOST-01", "Live service checks", "NOT ASSESSED", "Skipped for staged root.", "Run on the authorized live host for service state checks.")]
    rc, out = command_result(["systemctl", "is-active", "auditd"]); rc2, out2 = command_result(["systemctl", "is-active", "ufw"])
    return [Result("HOST-01", "Audit logging service", "PASS" if rc == 0 else ("NOT ASSESSED" if rc is None else "FAIL"), out or "No output.", "Enable and monitor the platform audit service if required by the approved baseline."), Result("HOST-02", "Host firewall service", "PASS" if rc2 == 0 else ("REVIEW" if rc2 is not None else "NOT ASSESSED"), out2 or "No output.", "Verify an active host firewall or equivalent platform control; permit only documented services.")]

def collect(root: Path) -> list[Result]:
    results=[mode_check(root,"/etc/passwd",0o644,"FS-01","/etc/passwd permissions"), mode_check(root,"/etc/shadow",0o640,"FS-02","/etc/shadow permissions")]+ssh_check(root)+live_checks(root)
    login_defs=read_text(root,"/etc/login.defs")
    evidence=next((x for x in login_defs.splitlines() if x.strip().startswith("PASS_MAX_DAYS")), "not configured") if login_defs else "login.defs unavailable."
    results.append(Result("AUTH-01","Password aging policy","REVIEW" if login_defs else "NOT ASSESSED",evidence.strip(),"Confirm password-aging policy and approved account exceptions.")); return results

def markdown(results: list[Result], root: Path) -> str:
    now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines=["# Linux baseline review","",f"Generated: {now}",f"Assessed root: `{root}`","","> Read-only educational subset; validate against your OS/version and approved CIS profile.","","| ID | Check | Status | Evidence | Remediation |","|---|---|---|---|---|"]
    lines += [f"| {r.id} | {r.title} | **{r.status}** | {r.evidence.replace('|','/')} | {r.remediation} |" for r in results]
    return "\n".join(lines)+"\n\n## Review notes\n`FAIL` indicates a direct mismatch in this small check. `REVIEW` needs context; `NOT ASSESSED` is not a pass. Record approved exceptions and retest after any change.\n"

def main() -> int:
    p=argparse.ArgumentParser(description="Read-only CIS-style Linux baseline checker"); p.add_argument("--root",default="/"); p.add_argument("--output"); p.add_argument("--format",choices=("markdown","json"),default="markdown"); args=p.parse_args()
    root=Path(args.root).resolve(); results=collect(root); output=markdown(results,root) if args.format=="markdown" else json.dumps([asdict(x) for x in results],indent=2)+"\n"
    if args.output: Path(args.output).parent.mkdir(parents=True,exist_ok=True); Path(args.output).write_text(output)
    else: print(output,end="")
    return 0
if __name__ == "__main__": raise SystemExit(main())
