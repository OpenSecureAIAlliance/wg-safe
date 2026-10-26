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
* The required defensive outcome
* The minimum control and acceptable alternatives
* A reproducible verification method. Reproducibility is necessary and not sufficient: a method can be deterministic, repeatable, and still silent about the control it claims to exercise. Each method should also state:
  * **Its own failure mode.** At least one way the method can return a passing or empty result without raising an error, and what the record shows when it does. A check that fails open and reports a plausible number is worse than no check, because a number now exists and someone will act on it.
  * **Its noise floor, and the population that floor was measured over.** A floor obtained by repeating an identical input measures determinism rather than discrimination. Where the reported figure is a ratio, the method should state whether the party being measured can change the denominator.
  * **The path through which the evidence was produced.** Where that path differs from the one production traffic takes, the divergence should be recorded as a limit on the claim rather than left out of the report.
  * **How much of the corpus exercised the control under test.** Zero is a permitted value and a required disclosure, because "the control behaved as specified" and "no input ever reached the control" are indistinguishable from outside.
  * **Whether the identity of what it depends on was measured or asserted.** Where a result depends on a versioned artifact, the method states whether that artifact's identity was measured or asserted. An asserted identity travels with every finding derived from it. An absent identity states which side it is absent on: not provided by the measured party, or provided, durably acknowledged by the method, and not retained. Where a result is produced by a model, the model is a versioned artifact. A model name, whether sent in the request or returned in the response, is an asserted identity. A method that claims a fixed scorer states how a change of scorer would be detected, and how soon.
  * **Whether each property it states about its own results is enforced or observed.** An enforced property names the implementation boundary that rejects the alternative and a reproducible counterexample test. An observed property names the corpus identity, method version and observation window over which it held, and must not be stated as an invariant.
* The evidence to retain, responsible owner and implementation deadline
* Adoption, effectiveness and review metrics

When doing so does not expose sensitive evidence or create additional risk, SAFE will publish reusable tests, machine-readable policies, detection rules, reference configurations and incident-response guidance. SAFE will maintain these materials in a shared, versioned catalog of incident-driven defensive recommendations.

For unintended access to real systems, recommendations might include default-deny network egress, explicit target allowlists, signed evaluation manifests, independent preflight isolation checks, real-time action monitoring, automatic stops when scope is uncertain and equivalent assurance requirements for evaluation partners.

# The Compact

**Report honest mistakes and close calls early so the community can prevent the next incident.**
