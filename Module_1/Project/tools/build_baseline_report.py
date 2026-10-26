#!/usr/bin/env python3
"""Build a Markdown baseline summary from sanitized project evidence; no scanning."""
from __future__ import annotations
import argparse, csv
import xml.etree.ElementTree as ET
from pathlib import Path

def ports(xml_file: Path) -> tuple[str, list[tuple[str, str, str]]]:
    root = ET.parse(xml_file).getroot(); host = root.find("host")
    name = host.find("hostnames/hostname").attrib.get("name", "unlabelled-host")
    rows=[]
    for port in host.findall("ports/port"):
        service=port.find("service"); rows.append((port.attrib["portid"], port.find("state").attrib["state"], service.attrib.get("name", "unknown")))
    return name, rows

def capture(csv_file: Path) -> list[dict[str, str]]:
    with csv_file.open(newline="") as handle: return list(csv.DictReader(handle))

def main() -> int:
    ap=argparse.ArgumentParser(description="Create a report from already-sanitized lab evidence")
    ap.add_argument("--nmap-xml", type=Path, default=Path("data/lab-web-01-nmap.xml")); ap.add_argument("--capture-csv", type=Path, default=Path("data/capture-summary.csv")); ap.add_argument("--output", type=Path, default=Path("completed-project/generated-baseline.md")); args=ap.parse_args()
    host, rows=ports(args.nmap_xml); frames=capture(args.capture_csv)
    lines=["# Generated Network Baseline Summary", "", "> Built from sanitized local evidence only; this tool performs no network activity.", "", f"## Service observation — {host}", "", "| TCP port | State | Service |", "|---:|---|---|"]
    lines += [f"| {p} | {state} | {service} |" for p,state,service in rows]
    lines += ["", "## Capture observation", "", "| Time (UTC) | Flow | Protocol | Observation |", "|---|---|---|---|"]
    lines += [f"| {r['time_utc']} | {r['source']} → {r['destination']} | {r['protocol']} | {r['observation']} |" for r in frames]
    lines += ["", "## Analyst prompts", "", "- Confirm that the HTTP listener is redirect-only and contains no session-bearing content.", "- Confirm the intended exposure and source-zone policy for HTTPS.", "- Validate TLS policy and certificate separately; ClientHello/ServerHello alone is insufficient."]
    args.output.write_text("\n".join(lines)+"\n"); print(f"Wrote {args.output}"); return 0
if __name__ == "__main__": raise SystemExit(main())
