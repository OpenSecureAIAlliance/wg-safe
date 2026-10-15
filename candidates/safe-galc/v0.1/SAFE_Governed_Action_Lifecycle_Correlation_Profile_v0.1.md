# SAFE Governed-Action Lifecycle Correlation Profile

- **Candidate version:** 0.1
- **Profile identifier:** `safe-galc/0.1`
- **Date:** 2026-09-17
- **Last revised:** 2026-09-24
- **Status:** Candidate contribution draft — not adopted
- **Prepared by:** Gary Gayle, Founder and CEO, Value Intelligence Solutions Inc.
- **Related research:** R.E.T.N.A.™ Proof of Governed State / Distributed Governance R&D


## Status and contribution boundary

This document is an independent, format-neutral candidate profile for discussion in the Open Secure AI Alliance Shared AI Findings Exchange (SAFE) community. It has not been adopted, endorsed, reviewed, or approved by the Open Secure AI Alliance, the Linux Foundation, or the authors of any related SAFE proposal.

The identifier `safe-galc/0.1` is a local candidate identifier only. It is not an official SAFE namespace assignment or registry entry.

This candidate contributes an interoperability boundary and conformance model. It does not request adoption of a proprietary R.E.T.N.A. implementation and does not disclose or transfer proprietary policy-evaluation logic, decision algorithms, distributed-governance mechanisms, implementation architecture, or unpublished protocol internals.

If submitted upstream, licensing and contribution terms MUST be confirmed against the repository's applicable contribution policy before merge.

## Abstract

SAFE proposals currently address evidence preservation, temporal anchoring, independent verification, provenance, and chain of custody. Those properties are necessary but do not establish that independently valid records refer to the same governed action or state transition.

This profile defines the minimum evidence and verification behavior needed to correlate:

`proposal → governance determination → enforcement event → execution result → observed state → reconciliation result`

It allows a reviewer to determine whether:

1. a governance determination evaluated the exact proposed action;
2. an enforcement point acted under that exact determination while it remained valid;
3. the attempted or completed operation matched the authorized actor, action, target, parameters, context, and use constraints;
4. an observation referred to the resulting state of that execution rather than merely sharing a timestamp or identifier; and
5. reconciliation compared the authorized transition with the observed consequence without collapsing cryptographic integrity into external truth.

The profile keeps lifecycle correlation separate from temporal anchoring, chain of custody, component integrity, producer independence, execution correctness, and real-world grounding. Success in one property MUST NOT be treated as proof of another.

## 1. Motivation

A governance record can be correctly signed and temporally anchored. An execution record can have an intact custody chain. An observer can independently sign a resulting-state report. All three records may still describe different actions, different targets, different validity intervals, or different external events.

Examples include:

- an execution result referencing a superseded governance determination;
- an authorized quantity of one becoming an executed quantity of ten;
- a valid determination for target A being replayed against target B;
- an enforcement point reporting success while the operation partially completed;
- an observation of state B being correlated to the wrong execution attempt;
- two records sharing a trace identifier while their signed payload digests disagree;
- a governance determination remaining cryptographically valid after authority or evidence became stale;
- a complete internal evidence chain contradicting independently observed external state.

These are failures of lifecycle correlation, execution binding, temporal validity, or consequence binding. They are not cured by anchoring, custody, signing, consensus, or shared identifiers alone.

## 2. Relationship to current SAFE work

This candidate is designed to compose with, not replace:

