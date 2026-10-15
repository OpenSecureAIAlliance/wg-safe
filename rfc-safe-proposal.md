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
* The technique classification of the failure against open, vendor-neutral taxonomies (for example MITRE ATLAS techniques or the OWASP LLM and agentic classes), so that recurrence of the same failure across members and time is mechanically detectable rather than editorially asserted
* The required defensive outcome
* The minimum control and acceptable alternatives
* A reproducible verification method
* The evidence to retain, responsible owner and implementation deadline
* Adoption, effectiveness and review metrics

When doing so does not expose sensitive evidence or create additional risk, SAFE will publish reusable tests, machine-readable policies, detection rules, reference configurations and incident-response guidance. SAFE will maintain these materials in a shared, versioned catalog of incident-driven defensive recommendations.

Detection rules published to the catalog should be expressed in open, executable, vendor-neutral formats rather than prose, and should carry the same discipline the recommendations themselves require: declared true-positive and true-negative test cases, measured false-positive evidence on benign traffic, a version, and the technique classification above. Open rule standards with these properties already exist at both layers of the operating stack — for example Sigma for infrastructure telemetry, and ATR (Agent Threat Rules, MIT) for the agent layer of prompts, tool calls and skill artifacts, which already carries crosswalks to ATLAS and the OWASP classes. A catalog entry that names its technique, ships its tests and states its measured error rates is a control a member can adopt and verify; one that does not is advice.

Each published test result should identify the observed rule or ruleset digest; evaluator, configuration and normalization versions; corpus identity, digest and label provenance; observation window; evaluation unit, denominator and base rate; replay or live status; monitor, shadow or enforce mode; observed or blocked outcome; a correlation reference for the observation and decision path; and overlap or union semantics when multiple rules fire. Per-case outcomes should distinguish true positive, true negative, false positive, false negative, abstention, error and timeout, while separately reporting malformed, dropped, not-reached and unusable evidence. Without this envelope, two members can test the same named rule on the same named corpus while loading different artifacts, counting different units or silently treating failures as negatives, and publish incompatible error rates that appear equivalent.

For unintended access to real systems, recommendations might include default-deny network egress, explicit target allowlists, signed evaluation manifests, independent preflight isolation checks, real-time action monitoring, automatic stops when scope is uncertain and equivalent assurance requirements for evaluation partners.

# The Compact

**Report honest mistakes and close calls early so the community can prevent the next incident.**
