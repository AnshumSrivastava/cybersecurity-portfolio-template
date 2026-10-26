# Project 6 · Incident Response Tabletop and Evidence Record

## Scenario
A fictional organization reports a suspicious message, a synthetic sign-in anomaly, and renamed files on a training workstation. The team must make evidence-aware decisions, choose containment, protect recovery options, and brief leadership. This is a tabletop exercise: do not execute malware or access real accounts/systems.

## Goal
Demonstrate preparation, detection/analysis, containment, eradication, recovery, and improvement. Map selected decisions to NIST CSF 2.0 and relevant ISO/IEC 27001 themes with rationale. Do not claim certification or legal compliance based on this classroom exercise.

## Exercise sequence
1. Assign incident commander, technical lead, evidence custodian, communications lead, and business owner.
2. Read `scenario/scenario-injects.md` in order and maintain a timestamped decision log.
3. For every inject, separate confirmed facts, hypotheses, and unknowns; identify evidence needed next.
4. Choose containment actions with approver, business impact, reversibility, and evidence-preservation notes.
5. Plan eradication/recovery, including trusted backups, identity recovery, validation, monitoring, and return-to-service gates.
6. Complete `chain-of-custody.csv`, `evidence-to-claim.md`, and `decision-log.md`. Hash supplied files where applicable; a hash supports integrity since collection but does not prove origin.
7. Deliver a seven-minute leadership briefing and a technical after-action review with three measurable improvements.

## Safety and privacy
Use only the fictional packet and synthetic artifacts. Do not open suspicious attachments, make network connections to indicators, contact real people, or change real accounts/devices. Preserve originals as instructed and distinguish simulated decisions from actual operational evidence.

## Deliverables
- Decision log and incident timeline
- Evidence-to-claim register and chain-of-custody record
- Containment, eradication, recovery, communications, and notification decision plan
- NIST CSF/ISO control mapping with reasoning and gaps
- Executive briefing, after-action review, and owners/measures for improvements

## Assessment · 100 points
Lifecycle decisions 25 · evidence integrity 20 · facts vs inference 15 · containment/recovery 15 · control mapping 10 · communications/roles 10 · improvements 5.

## References
[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST CSF 2.0](https://www.nist.gov/cyberframework) · [CISA StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) · [ISO/IEC 27001:2022](https://www.iso.org/standard/27001.html).