- [SAFE public comment on evidence reconciliation and independent verification](https://github.com/OpenSecureAIAlliance/RFCs/issues/14);
- [Anchored Evidence for SAFE, PR #18](https://github.com/OpenSecureAIAlliance/RFCs/pull/18); and
- [SAFE Chain-of-Custody Receipt Profile, PR #27](https://github.com/OpenSecureAIAlliance/RFCs/pull/27).

The intended boundary is:

| Property | Candidate owner |
|---|---|
| Temporal existence, anchoring status, producer-basis evidence | PR #18 or its successor |
| Collection, transfer, transformation, durable acceptance, custody continuity | PR #27 or its successor |
| Correlation across proposal, determination, enforcement, execution, observation, and reconciliation | This profile |

This profile references anchoring and custody results without redefining their mechanisms. It does not assume that either related proposal will be adopted.

## 3. Requirements language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in BCP 14, [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174), when and only when they appear in all capitals.

## 4. Scope

### 4.1 In scope

This profile specifies:

- a runtime-neutral lifecycle record;
- typed, integrity-verifiable relationships between lifecycle records;
- the minimum binding properties needed at each stage;
- explicit validity, freshness, revocation, replay, and material-change evidence;
- independent property evaluations rather than a single undifferentiated trust flag;
- canonical failure and uncertainty semantics;
- conformance behavior and candidate test vectors; and
- the evidence needed to distinguish authorization, execution, and consequence.

### 4.2 Out of scope

This profile does not specify:

- how a policy engine reaches a governance determination;
- which policies, laws, or organizational rules are correct;
- an identity provider, delegation protocol, or authorization language;
- a transport, event bus, storage service, or evidence repository;
- one signature, encryption, anchoring, or custody mechanism;
- a universal evidence schema;
- a consensus or distributed-witness protocol;
- whether an external observation is objectively true;
- whether a model, agent, sensor, human, or tool behaved honestly;
- a requirement to publish sensitive evidence;
- a safety certification; or
- a claim that a correlated action was appropriate, safe, lawful, or beneficial.

## 5. Core principle

The profile preserves the following independent questions:

| Property | Question |
|---|---|
| Authority | Was the requesting principal presently entitled to request the transition? |
| Admissibility | Was the proposed transition allowable under the applicable evidence, policy, context, dependency, temporal, and consequence constraints? |
| Lifecycle correlation | Do the records refer to the same governed transition? |
| Execution integrity | Was the authorized operation the operation actually attempted and completed? |
| Consequence integrity | Did the observed resulting state correspond to the transition that governance authorized? |
| Grounding | How strongly does the admitted evidence or observation correspond to external reality? |
| Component integrity | Have the bytes, signatures, identifiers, and declared representations verified? |
| Temporal anchoring | Can existence at a relevant time and history be independently established? |
| Chain of custody | Can handling, transfer, transformation, and durable acceptance be reconstructed? |

A conformant implementation MUST NOT infer one row from another.

In particular:

- a valid signature does not establish truth;
- an anchor does not establish custody or completeness;
- custody does not establish authorization;
- authorization does not establish execution;
- execution does not establish consequence;
- consensus does not establish external ground truth; and
- a shared trace or lifecycle identifier does not establish correct correlation.

## 6. Terminology

**Proposed transition** — A normalized request to change a target from an expected before-state toward an intended after-state under declared parameters and constraints.

**Governance determination** — A versioned result evaluating a proposed transition. Candidate outcomes are `allow`, `deny`, `hold`, `escalate`, and `constrain`.

**Enforcement event** — The enforcement point's acceptance, rejection, or attempted consumption of a governance determination.

**Execution result** — A report of what operation was attempted and what the execution substrate reports occurred. It is not, by itself, proof of external consequence.

**Observation** — A report about resulting state produced by an identified observer under a declared observation method and trust domain.

**Reconciliation result** — A comparison between the governed expected transition, execution evidence, and one or more observations.

**Lifecycle** — The set of records and typed links associated with one proposed transition and its attempted or non-attempted consequence.

**Material change** — A change to an actor, authority, action, target, parameter, policy, evidence, dependency, context, validity condition, or expected consequence that can change admissibility or execution meaning.

**Irreversible boundary** — The last point before an action becomes impossible, impractical, unsafe, or disproportionately costly to reverse.

**Trust domain** — The administrative and verification context in which an identity, key, role, or assertion is meaningful.

**Grounding uncertainty** — Residual uncertainty about whether a signed or integrity-protected claim corresponds to external reality.

## 7. Lifecycle stages and timepoints

Implementations MAY use different internal stage names, but a conformant mapping MUST preserve these distinctions:

| Timepoint | Stage | Required distinction |
|---|---|---|
| `T0` | Evidence observation | When evidence or context was observed |
| `T1` | Governance evaluation | When admissibility was evaluated |
| `T2` | Determination issuance | When the determination became available |
| `T3` | Enforcement acceptance | When the enforcement point accepted or rejected it |
| `T4` | Irreversible boundary | Last safe point for required revalidation |
| `T5` | Execution completion | When the execution substrate reported completion or termination |
| `T6` | Resulting-state observation | When a consequence was observed |
| `T7` | Reconciliation | When expected and observed state were compared |

Wall-clock timestamps are claims. They MUST identify their format and source. Timestamps SHOULD use UTC [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) representations. A timestamp MUST NOT be treated as independently authenticated time unless the evidence supporting that property is also identified.

Sequence numbers, nonces, monotonic counters, epochs, or external timestamp evidence MAY supplement wall-clock time.

## 8. Abstract data model

The profile consists of:

1. one lifecycle envelope;
2. one or more typed lifecycle records;
3. typed links among records;
4. independent verification results; and
5. declared limitations and unresolved uncertainties.

Field names are descriptive. Implementations MAY use any open representation that preserves equivalent semantics.

### 8.1 Lifecycle envelope

The envelope MUST contain:

| Field | Requirement |
|---|---|
| `profile` | Stable profile identifier |
| `profile_version` | Version of this profile |
| `lifecycle_id` | Collision-resistant identifier scoped by issuer and trust domain |
| `transition_id` | Stable identifier for the proposed state transition |
| `created_at` | Envelope creation time claim |
| `producer` | Identity and trust domain of the envelope producer |
| `records` | Typed lifecycle records |
| `links` | Typed, integrity-protected relationships |
| `evaluation_contract` | Versioned property-set, verifier-method, and aggregation-rule identifiers |
| `evaluations` | Independent property results |
| `limitations` | Known gaps, unavailable evidence, or residual uncertainty |

The `lifecycle_id` is a correlation aid, not proof. Implementations MUST verify record digests and typed links rather than joining records solely by identifier equality.

### 8.2 Common lifecycle record

Every record MUST contain:

- `record_id` unique within its issuer and trust domain;
- `record_type`;
- `schema_id` and schema version;
- `digest_algorithm` and payload digest;
- `canonicalization_id` or an explicit `as-transmitted` representation rule;
- producer identity and trust domain;
- issuance time claim;
- signature or integrity mechanism reference;
- availability state; and
- any applicable anchoring reference and a loss-aware custody projection, or explicit unavailable states.

Permitted record types in version 0.1 are:

- `proposal`;
- `governance_determination`;
- `enforcement_event`;
- `execution_result`;
- `observation`; and
- `reconciliation_result`.

Transforming, redacting, normalizing, aggregating, or reserializing a record creates a new record identity and digest. The transformed record MUST link to its inputs or explicitly declare that linkage unavailable.

### 8.2.1 Loss-aware custody projection

This profile consumes custody evidence produced under PR #27 or a successor without redefining its receipt or transfer mechanisms. A record's custody projection MUST preserve, at minimum, these distinct states:

- `never_provided`;
- `offered_not_accepted`;
- `accepted_available`;
- `accepted_unavailable`; and
- `insufficient_evidence`.

The projection MUST identify the verifier, verifier method and version, and the evidence basis used. When a custody result or receipt exists, the projection MUST reference its immutable identity and digest. An `accepted_available` projection MUST include a retrievable result reference and MUST NOT be derived solely from a producer-supplied summary. An `accepted_unavailable` projection MUST preserve the last accepted result identity and the evidence supporting subsequent loss of availability.

Sender-side success, including creation or transmission of an offer, MUST NOT be represented as counterparty acceptance. A missing, inaccessible, or unverifiable custody result MUST NOT produce `custody_continuity: pass`. Transformation creates a new evidence identity and MUST preserve references to the applicable input and output custody results.

### 8.2.2 Anchoring-result projection

This profile consumes anchoring results under PR #18 or a successor; it does not define a replacement anchoring protocol. A supplied `anchor.status: anchored` is a claim requiring verification, not a produced `temporal_anchoring: pass` result. In the JSON representation, an anchored claim MUST include `reference` (a result locator) and `result_ref` (the immutable result identity and digest). Missing either is a structural error. `unanchored` and `unavailable` remain distinct supplied states and do not imply successful verification.

The referenced result, directly or through its digest-bound evidence, MUST identify:

- the exact anchored object and its kind (for example, record payload or receipt), identity, digest algorithm and digest;
- the object's schema and canonicalization or explicit byte-representation rule;
- the immutable anchoring-result identity and digest matching `result_ref`;
- the verifier identity/trust domain, method and version;
- immutable references to the evidence actually evaluated; and
- the inclusion, independently authenticated timing, and history-consistency basis actually checked, with unavailable checks and limitations explicit.

These details MAY remain in the referenced #18 result instead of being duplicated in the lifecycle record. A locator alone does not establish their existence, integrity, or applicability. The consumer MUST verify the result binding to the particular object whose anchoring it reports. Anchoring a receipt MUST NOT be promoted into anchoring its referenced payload. A result for a different object cannot substantiate the lifecycle record's anchoring claim.

For structurally well-formed claims, missing, inaccessible, or otherwise unevaluable referenced result evidence MUST produce `temporal_anchoring: insufficient_evidence` for the affected applicable claim. Demonstrated integrity failure or a demonstrated object/result binding mismatch MUST produce `fail`. Inclusion that verifies while time remains solely operator-asserted MUST NOT produce `pass`; it produces `insufficient_evidence` for temporal anchoring. Producer assertions about these checks MUST NOT substitute for the checks. For a lifecycle-wide temporal evaluation of multiple applicable anchoring claims, any demonstrated failure takes precedence over insufficient evidence; otherwise any unresolved required claim prevents `pass`.

The temporal result remains separate from mandatory correlation aggregation in section 10.2. Thus correlation can be `correlated` while temporal anchoring is `fail` or `insufficient_evidence`. The schema checks required references, not their retrieval, cryptography, or temporal validity.

### 8.3 Proposed-transition record

A `proposal` record MUST bind:

- originating principal and effective authority reference;
- normalized action;
- target identity and target trust domain;
- normalized parameters or their digest;
- expected before-state reference, where applicable;
- intended after-state reference or transition predicate;
- evidence and context references;
- requested validity or completion constraints;
- consequence classification, where used; and
- a nonce or idempotency key when replay or duplicate execution is relevant.

### 8.4 Governance-determination record

A `governance_determination` record MUST bind:

- the exact proposal record identity and digest;
- the evaluated actor, action, target, parameters, context, and evidence set;
- policy identifier, version, provenance reference, and effective interval;
- authority and delegation evidence references;
- determination outcome;
- canonical reason codes;
- `issued_at`, `not_before`, and `not_after` claims;
- maximum permitted uses;
- material-change invalidators;
- revocation mechanism or explicit non-revocability declaration;
- required revalidation conditions; and
- governance producer identity and trust domain.

An `allow` outcome MUST NOT be represented as proof that admitted evidence was objectively true.

### 8.5 Enforcement-event record

An `enforcement_event` record MUST bind:

- the exact determination identity and digest;
- the exact proposal identity and digest;
- enforcement-point identity, software or artifact identity when available, and trust domain;
- acceptance outcome: `accepted`, `rejected`, `unavailable`, or `insufficient_evidence`;
- the actual actor, action, target, and normalized parameters presented for enforcement;
- validity, revocation, material-change, and use-count checks performed;
- the check time and evidence used;
- the nonce or idempotency key consumed;
- whether the irreversible boundary had been crossed; and
- a machine-readable reason for any non-accepted outcome.

An enforcement point MUST reject or hold execution when a required binding cannot be verified. It MUST NOT silently treat unavailable evidence as valid.

### 8.6 Execution-result record

An `execution_result` record MUST bind:

- the exact enforcement-event identity and digest;
- the normalized operation actually attempted;
- actual actor, target, and parameters;
- execution start and completion time claims;
- result status: `not_attempted`, `started`, `completed`, `partial`, `failed`, `rolled_back`, `compensated`, `unknown`, or `unavailable`;
- execution-substrate identity and trust domain;
- output or side-effect references;
- duplicate, retry, replay, rollback, and compensation indicators; and
- any divergence from the enforced operation.

The result MUST distinguish command acceptance from operation completion.

### 8.7 Observation record

An `observation` record MUST bind:

- observer identity and trust domain;
- observation method and method version;
- observed target;
- observed state reference or digest;
- observation time claim and freshness bound;
- execution or transition reference being observed;
- independence basis, if independence is claimed;
- sensor, runtime, or artifact identity when relevant;
- confidence or uncertainty representation, where used; and
- known observation limitations.

An observation MUST NOT claim independence merely because it was produced by a separate process. Administrative control, infrastructure, data dependencies, signing authority, and recovery paths SHOULD be declared when relevant.

### 8.8 Reconciliation-result record

A `reconciliation_result` record MUST bind:

- the proposal, determination, enforcement, execution, and observation records actually evaluated;
- the expected transition predicate;
- the observed resulting-state evidence;
- the reconciliation method and version;
- the result;
- canonical reason codes;
- conflicting or missing evidence references;
- residual grounding uncertainty; and
- reconciler identity and trust domain.

Permitted reconciliation results are:

- `matched`;
- `missing`;
- `conflicting`;
- `unresolved`; and
- `not_applicable`.

`matched` means only that the declared reconciliation method found the supplied expected and observed representations consistent. It does not eliminate grounding uncertainty.

## 9. Typed lifecycle links

Every lifecycle link MUST contain:

- `link_id`;
- `relation`;
- source record identity and digest;
- target record identity and digest;
- asserting identity and trust domain;
- assertion time claim;
- schema and canonicalization identifiers;
- signature or integrity mechanism reference; and
- verification status.

Version 0.1 defines these relations:

| Relation | Source → target | Meaning |
|---|---|---|
| `evaluates` | determination → proposal | Determination evaluated this exact proposal |
| `enforces` | enforcement → determination | Enforcement event consumed or rejected this determination |
| `attempts` | execution result → enforcement | Result reports the operation attempted under this enforcement event |
| `observes` | observation → execution result or proposal record | Observation reports state associated with the referenced execution or transition |
| `reconciles` | reconciliation → referenced lifecycle records | Reconciliation evaluated the identified evidence set |
| `supersedes` | later record → earlier record | Later record explicitly replaces an earlier record without deleting history |
| `transforms` | output record → input record | Output is a declared transformation of input |

The link MUST bind record digests, not only record identifiers.

A verifier MUST reject or mark insufficient any link whose referenced digest does not match the retrieved representation.

Verified typed links establish only that the supplied records are related as declared under this profile. They MUST NOT be represented as proof that the described action was attempted or completed,
that it caused an observed state, or that the observation is externally true. Those propositions require separate execution, consequence, and grounding evaluations.

## 10. Independent property evaluation

A verifier MUST report each applicable property separately using:

- `pass`;
- `fail`;
- `insufficient_evidence`; or
- `not_applicable`.

The minimum evaluation matrix is:

| Property | Minimum verification question |
|---|---|
| `component_integrity` | Do declared digests, canonicalization rules, signatures, and referenced bytes verify? |
| `proposal_binding` | Did the determination evaluate the exact proposal? |
| `authority_validity` | Was the authority evidence valid at the required decision and enforcement points? |
| `determination_validity` | Was the outcome applicable, unexpired, unrevoked, and within use constraints? |
| `enforcement_binding` | Did enforcement validate and consume the exact determination and proposal? |
| `execution_binding` | Did the reported operation match the enforced operation? |
| `consequence_binding` | Did the observation and reconciliation address the resulting state of the same transition? |
| `replay_resistance` | Was duplicate or out-of-scope reuse prevented or explicitly detected? |
| `temporal_anchoring` | What anchoring status and independently checkable timing/history basis exist? |
| `custody_continuity` | What handling, transfer, transformation, and durable-acceptance evidence exists? |
| `producer_basis` | What evidence supports producer identity, control, and any claimed separation? |
| `grounding` | What supports correspondence between the records and external reality? |

### 10.1 Evaluation contract and applicability

Every evaluation set MUST identify:

- a versioned property-set identifier;
- the mandatory properties in that set;
- the verifier method identifier and version;
- a versioned aggregation rule; and
- whether verifier independence is claimed and the evidence basis for that claim.

Version 0.1 defines the full-lifecycle property set `safe-galc/0.1/full-lifecycle`. Its mandatory correlation properties are:

- `component_integrity`;
- `proposal_binding`;
- `authority_validity`;
- `determination_validity`;
- `enforcement_binding`;
- `execution_binding`;
- `consequence_binding`; and
- `replay_resistance`.

Each mandatory property MUST appear exactly once. `temporal_anchoring`, `custody_continuity`, `producer_basis`, and `grounding` MAY also appear, but no property may appear more than once in one evaluation set. Duplicate or conflicting results for the same property make the evaluation set non-conformant and MUST prevent an overall result of `correlated`.

Applicability is determined from the lifecycle stages and claims being evaluated. A legitimately absent stage, such as execution after a denied determination, MUST be reported as `not_applicable` with an explanatory reason code; implementations MUST NOT fabricate execution or observation records. A required stage or evidence item that cannot be obtained is `insufficient_evidence`, not `not_applicable`.

Verifier identity alone does not establish a verification method or verifier independence. Method and version MUST be explicit. Independence MUST NOT be claimed without a stated basis addressing relevant administrative control, infrastructure, data dependencies, signing authority, and recovery paths.

### 10.2 Overall-result aggregation

An implementation MAY calculate an overall lifecycle result, but it MUST retain the property matrix and MUST NOT convert `insufficient_evidence` into `pass`.

If reported, `overall_result` MUST be one of:

- `correlated`;
- `correlation_failed`;
- `insufficient_evidence`; or
- `not_applicable`.

Version 0.1 defines aggregation rule `safe-galc/0.1/mandatory-precedence`, version `1`:

1. if any applicable mandatory property is `fail`, the overall result is `correlation_failed`;
2. otherwise, if any applicable mandatory property is `insufficient_evidence`, the overall result is `insufficient_evidence`;
3. otherwise, if every applicable mandatory property is `pass` and at least one mandatory property is applicable, the overall result is `correlated`; and
4. if no mandatory property is applicable, the overall result is `not_applicable`.

`not_applicable` properties do not affect aggregation. The independently reported `temporal_anchoring`, `custody_continuity`, `producer_basis`, and `grounding` properties do not alter `overall_result` under this rule; their failures and uncertainties MUST remain visible and MUST NOT be rewritten as success.

`correlated` does not mean safe, trustworthy, truthful, or authorized in a broader legal or organizational sense.

## 11. Material change and TOCTOU

The verifier MUST evaluate whether any material input changed between governance evaluation and the irreversible boundary.

At minimum, implementations MUST support change evidence for:

- actor identity;
- authority and delegation;
- action;
- target;
- parameters;
- evidence freshness;
- policy version and effective state;
- relevant context;
- dependency state;
- revocation state; and
- expected consequence constraints.

A material change MUST produce one of:

- revalidation under the declared policy;
- deterministic rejection;
- hold or escalation; or
- an explicit `insufficient_evidence` result.

Silently continuing under the earlier determination is non-conformant when the determination declares that change invalidating.

## 12. Revocation, expiry, replay, and duplicate execution

A conformant lifecycle MUST represent:

- validity start and end;
- revocation status or the inability to determine it;
- maximum use count;
- consumed nonce or idempotency key;
- duplicate and retry state;
- the enforcement check nearest the irreversible boundary; and
- the result when revocation arrives during execution.

A valid signature on an expired, revoked, superseded, or previously consumed determination MUST NOT cause `determination_validity: pass`.

Retries MUST remain distinguishable from duplicate consequential execution. When the execution substrate cannot establish whether a prior attempt crossed the irreversible boundary, it SHOULD hold or escalate rather than assume the operation is safe to repeat.

## 13. Canonical reason codes

Version 0.1 defines the following minimum reason-code vocabulary:

| Reason code | Meaning |
|---|---|
| `record_missing` | A required lifecycle record is unavailable |
| `record_digest_mismatch` | Retrieved bytes do not match the referenced digest |
| `link_integrity_failure` | A typed link cannot be verified |
| `proposal_digest_mismatch` | Determination does not bind the supplied proposal |
| `actor_mismatch` | Actual actor differs from the governed actor |
| `target_mismatch` | Actual or observed target differs from the governed target |
| `action_mismatch` | Actual operation differs from the governed action |
| `parameters_mismatch` | Actual parameters differ materially from governed parameters |
| `policy_mismatch` | Applied policy identity or version differs from the determination |
| `authority_invalid` | Required authority was absent, invalid, expired, or revoked |
| `determination_denied` | Governance outcome did not authorize execution |
| `determination_expired` | Enforcement occurred outside the validity interval |
| `determination_revoked` | Determination or supporting authority was revoked |
| `determination_superseded` | A later determination replaced the referenced one |
| `evidence_stale` | Required evidence exceeded its freshness bound |
| `material_change_unvalidated` | A material change occurred without required revalidation |
| `replay_detected` | Previously consumed authorization was presented again |
| `duplicate_execution` | The consequential operation occurred more than permitted |
| `execution_partial` | Only part of the governed operation completed |
| `execution_unknown` | Completion could not be established |
| `observation_missing` | Required resulting-state observation is unavailable |
| `observation_conflict` | Observers report materially inconsistent resulting state |
| `consequence_mismatch` | Observed state does not satisfy the governed transition predicate |
| `observer_basis_unknown` | The claimed observer relationship cannot be established |
| `custody_gap` | Required custody transition or transformation evidence is missing |
| `custody_not_accepted` | Sender-side success exists without counterparty acceptance |
| `custody_accepted_then_unavailable` | Evidence was accepted but is no longer available for verification |
| `custody_result_reference_missing` | A custody projection claims acceptance without a checkable result identity |
| `duplicate_property_evaluation` | More than one result was supplied for the same property in one evaluation set |
| `anchor_unavailable` | Required anchoring evidence cannot be obtained or evaluated |
| `anchor_time_unsubstantiated` | Inclusion evidence does not independently authenticate the claimed time |
| `anchor_result_invalid` | Anchoring result integrity or exact-object binding demonstrably fails |
| `correlation_ambiguous` | More than one lifecycle relationship remains plausible |
| `grounding_unresolved` | Record integrity verifies but correspondence to reality remains unresolved |

Implementations MAY add namespaced reason codes. Unknown reason codes MUST be preserved and MUST NOT be silently mapped to success.

## 14. Illustrative representation

The companion JSON Schema supplies one candidate representation. This abbreviated example is informative:

```json
{
  "profile": "safe-galc",
  "profile_version": "0.1",
  "lifecycle_id": "urn:uuid:3d8f3a43-c6c6-40b0-8f34-b6ca2d9fa510",
  "transition_id": "urn:example:transition:inventory-42",
  "created_at": "2026-09-17T12:00:08Z",
  "producer": {
    "id": "urn:example:reconciler:1",
    "trust_domain": "example.org"
  },
  "records": [
    {
      "record_id": "urn:example:record:proposal-1",
      "record_type": "proposal",
      "schema_id": "urn:example:schema:proposal:1",
      "canonicalization_id": "rfc8785-jcs",
      "digest_algorithm": "sha-256",
      "digest": "sha256:0000000000000000000000000000000000000000000000000000000000000001",
      "producer": {"id": "urn:example:agent:7", "trust_domain": "example.org"},
      "issued_at": "2026-09-17T12:00:00Z",
      "availability": "available",
      "integrity": {"status": "pass", "method": "example-signature-profile"}
    }
  ],
  "links": [],
  "evaluations": [
    {
      "property": "component_integrity",
      "result": "pass",
      "checked_at": "2026-09-17T12:00:08Z",
      "verifier": {"id": "urn:example:verifier:1", "trust_domain": "review.example"},
      "reason_codes": []
    }
  ],
  "overall_result": "insufficient_evidence",
  "limitations": ["Illustrative record omits the remaining lifecycle stages."]
}
```

JSON implementations using structured canonicalization SHOULD identify a versioned canonicalization profile. [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785) is one candidate for JSON, but this profile does not mandate it. Implementations MUST preserve the exact representation needed to reproduce every declared digest.

## 15. Conformance

### 15.1 Producer conformance

A conformant producer:

1. emits all required fields for each record type it claims to produce;
2. binds references by record identity and digest;
3. identifies schema, canonicalization, digest, and integrity mechanisms;
4. represents missing and unavailable evidence explicitly;
5. preserves material changes, supersession, retries, and transformations rather than rewriting history; and
6. does not claim properties it did not evaluate.

### 15.2 Verifier conformance

A conformant verifier:

1. validates the profile version and representation;
2. validates record and link integrity;
3. checks typed-link source and target digests;
4. evaluates applicable validity, revocation, freshness, material-change, and use constraints;
5. reports each independent property separately;
6. preserves `fail` and `insufficient_evidence` results;
7. does not upgrade anchoring, custody, signature, attestation, or consensus into truth; and
8. emits canonical or namespaced reason codes;
9. identifies its method and version and does not infer independence from identity alone;
10. emits each mandatory property exactly once under a declared property set; and
11. applies the declared aggregation rule without allowing non-aggregating properties to disappear.

### 15.3 Full-lifecycle profile conformance

A system claiming full-lifecycle conformance MUST demonstrate at least:

- one authorized and matched transition;
- one denied transition with no execution;
- one expired or revoked determination rejected at enforcement;
- one proposal, target, action, or parameter mismatch;
- one replay or duplicate-execution attempt;
- one partial or unknown execution result;
- one missing observation;
- one conflicting observation set;
- one consequence mismatch;
- one valid component set with an invalid cross-record correlation; and
- one lifecycle in which cryptographic integrity passes while grounding remains unresolved.

## 16. Candidate conformance vectors

The companion conformance file defines machine-readable skeletons for these minimum cases:

| Vector | Condition | Required result |
|---|---|---|
| `GALC-001` | Exact proposal, live determination, matching execution, matching observation | `correlated` |
| `GALC-002` | All records individually valid; execution references the wrong determination | `correlation_failed` |
| `GALC-003` | Determination expired before enforcement | `correlation_failed` |
| `GALC-004` | Authority revoked between issuance and irreversible boundary | `correlation_failed` |
| `GALC-005` | Executed parameters differ materially from authorized parameters | `correlation_failed` |
| `GALC-006` | Previously consumed determination is replayed | `correlation_failed` |
| `GALC-007` | Execution reports partial completion while the attempted operation remains correctly bound | Execution binding `pass`; consequence binding and overall result `insufficient_evidence` |
| `GALC-008` | Required resulting-state observation is missing | `insufficient_evidence` |
| `GALC-009` | Independent observers conflict | `insufficient_evidence` |
| `GALC-010` | Internal records agree; observed consequence differs | `correlation_failed` |
| `GALC-011` | Anchoring passes; custody is incomplete | Correlation evaluated separately; custody `fail` or `insufficient_evidence` |
| `GALC-012` | Custody passes; temporal anchoring unavailable | Correlation evaluated separately; anchoring `insufficient_evidence` |
| `GALC-013` | All component records verify; lifecycle link digest is wrong | `correlation_failed` |
| `GALC-014` | Component and correlation integrity pass; external truth cannot be independently established | Correlation MAY pass; grounding `insufficient_evidence` |
| `GALC-015` | Sender reports a successful offer without counterparty acceptance | Custody `fail`; sender-side success MUST NOT become acceptance |
| `GALC-016` | Evidence was accepted and later became unavailable | Custody `insufficient_evidence`; preserve prior acceptance and later loss |
| `GALC-017` | Custody claims acceptance without a referenced result | Input structural negative; no semantic oracle |
| `GALC-018` | Two evaluations report the same property | Output-envelope structural negative; no semantic oracle |
| `GALC-019` | Anchored claim lacks required references | Input structural negative; no semantic oracle |
| `GALC-020` | Referenced anchoring result is inaccessible | Temporal anchoring `insufficient_evidence`; correlation evaluated separately |
| `GALC-021` | Inclusion verifies; time remains operator-asserted | Temporal anchoring `insufficient_evidence`; correlation evaluated separately |
| `GALC-022` | Referenced anchoring result demonstrably fails integrity | Temporal anchoring `fail`; correlation evaluated separately |

### 16.1 Scenario construction and verifier-output boundary

The companion file contains 22 ordered candidate scenario skeletons, not cryptographic known-answer evidence. `base_lifecycle` is a structural fixture envelope: its `evaluations` and `overall_result` are placeholders used only for full-envelope schema tests, never results produced for a materialized vector. `base_verification_context` separately declares synthetic resolver/test-double inputs for upstream anchoring evidence; it is not executed verification and does not establish real-world anchoring.

A conforming scenario materializer MUST:

1. deep-copy the base lifecycle and verification context for each vector;
2. apply `semantic_changes` in order using only `add`, `remove`, and `replace` with JSON Pointer semantics; changes MAY address either base object;
3. check the changed full fixture envelope against the lifecycle schema, preserving structural negative controls including output-only mutations;
4. project the lifecycle input by removing `evaluations` and `overall_result`;
5. emit the fixture envelope, projected scenario input, verification context, and expected-output artifact separately;
6. classify the case by `test_scope`: `semantic_scenario`, `structural_input_negative`, or `output_envelope_negative`;
7. omit `semantic_verifier_output` for structural negative cases and explicitly mark semantic comparison `not_applicable`; their `expected` object contains only `schema_validation: fail`;
8. for eligible semantic cases, pass only the projected input and explicitly declared verification context to a future verifier, which MUST produce new evaluations independently of the expected-output artifact; and
9. compare independently produced outputs according to section 16.2 only after the semantic case's structural precondition succeeds.

The emitted `<scenario>.fixture-envelope.json` is explicitly labelled as a structural fixture and is the target of the schema check. Its placeholder or deliberately invalid output fields MUST NOT be consumed as actual results. `<scenario>.scenario-input.json` contains no top-level verifier outputs. `<scenario>.verification-context.json` contains the synthetic evidence environment, and `<scenario>.expected-output.json` identifies scope, structural expectations, and semantic applicability. This preserves GALC-018's invalid evaluation set for inspection without assigning a contradictory oracle to its otherwise baseline input.

A future driver MUST instantiate the declared resolver/test doubles and record their immutable revision with the run. Their supplied upstream check conditions are test inputs, not the produced GALC property matrix. In this fixture format, `resolution: inaccessible` makes the referenced result unavailable regardless of other retained fixture fields; `result_integrity: invalid` declares a demonstrably invalid upstream result; `time_basis: operator_asserted` supplies no independently authenticated time. A driver MUST NOT silently substitute live evidence or a different trust context. Production verifiers MUST perform or verify the actual upstream checks rather than trust these fixture declarations.

When `recompute_integrity` is true, a future materializer performing an implementation run MUST recompute affected payload digests under their declared representations, update dependent record and link references transitively, and regenerate or remove invalidated integrity assertions. Changed objects require newly valid anchoring evidence; updating a reference does not renew an old anchor. When false, preserve deliberately inconsistent bindings for testing. This structural harness does not perform that cryptographic work. Supplied digests, result references, and upstream fixtures are synthetic.

### 16.2 Partial-expectation comparison and consistency

Comparison rule `safe-galc/0.1/partial-expectations/1` applies only to `semantic_scenario` cases. Before comparing an oracle, the produced evaluation set MUST satisfy the full output schema, the mandatory-property and uniqueness rules of section 10.1, and the applicability requirements. The aggregate MUST be independently derived under the declared rule in section 10.2, not copied from the oracle.

- Every property named in `expected.evaluations` MUST exist in the produced set and match the specified status exactly.
- Unspecified properties are not asserted by the partial oracle. They remain subject to the full evaluation contract; omission from an oracle is not permission to omit mandatory produced evaluations.
- `expected.reason_codes` is a required subset of the union of `reason_codes` across the produced property evaluations. Order is immaterial and additional contract-permitted codes are allowed. This flat list does not assert which property carries a code; a test needing that distinction requires a future versioned expectation format.
- If `expected.overall_result` is present, it MUST equal the independently aggregated produced result exactly.
- Structural negative cases have no semantic expectation. Their invalid fixture is tested for structural rejection only; projection does not make them semantic test cases.

The harness MUST reject incompatible partial expectations for identical projected inputs, verification contexts, and integrity-recomputation modes. It compares specified aggregate values and overlapping property statuses; compatible partial maps may coexist and required reason-code subsets may accumulate. Scenario IDs, titles, and expected outputs are not verifier inputs and MUST NOT be used to distinguish otherwise identical cases. The JSON serialization used for this local equality check is not a cryptographic canonicalization claim.

These checks establish fixture scope and oracle consistency, not the truth of semantic expectations. No semantic verifier or cryptographic/runtime conformance is claimed by this harness.

## 17. Security and abuse considerations

Implementations MUST consider at least:

- identifier collision and correlation injection;
- substitution of records sharing display names but belonging to different trust domains;
- signature, canonicalization, or digest algorithm downgrade;
- replay of valid determinations against new actions or targets;
- stale evidence and TOCTOU changes;
- policy rollback or equivocation;
- authority or delegation revocation suppression;
- enforcement bypass;
- execution-parameter substitution;
- partial, duplicate, split, or compensated execution;
- observer compromise and sensor disagreement;
- forged or omitted reconciliation;
- cross-organizational clock disagreement;
- transformed evidence without lineage;
- split views of anchoring or custody records;
- recovery-path and administrative-key abuse; and
- disclosure created by stable cross-system correlation identifiers.

No single cryptographic mechanism resolves all of these threats.

### 17.1 Correlation identifier abuse

Stable identifiers can leak relationships among parties, incidents, actions, and systems. Implementations SHOULD minimize scope, rotate or pseudonymize identifiers where accountability permits, and apply the same access restrictions to linkage metadata as to the underlying evidence.

### 17.2 Cross-domain identity ambiguity

Matching email addresses, local subject identifiers, or display names MUST NOT establish identity equivalence across trust domains. Cross-domain equivalence requires an explicit, scoped, integrity-protected binding with revocation semantics.

### 17.3 Attestation limits

Runtime attestation can support claims about measured software or platform state. It does not automatically establish complete capture, policy correctness, honest sensor input, continuous observation, or truthful external consequence. Implementations using attestation SHOULD state the appraisal policy, reference values, freshness evidence, instance binding, and residual assumptions. See the [RATS architecture, RFC 9334](https://www.rfc-editor.org/rfc/rfc9334).

### 17.4 Trace-context limits

Distributed trace identifiers can aid propagation and diagnostics but are not authorization or evidence-integrity mechanisms. A trace identifier MAY be retained as an auxiliary reference, but it MUST NOT replace digest-bound lifecycle links. See the [W3C Trace Context Recommendation](https://www.w3.org/TR/trace-context/).

### 17.5 Provenance mapping

Implementations MAY map lifecycle entities, activities, and agents to the [W3C PROV Data Model](https://www.w3.org/TR/prov-dm/). Such mapping does not remove this profile's authorization, validity, revocation, or correlation requirements.

## 18. Privacy and disclosure considerations

Lifecycle evidence can reveal:

- identities and organizational relationships;
- privileged actions and targets;
- policy and security architecture;
- incident timing;
- physical or operational state;
- unsuccessful or denied activity; and
- links that reverse de-identification.

Implementations SHOULD:

- minimize public metadata;
- separate public commitments from restricted payloads;
- use scoped identifiers;
- document retention and deletion rules;
- preserve transformation receipts for redaction;
- prevent low-entropy digest confirmation attacks where applicable; and
- avoid treating a content hash as anonymous disclosure.

## 19. Operational failure semantics

The profile does not require one universal runtime response. Runtime behavior depends on consequence class and reversibility. However, implementations MUST record which behavior occurred.

Candidate behaviors are:

- `deny`;
- `hold`;
- `retry`;
- `degrade`;
- `escalate`;
- `continue_bounded`;
- `rollback`;
- `compensate`; and
- `terminate`.

For irreversible or high-consequence actions, missing required correlation, validity, revocation, or grounding evidence SHOULD result in `deny`, `hold`, or `escalate` rather than fail-open execution.

## 20. Interoperability and versioning

Implementations MUST:

- identify the profile and profile version;
- reject unsupported major versions or mark them `insufficient_evidence`;
- preserve unknown fields and reason codes when relaying evidence where possible;
- not reinterpret an earlier record under a later schema or canonicalization rule;
- issue a new record when meaning or bytes change; and
- preserve prior records when a later record supersedes them.

Schema validation establishes structural conformance only. It does not establish semantic correctness, integrity, authorization, or external truth.

Structural validation MUST reject a missing required custody-result reference and duplicate property evaluations. Digest and link-target equality remain semantic checks that require a verifier; the `GALC-013` negative control exercises that boundary.

## 21. Adoption and implementation sequence

The smallest useful adoption sequence is:

1. review the property boundaries and terminology;
2. agree on the minimum lifecycle stages and typed links;
3. review the failure and uncertainty vocabulary;
4. publish candidate schema and vectors as non-normative test material;
5. run at least two independent implementations against the same vectors;
6. document disagreements rather than silently normalizing them;
7. exercise allowed, denied, expired, replayed, partial, conflicting, and consequence-mismatch cases; and
8. decide separately whether any part should become a SAFE requirement.

Publication of candidate test material MUST NOT be represented as Alliance adoption of the normative profile.

## 22. Open questions

1. Should correlation be represented as one envelope, independent link records, or both?
2. Which lifecycle stages are mandatory for denied or non-executed actions?
3. Should expected state be a digest, predicate, semantic claim, or typed external reference?
4. How should compound or multi-target actions be decomposed without enabling action splitting?
5. Which material changes require automatic invalidation versus policy-directed revalidation?
6. How should mid-execution revocation be represented after an irreversible boundary?
7. When may a retry reuse a transition identifier without becoming a duplicate execution?
8. What evidence is sufficient to claim observer independence?
9. How should conflicting observers be weighted without collapsing reconciliation into one vendor's confidence score?
10. Which correlation metadata can be safely public, and which must remain confidential?
11. How should the profile express probabilistic or interval-valued state without implying certainty?
12. Should conformance require an independent verifier implementation?

## 23. Claim boundary

Conformance with this candidate profile would establish only that an implementation can emit or verify the specified lifecycle records, links, property results, and failure semantics under declared assumptions.

It would not establish that:

- the system is secure or safe;
- the governance policy is correct;
- the action was lawful or ethically appropriate;
- the evidence or observation was true;
- every relevant event was captured;
- the execution substrate behaved honestly;
- the resulting state persisted;
- the profile prevents all replay, substitution, or collusion attacks;
- the implementation is production-ready; or
- the Open Secure AI Alliance, Linux Foundation, or any third party endorses the work.

## 24. References

- Bradner, S., [RFC 2119: Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119)
- Leiba, B., [RFC 8174: Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174)
- Klyne, G. and Newman, C., [RFC 3339: Date and Time on the Internet](https://www.rfc-editor.org/rfc/rfc3339)
- Laurie, B., Langley, A., and Kasper, E., [RFC 6962: Certificate Transparency](https://www.rfc-editor.org/rfc/rfc6962)
- Rundgren, A., Jordan, B., and Erdtman, S., [RFC 8785: JSON Canonicalization Scheme](https://www.rfc-editor.org/rfc/rfc8785)
- Birkholz, H. et al., [RFC 9334: Remote ATtestation procedureS Architecture](https://www.rfc-editor.org/rfc/rfc9334)
- W3C, [Trace Context](https://www.w3.org/TR/trace-context/)
- W3C, [PROV-DM: The PROV Data Model](https://www.w3.org/TR/prov-dm/)
- JSON Schema, [Draft 2020-12](https://json-schema.org/draft/2020-12)
- Open Secure AI Alliance, [SAFE RFC proposal](https://github.com/OpenSecureAIAlliance/RFCs/blob/main/rfc-safe-proposal.md)
- Open Secure AI Alliance, [Public Comment: Strengthening Evidence Reconciliation and Independent Verification in SAFE](https://github.com/OpenSecureAIAlliance/RFCs/issues/14)
- Open Secure AI Alliance, [RFC: Anchored Evidence for SAFE, PR #18](https://github.com/OpenSecureAIAlliance/RFCs/pull/18)
- Open Secure AI Alliance, [RFC: Add chain-of-custody receipt profile, PR #27](https://github.com/OpenSecureAIAlliance/RFCs/pull/27)

## Appendix A — Candidate implementation artifacts

- `SAFE_Governed_Action_Lifecycle_Correlation_Profile_v0.1.md` — normative candidate profile
- `safe-galc-v0.1.schema.json` — candidate JSON Schema representation
- `safe-galc-v0.1.conformance-vectors.json` — candidate machine-readable conformance skeletons
- `validate_safe_galc_vectors.py` — structural materializer and Draft 2020-12 validation harness (`jsonschema` 4.25.1)

The schema, vectors, and validation harness are candidate evaluation material. They are not adopted SAFE artifacts and do not establish cryptographic, semantic, runtime, or SAFE conformance by their existence or successful structural validation.

## Appendix B — Disclosure

This candidate was prepared by Gary Gayle, Founder and CEO of Value Intelligence Solutions Inc., as part of R.E.T.N.A.™ Proof of Governed State / Distributed Governance R&D. It is offered as an open evidence-model contribution, not as a request to adopt a proprietary implementation.
