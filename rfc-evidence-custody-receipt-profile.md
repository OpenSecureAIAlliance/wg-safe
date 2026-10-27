# SAFE Chain-of-Custody Receipt Profile

This companion proposal defines the minimum properties needed to authenticate the handling history of an evidence item from collection through submission. It specifies evidence requirements and conformance behavior, not a transport, storage service or universal retention policy.

# Problem

A sender-side log can show that a transfer was attempted without establishing that the intended receiver durably accepted the evidence. A content hash can show that two parties hold the same bytes without establishing who collected, handled, transformed or accepted them. Temporal anchoring can show that bytes existed by a time without establishing custody.

SAFE therefore needs a linked receipt for each custody transition. The receipt must keep origin, integrity, transfer acceptance, transformation and temporal anchoring as separate claims that can be verified together.

# Minimum Record

The field names below are descriptive. Implementations may use any open representation that preserves the same properties.

## Evidence identity and origin

* An issuer-scoped `evidence_id`
* Payload digest and digest algorithm
* Schema and canonicalization identifiers for the bytes or structured object that were digested
* Origin system, collector and custodian identities, including the trust domain or contour in which each identity is meaningful
* Collection method, method version, collection time and available source attestation
* Observed artifact identity for the system that produced the evidence, when relevant
* Storage format, protection method, retention or disposition state and an access-control or access-audit reference

## Transfer receipt

* A unique `transfer_id` bound to the evidence ID and payload digest
* Sender and intended receiver identities and trust domains
* `sent_at` and durable `accepted_at` timestamps, without treating the former as proof of the latter
* The previous custody-receipt digest, or an explicit genesis state for the first receipt
* Transport and protection method identifiers sufficient to reproduce the verification decision without exposing credentials
* Signer and key identifiers plus a durable status or revocation reference
* Acceptance outcome: `accepted`, `rejected`, `unavailable` or `insufficient_evidence`
* A machine-readable reason when the outcome is not `accepted`

The receiver's durable, identity-bound acknowledgement establishes acceptance. A successful sender request, queue acknowledgement or transport delivery report establishes only that the sender or transport observed its own step.

## Transformation receipt

Redaction, normalization, extraction, compression, format conversion and aggregation create new evidence objects. Each transformation receipt must record:

* Input evidence IDs and payload digests
* Output evidence ID and payload digest
* Transformation method and version
* Actor, time and stated purpose
* Whether the transformation is lossless, lossy or redacting
* References to retained originals or an explicit reason they are unavailable

The transformed object receives its own custody chain. It does not inherit an unqualified claim that it is byte-identical to its inputs.

# Identity and Trust Boundaries

An identity is qualified by its issuer and trust domain. Matching email addresses, display names or locally assigned subject identifiers across organizations or regional contours do not establish that two custody actors are the same party.

Cross-domain identity equivalence requires an explicit, scoped, signed and revocable binding. A receipt should preserve the binding reference and the audience or purpose for which it was accepted. Revocation of the binding affects future transfers without rewriting receipts that were validly produced earlier.

# Behavioral Requirements

1. **Durable acceptance.** A sender marks a handoff complete only after receiving a durable acknowledgement bound to the receiver, transfer ID, evidence ID and payload digest.
2. **Idempotent transfer.** Retrying the same transfer does not create conflicting custody transitions. Repeated acknowledgements resolve to the same accepted receipt or an explicit conflict.
3. **Linked continuity.** Every non-genesis receipt references its predecessor. A missing or ambiguous predecessor is reported as a custody gap rather than silently repaired.
4. **Transformation transparency.** Every change to the evidence bytes creates a transformation receipt that binds input and output digests. Copying without byte changes may preserve the payload digest but still creates a custody transition.
5. **Key status.** Verification records the signing method, key identifier and the status evidence used to evaluate the key at signing or acceptance time. Current revocation alone must not silently reinterpret historical receipts.
6. **Fail-explicit availability.** The record distinguishes never provided, offered but not accepted, accepted and available, accepted then unavailable, and insufficient evidence.
7. **Independent properties.** Custody, content integrity, temporal anchoring, observed artifact identity and producer independence remain separately reportable. Success in one dimension must not be imputed to another.
8. **Data minimization.** A receipt need not contain the evidence payload. It should reveal only the metadata required to verify the custody claim, subject to the same access and disclosure constraints as the evidence itself.
9. **Custodian and access history.** Each custodian change, transformation, export or disposition creates a linked receipt. Read-only access may remain in a separately protected audit record, but the custody receipt must preserve a verifiable reference to the applicable access history or state that it is unavailable.

# Conformance Vectors

A conformant implementation should publish machine-runnable variants of at least these cases:

1. **Sender-only success.** The sender receives a successful transport response but no receiver acknowledgement. The result is offered or unavailable, not accepted.
2. **Accepted then lost.** The receiver durably acknowledges a digest and later cannot provide the payload. The chain reports accepted then unavailable rather than never provided.
3. **Idempotent retry.** The sender retries an identical transfer after losing the acknowledgement. The receiver returns the same accepted transition without creating a second custody event.
4. **Undeclared transformation.** The payload is redacted or normalized without a receipt binding input and output digests. Verification reports a custody gap even when the output has a valid hash.
5. **Cross-domain name collision.** Sender and receiver records contain the same email address or display name in different trust domains without a signed binding. Verification does not merge the identities.
6. **Broken predecessor.** A receipt refers to a missing or mismatched previous digest. Verification reports incomplete continuity and identifies the last valid transition.
7. **Historical key status.** A validly produced receipt is checked after the signing key is revoked. Verification reports the key status and evaluates the receipt against the declared historical-status method rather than silently accepting or rejecting it.
8. **Unreferenced access history.** A custodian provides a valid payload and transfer chain but no verifiable access history or declared unavailable state. Verification reports incomplete custody evidence rather than complete custody.

Each vector should declare the receipt schema and canonicalization version, starting custody state, expected transition, expected availability state and verification method. Simulated, replayed and live transfers must remain distinguishable.

# Relationship to Other Evidence Properties

Temporal anchoring can prove that a receipt or evidence digest existed by a stated time. It does not prove that the receiver accepted custody. A custody receipt can prove that a named receiver acknowledged a digest. It does not prove that the underlying statement is true or that the producer was independent of the party under review.

Observed artifact identity establishes which artifact produced or was evaluated by a record. It does not establish the record's handling history. SAFE reviewers should evaluate these properties together without collapsing them into one trusted or untrusted status.

# Limits

This profile does not prescribe one transparency log, public-key infrastructure, identity provider or evidence store. It does not require public disclosure of evidence or internal identity mappings. It does not make a reporting party trustworthy by declaration.

The profile establishes a narrower property: a reviewer can determine who claimed to collect, transfer, accept and transform an evidence item; which bytes each transition covered; and where the custody chain is complete, unavailable or insufficiently evidenced.
