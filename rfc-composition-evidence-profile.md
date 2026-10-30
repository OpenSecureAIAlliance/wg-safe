# SAFE Workflow-Composition Evidence Profile

This companion proposal defines the minimum properties needed to review a harmful sequence of individually permitted agent actions. It specifies evidence requirements and conformance behavior, not a transport, storage format or policy language.

# Problem

Per-action evidence can show that every action satisfied its immediate policy while missing that the sequence exceeded a cumulative budget, reconstructed restricted data, escalated authority through delegation or continued after revocation. A workflow-composition review needs to reconstruct both the aggregate trajectory and the transitions that produced external effects.

A record that shows an action was proposed or approved does not establish that it was committed or executed. A record that shows a side effect does not establish which authority and cumulative state permitted it. The evidence profile must keep those claims separate and link them.

# Minimum Record

The field names below are descriptive. Implementations may use any open representation that preserves the same properties.

## Workflow identity

* An issuer-scoped `workflow_id` assigned by governance infrastructure rather than selected or reset by the governed agent
* Parent workflow and delegation identifiers when the workflow was created by delegation
* Principal, agent and workload identities, including the trust domain in which each identity is meaningful
* Policy, comparison method and cumulative-ledger versions used for the decision
* The configured retention window and the reason for that window

For every cross-boundary handoff, each governance instance must retain its locally authoritative workflow identity and a durable binding to the counterpart workflow reference and trust domain. The evidence must identify the identity model in use — propagated foreign reference, independently minted identifiers with bilateral binding, protocol-produced shared identifier or an equivalent model — and which governance instance controls authorization in each trust domain. A foreign or shared correlation identifier alone confers no authority.

The record must also state which cross-boundary properties its identity model can establish, including revocation propagation, cumulative-constraint continuity, liability attribution and dispute reconstruction, and report unsupported properties as unavailable or unverified. A separate federation protocol may add shared identifiers, jointly attested boundary records or shared ledger semantics. This profile does not require one architecture: a shared service can itself become unavailable or partitioned, so its presence is not evidence that those properties held for a particular workflow.

## Action set

* Stable action identifiers and an ordered digest of the complete proposed action set
* Normalized action and resource identities sufficient to compare the proposal with granted authority
* Expected deltas to each cumulative constraint, such as spending, data volume, privilege scope or sensitivity ceiling
* Per-action validation results and one aggregate result for the complete set
* Explicit states for malformed, unsupported, unavailable and insufficient evidence; absence of a parsed action is not proof that no action was present

## Authority and cumulative state

* The authority or grant identifier, issuer, subject, scope, validity interval and revocation state
* Ledger state or version before the attempt, the requested aggregate delta and the state after a successful commit
* A replay or idempotency identifier bound to the action-set digest and authority
* For delegation, the scope received from the original principal, the delegate's independently held scope and the effective scope used for the delegated work
* When delegated authority derives from a negotiated agreement, a stable agreement reference or digest and the participant attestations required to establish that authority

The effective delegated scope must not exceed the intersection of the scope received from the original principal and the scope the delegate may exercise. Independently held authority must not be silently added to a delegated workflow.

This profile begins when an authority or grant exists. It preserves the evidence binding that authority to a negotiated agreement, when one exists, but does not define proposal, counterproposal, acceptance or commitment semantics for the negotiation that produced it.

## Lifecycle and receipts

Evidence must distinguish:

1. `proposed`: the complete action set was observed but not yet accepted.
2. `validated`: action and aggregate policy evaluation completed without mutating authority.
3. `reserved`: cumulative capacity was atomically reserved for the validated set.
4. `committed`: the governance system authorized release of the validated set.
5. `withheld`: the set was not released, with a machine-readable reason and the disposition of any reservation.
6. `executed`: an execution boundary produced a receipt for an externally observed effect.
7. `unknown`: available evidence cannot establish the lifecycle state.

Proposal, validation, reservation, commit and execution records should carry content or canonical digests and stable parent references. An anchored proposal proves neither commit nor execution. A commit proves neither successful delivery nor an external effect without the corresponding receipt.

The base lifecycle ends at `executed`; execution does not establish acceptance of a deliverable, settlement of reciprocal obligations or completion of a workflow. The state names `accepted`, `settled` and `completed` are reserved for extension profiles. Base-profile implementations must not alias them to `executed` or infer them without evidence governed by a declared extension. An extension record should name its semantic version and remain linked to the base workflow and downstream delegations.

# Behavioral Requirements

