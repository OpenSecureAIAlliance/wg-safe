# Shared AI Findings Exchange (SAFE)

Version: 1.0
Date: October 21, 2026
Chairs (interim): Paul DiOrio (NVIDIA), Josh Boyer (Red Hat)

*An independent incident-learning and assurance initiative of the Open Secure AI Alliance's SAFE working group.*

---

## Mission

Cyberattacks will happen. AI systems will make mistakes. Safeguards and operating assumptions will sometimes fail. A responsible AI ecosystem is measured by how quickly it contains harm, establishes the facts, informs those at risk and turns each incident into stronger protection for the community.

SAFE confidentially collects and analyzes AI incidents and near misses, promptly informs affected parties and turns recurring failures into shared, evidence-based controls that reduce systemic risk.

---

## Scope and Membership

SAFE encourages participation from representatives of the following groups worldwide:

- Proprietary model creators, open-weight model creators and organizations focused on fine-tuning, quantization and other model development activities
- Academic institutions, research labs, and independent researchers working on AI security and safety
- AI deployers and enterprise customers
- Evaluation, hosting, cloud and tool providers
- Critical-infrastructure operators
- Civil-society and affected-user representatives
- Government and standards bodies as non-controlling observers

As an established Open Secure AI Alliance working group, SAFE follows the Alliance's established governance structures for membership, leadership rules and decision authority.

SAFE operates independently so that no vendor or industry segment controls its findings. Its processes apply equally to open and closed AI systems. Open systems are not automatically safe, and closed systems are not safe by declaration. Trust is not a control; shared evidence and verifiable improvement are how trust is earned.

Participation in SAFE is a commitment to this compact. Open Secure AI Alliance membership alone does not impose it. No member or funding source may control publication timing or remediation conclusions. Parties involved may supply evidence and correct factual errors without absolute control of the conclusions. Multilateral and regional public-interest institutions may contribute in a non-controlling role. Participation alone grants neither a veto nor access to identifiable confidential reports.

SAFE members, participants, reviewers, leaders and staff agree to disclose relevant significant conflicts of interest that could materially call their impartiality into question before participating in an incident review. Any conflicted individual or organization is responsible for recusing themselves where appropriate. SAFE will document conflict disclosures, recusals and replacement decision-makers while protecting confidential information. Disputed decisions may be appealed for independent review by initiating a request to the SAFE Chair and Co-Chair or to the Open Secure AI Alliance Steering Committee.

---

## Guiding Principles

**Commitment to responsible operation.** AI safety and security are the binding principles underlying all aspects of SAFE membership activities.

**Openness with accountability.** Transparent disclosure processes strengthen collective defense, subject to Coordinated Vulnerability Disclosure (CVD) best practices.

**Open learning.** Reviews focus on technical and systemic causes and are not intended to address blame.

**Risk-based response.** Reporting, disclosure and escalation should reflect actual risk.

**Member sovereignty.** SAFE establishes minimum interoperability and assurance practices without superseding members' internal security policies or legal obligations.

**Learning is separate from enforcement.** Confidential review should encourage candid reporting, while regulators and affected parties retain their legal rights. Members should provide a confidential internal reporting route independent of the immediate management chain, with a clear escalation owner and protection against retaliation for good-faith reporting.

---

## Definitions

**An AI incident** is an event in which an AI system causes or materially contributes to an outcome covered by the Reporting Compact.

**A near-miss AI incident** is an event with a credible path to a reportable outcome that is prevented before the outcome occurs, especially when one or more controls fail but a backup control prevents harm. Routine blocked attempts without a material control failure or credible consequential risk may be optionally aggregated to help share insights.

**Approved scope** is the authorization given by an accountable principal, including permitted actions, targets, resources, purpose, time limits and delegation limits. Approved scope must respect the resource owner's authorization. A task request or the AI system's interpretation cannot expand it.

The terms **agent sandbox** and **secure runtime** refer to isolated environments where an AI agent runs code and uses tools, with limits on the files, processes and network resources it can access. These environments govern permissions, credentials, network access, and record activity for audit. Overall, their purpose is to enforce security controls while an agent operates.

**Impact** means an observed consequence for people, organizations, systems or the environment.

**Systemic risk** means risk arising from shared dependencies or recurring failures across systems or organizations.

