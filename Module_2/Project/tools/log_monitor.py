#!/usr/bin/env python3
"""Summarize auth.log-style events from a supplied file without modifying it."""
from __future__ import annotations
import argparse, collections, json, re
from pathlib import Path
FAIL=re.compile(r"Failed password (?:.*? )?for (?:invalid user )?(?P<user>[\w.-]+) from (?P<ip>[\d.a-fA-F:]+)"); SUCCESS=re.compile(r"Accepted \w+ for (?P<user>[\w.-]+) from (?P<ip>[\d.a-fA-F:]+)")
def main() -> int:
    p=argparse.ArgumentParser(description="Read-only authentication-log triage"); p.add_argument("--log",required=True,type=Path); p.add_argument("--threshold",type=int,default=5); p.add_argument("--format",choices=("markdown","json"),default="markdown"); args=p.parse_args()
    failures=collections.Counter(); success_after_fail=[]; lines=args.log.read_text(errors="replace").splitlines()
    for number,line in enumerate(lines,1):
        if m:=FAIL.search(line): failures[(m["user"],m["ip"])]+=1
        if m:=SUCCESS.search(line):
            key=(m["user"],m["ip"])
            if failures[key]: success_after_fail.append({"line":number,"user":m["user"],"source":m["ip"],"prior_failures":failures[key]})
    alerts=[{"user":u,"source":ip,"failures":n} for (u,ip),n in failures.items() if n>=args.threshold]; data={"source":str(args.log),"lines_read":len(lines),"threshold":args.threshold,"repeated_failures":alerts,"success_after_failures":success_after_fail}
    if args.format=="json": print(json.dumps(data,indent=2)); return 0
    print("# Authentication log triage\n\n| Signal | Count | Review action |\n|---|---:|---|\n| Repeated failure sources | %d | Confirm account/source context; do not assume compromise. |\n| Success after earlier failure | %d | Validate user, source, MFA/session evidence. |"%(len(alerts),len(success_after_fail)))
    for x in alerts: print(f"\n- REVIEW: `{x['user']}` from `{x['source']}` had {x['failures']} failures.")
    return 0
if __name__ == "__main__": raise SystemExit(main())