1. **Complete-set validation.** The governance system evaluates the complete proposed action set, including malformed and unsupported carriers, before committing authority tied to execution.
2. **Atomic cumulative decision.** Compare, reserve and commit operations affecting a cumulative constraint are atomic across concurrent workers. A sequence cannot exceed a limit because each worker observed the same stale state.
3. **Declared failure semantics.** The record states whether rejected attempts consume rate limits, abuse budgets or other attempt-based capacity. It must not silently consume execution-bound authority for a set that was withheld.
4. **Replay safety.** Retrying or replaying the same action-set and authority binding cannot create a second commitment or side effect without an explicitly new authorization.
5. **Delegation monotonicity.** Each delegation records the original and effective scope, sensitivity ceiling, cumulative constraints and downstream revocation reference. Delegation cannot expand the original principal's authority.
6. **Revocation propagation.** A revocation observed before commit prevents that workflow and its downstream delegates from committing. Evidence records the propagation result or reports it as unavailable.
7. **Cross-boundary continuity.** When a workflow crosses governance instances, each side preserves a durable handoff reference sufficient to join the trajectory without requiring disclosure of raw content or internal policy. The evidence declares whether reconstruction uses independently joinable fragments, a full trajectory held by one instance, cooperative assembly of bilateral fragments or another model, and what evidence, access and cooperation that model requires.
8. **Fail-explicit lineage.** Missing, ambiguous or reset workflow lineage is reported as unverified or insufficient evidence. It must not be interpreted as a fresh workflow with unused cumulative limits.

# Conformance Vectors

A conformant implementation should publish machine-runnable variants of at least these cases:

1. **Concurrent cumulative limit.** Two actions independently satisfy a per-action limit but jointly exceed a workflow limit. Exactly the allowed number of atomic commits succeeds, and the final ledger state is reproducible.
2. **Mixed valid and malformed set.** A permitted action followed by a malformed or denied action causes the complete set to be withheld. The record shows no external effect and no silent consumption of execution-bound authority.
3. **Replay.** Repeating an identical committed request with the same replay identifier does not create a second commitment or double-spend.
4. **Delegation privilege addition.** A delegate has an independent privilege that the original principal did not delegate. The downstream workflow cannot use that privilege under the delegated authority.
5. **Revocation race.** Authority is revoked after validation but before commit. Commit fails, downstream delegates remain unable to commit, and the evidence identifies the revocation observed.
6. **Missing lineage.** A worker presents an action with no verifiable workflow or parent-delegation identity. The result is unverified or insufficient evidence rather than a fresh cumulative budget.

Each vector should declare the policy and ledger versions, starting state, concurrent schedule where relevant, expected lifecycle records and externally observed effects. Local replay or simulation results must be distinguishable from live observations.

An implementation that claims cross-boundary continuity should also publish these federation-dependent vectors. They test the implementation's declared cooperation mechanism; they do not establish conformance to a federation protocol that this profile does not specify.

7. **Cross-boundary workflow handoff.** Governance instance A delegates a workflow to governance instance B. Each instance records its locally authoritative workflow identity, identity model, counterpart reference and durable handoff binding. With both evidence fragments, a reviewer can reconstruct the boundary crossing. With either fragment alone, a reviewer can identify the counterpart reference, the declared reconstruction model and what additional evidence or cooperation is required.
8. **Cross-boundary revocation propagation.** Governance instance A revokes authority before B commits. In the reachable variant, B observes the revocation, prevents commit and records the source, observation time and disposition of reserved authority. In the unavailable variant, B cannot observe or verify the revocation state because the declared cooperation mechanism is unavailable; B records continued authorization and propagation as unverified rather than claiming success.

# Limits

This profile does not require organizations to share raw prompts, data or internal policy. It does not choose a universal retention window or define the cross-organizational cooperation and reconciliation protocol used to bind identities, reconcile cumulative state, distribute revocations, create joint attestations or resolve disputes. That protocol is a separate specification effort that this evidence profile enables but does not contain.

Negotiation, acceptance criteria, payment or other reciprocal settlement, dispute handling and terminal completion semantics are likewise separate specification efforts. The reserved lifecycle names prevent `executed` from being treated as proof that those obligations were discharged while leaving their semantics to an explicit extension.

This profile does not prove that every statement inside a receipt is true, and it does not replace independent production, temporal anchoring or chain-of-custody evidence.

The profile establishes a narrower property: a reviewer can determine whether individually governed actions composed into an aggregate outcome, which authority and cumulative state were used, and where the observed trajectory diverged from the governed one.