**Confidential or sensitive information** will follow the Traffic Light Protocol (TLP) 2.0 (as standardized by FIRST: https://www.first.org/tlp/) to facilitate sharing boundary labels. Ultimately, SAFE's aim is for investigations to progress into finalized findings and reports that are widely shareable (i.e., TLP:Green and TLP:Clear). However, SAFE allows processes for restricted intermediate work and reporting as necessary (i.e., TLP:Red and TLP:Amber).

---

## Reporting Compact

As a condition of membership, members agree to report an incident when they become aware or reasonably suspect that an AI system they operate:

- Accesses, exploits, disrupts, misuses or modifies a third-party system without authorization.
- Causes third-party impact by escaping or bypassing a secure runtime, sandbox, or safety system across network, file artifact, identity, policy or tool boundaries.
- Accesses third-party confidential information, for example, by accessing data or redistributing it for others to access, without policies, capabilities and permissions approved to operate on behalf of a user.
- Continues to probe, access, exploit or modify a production target after the operator knows or reasonably suspects, based on direct discovery or third-party notification, that the activity is unauthorized or outside the approved scope.
- Causes or materially contributes to consequential harm, or a credible near miss, to people, the operating organization, property or the environment, including through a failure to act when action was required. This includes embodied AI and physical control systems.

In the spirit of the compact, members may also report an incident or near miss that does not involve a third-party system and is isolated to their own systems.

Intent does not determine whether an event is reportable. Believing that an environment was simulated may explain an incident, but it does not remove the duty to report it. Minimizing transparency of events slows learning. Reporting applies when an AI system causes another system to act outside the originating authorization, when a sequence of actions exceeds that authorization, or when an AI system's failure to act despite being capable of doing so results in harm. Unauthorized changes to the artifacts that define an agent's permissions, safeguards or scope are boundary failures. Material attempts stopped by another control should be assessed as near misses.

Members report incidents involving systems they operate, including infrastructure incidents that materially contribute to a reportable AI outcome. A deployer, host, model provider or tool provider reports what it knows and identifies the other responsible parties. A coordinating reporter will be designated where possible to link reports about the same incident. Coordination does not remove each member's duty to give prompt notice or provide evidence it controls. A provider need not produce records it does not possess but should state the resulting gap.

---

## Notification Timelines

| Deadline | Required action |
|---|---|
| Immediate action | Notify the directly affected organization. |
| 72 hours | Notify customers with credible exposure. |
| 4 business days | Submit a confidential preliminary SAFE incident report. |
| 14 days | Issue a broader customer advisory when warranted. |
| 30 days | Publish a preliminary factual report, subject to security, legal and investigative constraints. |
| 90 days | Publish remediation status. |
| Weekly updates | Provide machine-readable updates while material risks remain unresolved. |

The deadlines run from when the member becomes aware of facts giving reasonable grounds to suspect a reportable event. Record operator awareness, any earlier affected-party awareness, receipt of external reports, and the basis for each timestamp. Notify directly affected parties as soon as practicable; send available facts first and correct or expand them as evidence develops. Record the notification channel, delivery result and follow-up attempts. The preliminary SAFE report may be incomplete if evidence gaps and the plan to close them are stated.

SAFE reporting complements applicable legal, contractual and coordinated-disclosure duties; it does not replace or extend their deadlines. Reuse relevant existing reports where lawful, adding the SAFE-specific information that is missing. Record affected jurisdictions and any applicable external reporting duty, responsible party, deadline and filing status. Document any necessary restriction on public disclosure, its reason, decision owner and next review date. Maintain prompt, lawful notice and actionable guidance to affected parties. Confidentiality labels (i.e., TLP designations) do not override public-records laws or other lawful disclosure duties.

SAFE can accept reports from affected people and organizations whether or not they are existing members. The working group will acknowledge receipt and route them promptly for intake assessment. Members should maintain a monitored incident contact and use established security contacts or an appropriate response coordinator when a recipient cannot be reached.

SAFE submissions should use a versioned machine-readable minimum record where available; otherwise provide equivalent information in a structured narrative. Include a reporting contact, affected systems and observed versions, incident class, near-miss status, awareness and response timeline, current containment, evidence availability and next update. Identify affected people or groups, impact severity, scale, duration, reversibility and known disproportionate effects.

---

## Intake Assessment

SAFE assesses each submission before it enters review, so that every report receives a recorded decision and a stated reason. The same assessment applies to member and nonmember submissions. It is kept with the report under the report's confidentiality label.

The intake assessment records:

- **What happened:** the observed behavior, the affected systems and when the behavior was observed, with the source of each timestamp.
- **Evidence:** the records that tie the behavior to a specific AI system, each identified as a self-reported claim or an external observation. When the reporter does not hold the system's records, record which party holds them. An affected person is not expected to hold the operator's logs.
- **Approved scope:** the approved scope in force at the time, who granted it and where it is recorded, or that it is not yet known.
- **Reproducibility:** whether the behavior can be repeated and under what conditions, or why it cannot. Reproducibility informs the review; it is not a condition of acceptance.
- **Decision:** one of the outcomes below, with the reason, the decision owner and the date.

| Outcome | Applies when |
|---|---|
| Accept as an AI incident | The submission describes an AI incident as defined above, and the available evidence supports it. |
| Accept as a near-miss AI incident | The submission describes a near-miss AI incident as defined above, and the available evidence supports it. |
| Record for aggregation | The event is a routine blocked attempt without a material control failure or credible consequential risk. |
| Request more evidence | The submission may be in scope, but the available evidence does not yet support a decision. Record what is missing, who holds it and when the decision will be revisited. |
| Close as out of scope | The event is neither an AI incident nor a near-miss AI incident as defined above, for example when the reporter's own configuration explains the behavior and no covered outcome occurred. |

Approved scope often decides between these outcomes. Without a record of the scope in force, an AI system that exceeded its authorization cannot be told apart from one that did what it was configured to do. Intake records what is known about the scope; the review determines whether it was exceeded.

Missing evidence alone does not close a submission, and intent or a belief that the environment was simulated does not decide the outcome. A closed submission is reopened when new evidence brings it within scope. SAFE tells the reporter the outcome and the reason, subject to confidentiality constraints. Conflict-of-interest disclosure and recusal apply to intake decisions as they do to reviews, and intake decisions may be appealed in the same way.

The intake assessment decides whether SAFE reviews a submission. It does not change a member's reporting or notification duties, which run from awareness as set out above.

---

## Evidence Preservation

Assign evidence items stable identifiers and record collection time, source, actor or workload, relevant system and links to related events. Preserve original records and document custody, access, transfers, transformations, retention and integrity checks. Distinguish self-reported claims from external observations. State when evidence was not collected, is unavailable, is lawfully withheld or is not applicable. Absence of evidence will not be treated as proof of success or failure.

Members must preserve and provide affected organizations with the evidence needed for a complete forensic response, including:

- Agent execution traces and model reasoning traces (e.g., general failure analysis, chain-of-thought traces), retaining the observed versions, identifiers and configurations.
- Records of the operating and test environments, including infrastructure, runtime and software versions, images or build definitions retained and identified by content digest, the agent's working directory at the start of the affected session (e.g., a repository with both committed and uncommitted changes), network paths, isolation boundaries, connected systems, relevant configurations, and any differences between the intended environment, the environment as described to the agent, and the environment encountered.
- Prompts (including system prompts and tool definitions), tool calls and their results as delivered to the agent (noting any truncation), logs, and third-party dependencies, including the safeguards, external tools, APIs, harnesses and serving artifacts observed.
- Permissions and credential identifiers, types, scopes and revocation status available during the run; secret values should remain protected in restricted forensic custody where preservation is necessary. Do not include reusable passwords, tokens or private keys in incident reports, alerts or advisories; use protected references and scope instead.
- Human approvals, automated monitor approvals and other intervention events while preserving the originating principal, authorization source, delegation chain and approved action scope.
- Files and external artifacts created, modified or deleted, with location, time of change and, if available, the previous state before any changes occurred.
- Detection, containment and recovery events, including any methods for reproduction testing based on remediation evidence. Separate original incident observations and preserved state from later replay, reproduction and remediation tests. Never silently substitute a new run or configuration for missing original evidence.
- For physical systems, preserve relevant sensor and actuator records, physical state, safety interlocks, operating limits and human interventions.
- For human language-dependent controls, record the languages, scripts and code-switching involved, and whether the implicated controls were evaluated for those inputs.

Members must also provide a preliminary control-failure analysis within 30 days and report near misses, not only events that produce confirmed harm.

---

## Review Framework

Examine each incident across the complete operating stack. For every applicable control layer, state the expected outcome, assessment and supporting evidence, using pass, fail, insufficient evidence or not applicable. Pass means the stated control outcome is supported; fail means it is contradicted. Missing, inaccessible or inconclusive evidence is insufficient evidence, with the reason recorded. These labels describe a specific assessment but do not indicate general system safety or legal compliance.

| Control layer | Review Criteria |
|---|---|
| Model | Model recognition of uncertainty, scope boundaries and stop conditions. |
| Instructions | Authorization and environmental assumptions were explicit and correct. |
| Safeguards | Classifiers, policies, approvals, action limits and trust-boundary checks were operating as intended, including for the human languages, scripts and usage conditions involved. |
| Tools | Credentials, permissions, spending, publishing and execution were appropriately constrained. |
| Environment | Network paths, isolation, targets and data boundaries were independently verified. |
| Monitoring | Operators detected and interrupted unexpected behavior in real time. |
| Human operations | Responsibilities, escalation paths and stop procedures were clear, and people had an opportunity to understand, contest or recover from the outcome. |
| Supply chain | A partner or third-party dependency (cloud, evaluation, data or tooling provider) upheld assumed controls. |
| Serving path | The invoked model, runtime, gateway, cache, proxy and wrapper matched configurations and produced expected results. |
| Authorization and commitment | The consequential action matches valid authorization at commitment, including delegation, expiry and revocation. |
| Workflow composition | The combined sequence, shared state and interactions did not cross a trust boundary and did not exceed the originating scope. |

The affected organization may correct factual errors but should not have veto power over learnings or recommendations.

---

## Disclosure Model

**Confidential rapid alert:** Immediate indicators, containment steps and affected patterns for members and other trusted recipients.

**Member operating advisory:** De-identified analysis, implicated controls, tests and recommended actions.

**Public safety report:** Root causes, systemic lessons, recommendations and adoption metrics after sensitive details are removed.

Share evidence securely and only as needed, considering legal duties, privacy and security risks. Remove unnecessary sensitive data, protect reusable secrets, document redactions and, if necessary, clearly state sharing restrictions according to the Traffic Light Protocol (TLP) 2.0 with identification of the intended community. Restrict only information needed to address a documented material risk to people, systems, reporter confidentiality, legal rights or an active investigation. Embarrassment, reputational harm or commercial disadvantage alone does not justify withholding. Regardless of TLP determination, provide directly affected parties the evidence and guidance they can lawfully receive to investigate and protect their systems.

SAFE participation is voluntary. Members undertake the reporting duties in this compact. SAFE encourages early internal escalation and candid reporting of honest mistakes, permits confidential nonmember reports, and protects reporters from retaliation through its own rules. Confidential learning does not create legal privilege or immunity, prevent lawful disclosure or displace the rights of affected parties and authorities. Intentional abuse, fraud or criminal conduct is not included in SAFE's non-punitive treatment within its own rules.

---

## From Lessons to Controls

Every incident review should produce shared defensive recommendations that AI providers, deployers, evaluators and customers can implement and verify. Each recommendation should specify:

- The failure and affected systems
- The required defensive outcome
- The minimum control and acceptable alternatives
- A reproducible verification method stating its subject, scope, assumptions, evidence path, failure behavior, known systematic error classes and measurement uncertainty
- The evidence to retain, responsible owner and implementation deadline
- Adoption, effectiveness and review metrics
- The distinctions among an observed event, a reported claim, a structural finding, a control recommendation and a verified test result (stating the evidence and limitations for each)

When safe and lawful, SAFE will publish reusable tests, machine-readable policies, detection rules, reference configurations and incident response guidance in a shared, versioned catalog including preservation of any corrections, disputes, withdrawals and supersession. Links to confidential evidence or reports will remain under access control. The catalog will use established identifiers, data schema conventions, open taxonomies and exchange formats where they fit, documenting their versions and extensions. SAFE records should remain portable and vendor independent.

Where feasible, detection rules will be published in open, operational, vendor-neutral formats. Rules should include their intended inputs, dependencies, version, positive and negative test examples, known false positives and false negatives, and a repeatable test procedure. For unintended access to real systems, recommendations might include default-deny network egress, explicit target allowlists, signed evaluation manifests, independent preflight isolation checks, real-time action monitoring, automatic stops when scope is uncertain and equivalent assurance requirements for evaluation partners.

---

## The Compact

Report honest mistakes and close calls early so the community can prevent the next incident.
