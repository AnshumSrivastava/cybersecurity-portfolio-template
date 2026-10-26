# Network Audit Operations Guide

## Repeatable workflow

1. Obtain written approval and complete `../completed-project/scope.md`; do not substitute a real IP in the example evidence.
2. Update `../completed-project/inventory.csv` using safe lab labels and redraw `../completed-project/topology.mmd` when the topology changes.
3. Record the exact scan command, version, window, target, and output in `scan-plan.md`. Run only what the owner approved.
4. Open an instructor-provided PCAP or self-generated test capture in Wireshark. Apply the filters in `../data/wireshark-notes.md`; record direct observations before interpretation.
5. Save only sanitized derived evidence in `../data/`. Do not commit PCAPs, cookies, credentials, personal identifiers, or raw device names.
6. From the project root, run `python3 tools/build_baseline_report.py` to regenerate `../completed-project/generated-baseline.md`, then update `../completed-project/final-report.md` with validated conclusions.
7. Give the owner the recommendations, owner, due date, change dependencies, and retest method. Never apply a router/firewall change during the assessment unless separately approved.

## Evidence quality checks

Every claim needs an evidence ID, timestamp/window, source, direct observation, confidence, and limitation. A scanner label is not a vulnerability; a packet is not proof of user intent. Mark unknowns explicitly.
