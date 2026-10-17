# Candidate Evidence Template for Operators Without a Security Operations Center

Candidate for review. Addresses #22.

This document gives an operator without a security operations center a minimum evidence bundle it can produce on its own, and that a receiver can check without the operator's vendors or any hosted service. It defines the records, the evidence states, a checking procedure, five negative controls and a complete synthetic example. It does not define a transport, a storage service, a retention period or a reporting duty. It does not establish SAFE adoption or legal sufficiency.

The minimum bundle and the five negative controls follow the list @DmitrL-dev proposed in #22, and the tiering follows @wl6adams's proposal there.

This is template version `osaa-discussion-22-evidence/0.1-candidate`. A revision takes a new identifier, and earlier identifiers keep their meaning.

# Who This Is For

An operator that holds its own signing key and has no security team: an individual, or an organization of a few people running agents. The operator scales its own effort to its size, the consequence it declares and its deployment context. The meaning of each evidence state stays the same at every tier. An `unknown` from a one-person operator means what it means from a large one, and it stays `unknown`.

# Rules

1. **Self-contained.** A receiver can check a bundle with the bundle itself, the signer's published public key, and standard hashing and signature libraries. Hosting this template or any helper tool is optional. No check depends on a hosted service, a vendor account or a vendor verification endpoint.
2. **Explicit absence.** Every required slot appears in the manifest. A slot without its record carries a state and a reason. An empty or missing field never reads as complete.
3. **Separate action records.** Authorization, gate decision and observed effect are three records, each bound by digest to one action declared in the manifest. None stands in for another; an `allow` decision is no evidence that the action ran.
4. **A signature establishes attribution only.** A valid manifest signature shows that the holder of the signer key assembled these exact bytes, under the key-trust assumptions in the signer record. It does not make any record true, independent or complete, and it never changes a claim result.
5. **Derived bundles are new objects.** A redacted or otherwise transformed bundle gets its own `bundle_id`, manifest, signature and redaction receipt. It is never presented as the original signed bytes.
6. **Retention and disclosure are declared.** The manifest states the operator's retention period and intended audience. This template sets no universal duration and requires no public incident identifier.

# Evidence States

Each slot listed in the manifest carries one state.

| State | Meaning | Reason required |
| --- | --- | --- |
| `present` | The record is in the bundle, listed with its digest | No |
| `not_collected` | The operator did not capture the record | Yes |
| `unavailable` | The record was captured and is now lost or inaccessible | Yes |
| `withheld` | The record exists and was removed before sharing; the redaction receipt lists it | Yes |
| `not_applicable` | The record does not apply, for example when no gate sits in the action path | Yes |

The same states apply to a single field inside a record, written as an object with `state` and `reason`.

An `artifacts[]` entry whose state is not `present` carries exactly `slot`, `state` and `reason`. It omits `name`, `media_type`, `canonicalization`, `digest_alg` and `digest`, because there are no bytes in the bundle for them to describe. This holds for `withheld` too. The digest of a withheld record stays in the original manifest under the operator's custody, and the shared bundle does not repeat it: a digest of bytes the receiver cannot see checks nothing, and it can link this bundle to other reports.

A bundle is complete when every required slot is `present` or `not_applicable`. A slot in any other state makes the bundle incomplete, whatever its reason says. Complete describes coverage only. An incomplete bundle is still well formed, and its claims resolve as the tables below say.

Each claim stated in the manifest resolves to one result.

| Result | Meaning |
| --- | --- |
| `supported` | Every record the claim relies on is `present`, matches its digest, names the same action and passes the claim's checks |
| `not_supported` | A record the claim relies on is `present` and fails a check: a digest mismatch, a different action, a `deny` decision, or times out of order; or the declared action its records name fails the step 4 digest check |
| `unknown` | A record the claim relies on is in any state other than `present`, or its slot is missing from the manifest |

A transfer resolves separately to `accepted`, `rejected`, `sent_not_acknowledged` or `unknown`. See the transfer acknowledgment below.

# Minimum Bundle

Field names are descriptive. Any open representation that preserves the same properties will do. The example uses JSON records canonicalized with RFC 8785 (JSON Canonicalization Scheme) and hashed with SHA-256. A non-JSON artifact is hashed over its raw bytes, with `canonicalization` set to `none`.

## Manifest

The example declares one action. With several, the three action slots repeat per action and carry the action id, for example `gate_decision:A2`.

| Field | What it proves | What it does not prove |
| --- | --- | --- |
| `template`, `bundle_id`, `manifest_version`, `created_at` | Which template version and which bundle a receiver is reading | That this is the only or latest bundle the operator produced |
| `tier`: `operator_size`, `declared_consequence`, `deployment_context` | The context the operator used to scale its own effort | That the declaration is accurate |
| `retention`, `disclosure` | The operator's stated retention period and intended audience | That the operator keeps to them |
| `actions[]`: `id`, the action object, its digest | The one action that the authorization, decision and effect records must all name | That the agent took no other action |
| `artifacts[]`: `slot`, `state`, `reason`, and for a `present` slot `name`, `media_type`, `canonicalization`, `digest_alg`, `digest` | Exactly which bytes each record had when the operator signed, and which slots are empty and why | That any record is accurate, or that the operator captured everything relevant |
| `claims[]`: `id`, `statement`, `relies_on` | What the operator asserts, and which records a receiver checks for each assertion | Anything outside those records; an unlisted claim has no support in the bundle |
| `signature` | The holder of the signer key signed these exact manifest bytes | Independent observation, or the truth of any record |

## Scope Record

| Field | What it proves | What it does not prove |
| --- | --- | --- |
| `system_id`, `system_version` | Which agent build, as the operator names it, took the actions | That the name is unique outside the operator's trust domain |
| `model_ref`, `tool_ids`, `policy_ref` with its digest | Which configuration versions the operator says were in use | That those versions were the ones loaded at run time |
| `run_id`, `event_order` | How the operator orders events, so records can be compared | A trusted clock; all times are the operator's own |
| `observation_gaps[]` | What the operator knows it did not capture | That nothing else is missing |

## Authorization Record

| Field | What it proves | What it does not prove |
| --- | --- | --- |
| `action`: id and digest | Which declared action this authorization covers | That the action ran |
| `principal` | On whose behalf the action was proposed | That the principal agreed to this specific action, unless `human_approval` shows it |
| `authorizer`: kind and reference, such as a policy rule, a person or a delegated grant | What the operator says granted permission | That the authorizer held the authority to grant it |
| `scope`, `policy_ref` | The permitted action set as written at the time | That the policy was correct or complete |
| `issued_at`, `expires_at` | The window the authorization claims | A trusted clock |
| `human_approval`: a reference, or a state with reason | Whether a person approved, and where that approval is recorded | The approver's identity beyond what the reference itself shows |

## Gate Decision Record

| Field | What it proves | What it does not prove |
| --- | --- | --- |
| `action`: id and digest | Which action the gate decided | That the gate saw every action the agent attempted |
| `gate`: id and version | Which enforcement component, as the operator names it, decided | That the agent could not bypass the gate |
| `authorization_ref`: digest | Which authorization record the gate evaluated | That the gate evaluated it correctly |
| `decision` (`allow`, `deny`, `require_approval` or `error`), `decided_at`, `sequence` | What the gate recorded, when, and in what order | That the action then ran |

## Observed Effect Record

| Field | What it proves | What it does not prove |
| --- | --- | --- |
| `action`: id and digest | Which action the effect belongs to | That no other effect occurred |
| `outcome` (`effect_observed` or `no_effect_observed`), `effect` | What the observer recorded as the consequence | That the action alone caused it |
| `observer`: id, and `relation` of `operator_controlled` or `independent` | Who observed it, and whether the operator controls that observer | Independent observation, when the relation is `operator_controlled` |
| `receipt`: kind, status, digest of the external response | That the operator holds a response with this digest | That the counterparty would confirm it |
| `observed_at`, `sequence` | Order relative to the gate decision | A trusted clock |

## Signer Record

| Field | What it proves | What it does not prove |
| --- | --- | --- |
| `signer_id`, `trust_domain` | The key's name inside the operator's trust domain | That the same name means the same party in another domain |
| `algorithm`, `public_key`, `key_publication` | Which key verifies the manifest, and where the operator publishes it | Who holds the key; the receiver matches the key against a publication it already trusts |
| `custody`: holder, storage, and whether the agent can use the key | The operator's stated custody model | That the custody model held during the run |
| `key_status_basis`: method, reference, status at signing, time checked | How a receiver can learn whether the key was valid when it signed | Current status; a later revocation does not silently reinterpret an earlier bundle |
| `previous_keys[]` | The rotation history needed to read older bundles | Anything about keys the operator did not list |

## Redaction Receipt

A bundle shared in full lists this slot as `not_applicable` with the reason `no transformation`.

| Field | What it proves | What it does not prove |
| --- | --- | --- |
| `input_ref`: a digest, or a state with reason | Which bundle this one came from, or why that link stays private | The content of the input |
| `method`, `effect` (`lossless`, `lossy` or `redacting`) | How the bundle changed | That the method was applied as described, beyond what the output shows |
| `removed[]`: `slot`, `reason`, and `field` only when one field came out | Exactly which records or fields came out | What they contained |
| `claims_still_verifiable[]`, `claims_no_longer_verifiable[]` | Which stated claims a receiver can still check from this bundle | That the removed material would have supported any claim |
| `original_held_by` | Who keeps the original under private custody | That the original still exists |

An entry that removes a whole record names `slot` and `reason` and carries no `field`. An entry that removes one field inside a record names `slot`, `field` and `reason`. The matching `artifacts[]` entry carries state `withheld`; its `reason` may repeat the receipt's text or say less.

A shared bundle may withhold the original's digests where they would let a reader guess content or link reports. The receipt then says so in `input_ref`.

## Transfer Acknowledgment

The receiver signs the acknowledgment after the bundle exists, so the sender keeps it beside the bundle, outside the manifest.

| Field | What it proves | What it does not prove |
| --- | --- | --- |
| `bundle_id`, `manifest_digest` | Exactly which signed manifest the receiver took | That the receiver read it or agrees with it |
| `receiver`: id, trust domain, public key | Who acknowledged | That the receiver is the intended party, unless the key matches the receiver's own publication |
| `outcome` (`accepted` or `rejected`), `accepted_at` | That the receiver stated it durably stored those bytes, or refused them | That the receiver still holds them |
| `signature` | The receiver key signed the canonical form of this acknowledgment with the `signature` member removed | Anything about the bundle's contents |

A sender log, a queue acknowledgment or an HTTP success status shows only that the sender's own step completed. Without a receiver-signed acknowledgment that names this manifest's digest, the transfer state is `sent_not_acknowledged`. A fuller custody receipt can stand in for this record.

# How a Small Operator Fills This In

1. Write the three tier lines: your size, the consequence you declare, and your deployment context. They scale your effort and never change what a state means.
2. Declare each action you are reporting once in `actions[]`, and hash it.
3. For each action, fill three records: what authorized it, what your gate decided, and what you observed afterward. If no gate sits in your action path, list `gate_decision` as `not_applicable` with that reason. If you did not log the result, list `observed_effect` as `not_collected`. Both are honest answers. The bundle is incomplete, and the claims that need those records resolve `unknown`.
4. Fill the signer record once and reuse it: your public key, where you publish it, who and what can use the private key (say whether the agent itself can), and how a reader learns of a rotation or revocation.
5. State only claims you can point to records for, and name those records in `relies_on`.
6. Hash each record, list it in the manifest with its state, and sign the manifest. Any SHA-256 tool and any Ed25519 or comparable signing tool will do.
7. Before sharing, if you remove anything, build a new bundle with its own `bundle_id` and signature, plus a redaction receipt. Keep the original under your own custody for the retention period you declared.
8. Send the bundle and keep the receiver's signed acknowledgment beside it. If none comes back, your transfer state is `sent_not_acknowledged`.
9. Once, before relying on your tooling, run the five negative controls through it. If any control comes out `supported` or `accepted`, fix the tooling first.

You do not need a security operations center, a hosted service, a vendor account, a public incident identifier or a particular retention period.

# Checking a Bundle

Checks below use the canonicalization the manifest declares. The example declares RFC 8785 and SHA-256.

1. **Attribution.** Verify `signature` over the canonical form of the manifest with the `signature` member removed, using the key in the signer record, and match that key against the operator's publication. Record `attributed` or `unattributed`.
2. **Structure.** Confirm that every required slot is listed: `scope`, `authorization`, `gate_decision`, `observed_effect`, `signer` and `redaction_receipt`. An unlisted slot, a state other than `present` without a reason, a non-`present` entry that carries `name`, `media_type`, `canonicalization`, `digest_alg` or `digest`, or a derived bundle that reuses an earlier `bundle_id` is a structural error. Claims relying on an unlisted slot resolve `unknown`.
3. **Digests.** Recompute each `present` record's digest over its canonical bytes. A mismatch makes every claim relying on that slot `not_supported`.
4. **Actions.** Recompute each declared action's digest from its action object. A mismatch makes every claim `not_supported` whose relied-on records name that action id, since those records are bound to an action the manifest misstates.
5. **Claims.** Evaluate each claim against only the records in its `relies_on`, using its checks.
6. **Receipt.** A claim listed in `claims_still_verifiable` that does not resolve `supported`, and that relies on a `withheld` slot, is a receipt inconsistency.
7. **Transfer.** An acknowledgment counts only if its `signature` verifies with the receiver's key over the canonical form of the acknowledgment with the `signature` member removed, and its `manifest_digest` equals the digest of the canonical form of the whole manifest, signature included.

The attribution result from step 1 never changes a result from steps 2 to 7.

# Negative Controls

Each control starts from the synthetic example below, makes the stated change, and re-signs every new or changed manifest with the same test key, so the manifest signature is valid in all five. A checker passes a control only when it reports the expected result despite that valid signature.

| Control | Change from the example | Expected result | The checker fails if |
| --- | --- | --- | --- |
| N1. Missing authorization | Remove `authorization.json`. List the slot as `not_collected`, reason `gate log rotated before export`. | C1 `unknown`. C2 and C3 `supported`. | C1 resolves `supported`, or the bundle is reported complete. |
| N2. Gate decision for a different action | In `gate_decision.json`, keep the id `A1` and set `action.digest` to the digest of the same request against ticket 4412, `bf4bb17923224e9cf23e4268afa5129cb35d930cb1b7d045716cab37bb92ef01`. Update the manifest's digest for that record. | C1 and C2 `not_supported`, for an action mismatch. C3 `supported`. | C1 or C2 resolves `supported` because an `allow` decision exists somewhere in the bundle. |
| N3. No observed effect | Remove `observed_effect.json` and list it as `not_collected`, reason `agent exited before the response was logged`. With nothing redacted, list `redaction_receipt` as `not_applicable`, reason `no transformation`. | C3 `unknown`. C1 and C2 `supported`. | C3 resolves `supported`, or any output treats the `allow` decision as evidence that the action ran. |
| N4. Redaction removes evidence a stated claim needs | Derive a new bundle with `bundle_id` `bundle:operator.example/2026-10-04/0002-shared`, all other manifest fields unchanged. Remove `gate_decision.json` and list the slot as `withheld`, reason `withheld pending internal review`. Append `{"slot": "gate_decision", "reason": "withheld pending internal review"}` to the receipt's `removed[]`, leave C1 and C2 in `claims_still_verifiable`, and update the manifest's digest for the receipt. | C1 and C2 `unknown`. Receipt inconsistency reported for C1 and C2. C3 `supported`. | C1 or C2 resolves `supported`, the inconsistency goes unreported, or reusing the example's `bundle_id` raises no structural error. |
| N5. Receiver never durably acknowledged | Bundle unchanged. The sender holds only its own log line, `HTTP 202 from intake.vendor.example`, and no `transfer_ack`. | Transfer `sent_not_acknowledged`. Claims unchanged. | The transfer reads `accepted` on the strength of the sender log or a transport status. |

The ticket 4412 action object in N2 is `{"method": "POST", "target": "https://api.vendor.example/v1/tickets/4412/close", "project": "P-17"}`.

Variants worth running beside the five:

* N1, with the `authorization` slot dropped from `artifacts[]` entirely: a structural error, and C1 resolves `unknown`.
* N2, with the manifest's A1 action object changed to the ticket 4412 object and the declared digest left as is: a step 4 mismatch, and C1, C2 and C3 `not_supported`.
* N3, with `observed_effect.json` kept and its `outcome` set to `no_effect_observed`: C3 resolves `not_supported`.
* N5, with an acknowledgment whose `manifest_digest` names a different manifest: it counts as no acknowledgment.
* Tier check: rerun N1 with `declared_consequence` set to `high`. No result may change.

# Synthetic Example

A one-person operator runs one agent whose outbound HTTPS calls pass through a local policy gate. On 2026-10-03 the agent closed ticket 4411 in the operator's project P-17 on a third-party ticketing service, `api.vendor.example`. The service's owner asked what authorized the change. The operator shares a bundle derived from its private original, with the ticket title removed as third-party content, and the owner's intake acknowledges it. All names use the reserved `.example` domain.

Expected results: `attributed`; C1, C2 and C3 `supported`; no receipt inconsistency; transfer `accepted`.

Claim checks used in this example:

* **C1** relies on `authorization` and `gate_decision`. Both name A1's digest, the gate's `authorization_ref.digest` equals the authorization record's digest, and `issued_at <= decided_at < expires_at`.
* **C2** relies on `gate_decision`. It names A1's digest and its `decision` is `allow`.
* **C3** relies on `observed_effect`. It names A1's digest and its `outcome` is `effect_observed`.

Notes:

* The operator signs with the RFC 8032 section 7.1 TEST 1 key and the receiver with the TEST 2 key. Both are published test keys; never use them for real evidence. Ed25519 signatures are deterministic, so anyone who re-signs a control with the same key gets the same bytes.
* Parse each block and serialize it per RFC 8785 before hashing or verifying. Whitespace in the blocks does not matter.
* `policy_ref.digest` and `receipt.body_digest` name files the operator holds outside the bundle. The bundle alone cannot check them, and no stated claim relies on them.
* The SHA-256 of the RFC 8785 form of the full manifest, signature included, is `6d354dc8145bab9067aab3ce3c4f3d1ae69536ddb0cc8fee0c3ba7e3bf889b25`. The acknowledgment names this value.

**scope.json**

```json
{
  "record": "scope",
  "system_id": "agent:operator.example/ticket-helper",
  "system_version": "1.4.2",
  "model_ref": "model:example-model/2026-09-01",
  "tool_ids": ["tool:http-client/3.1.0"],
  "policy_ref": {
    "id": "policy:operator.example/outbound",
    "version": "7",
    "digest_alg": "sha-256",
    "digest": "9ff3bc7d95c6d70f1b2bd5bd83b62f58f9712068795eee339c4e9555a5409dbf"
  },
  "run_id": "run-2026-10-03-0042",
  "event_order": "per-run sequence number assigned by the gate",
  "observation_gaps": ["model reasoning text not retained", "no network packet capture"]
}
```

**authorization.json**

```json
{
  "record": "authorization",
  "action": {
    "id": "A1",
    "digest_alg": "sha-256",
    "digest": "6878dd3e9ebebd804b4f643b368ec0328c56b37b363a44a9cdd7c3d4482752cc"
  },
  "principal": "operator:operator.example/owner",
  "authorizer": {"kind": "written_policy", "ref": "policy:operator.example/outbound#rule-3"},
  "scope": "close tickets in project P-17 on api.vendor.example",
  "policy_ref": {
    "id": "policy:operator.example/outbound",
    "version": "7",
    "digest_alg": "sha-256",
    "digest": "9ff3bc7d95c6d70f1b2bd5bd83b62f58f9712068795eee339c4e9555a5409dbf"
  },
  "issued_at": "2026-10-03T14:00:00Z",
  "expires_at": "2026-10-03T18:00:00Z",
  "human_approval": {"state": "not_applicable", "reason": "rule-3 does not require approval"}
}
```

**gate_decision.json**

```json
{
  "record": "gate_decision",
  "action": {
    "id": "A1",
    "digest_alg": "sha-256",
    "digest": "6878dd3e9ebebd804b4f643b368ec0328c56b37b363a44a9cdd7c3d4482752cc"
  },
  "gate": {"id": "gate:operator.example/outbound", "version": "2.0.1"},
  "authorization_ref": {
    "digest_alg": "sha-256",
    "digest": "fa9b1e9f43d97d4b035b51ef1d077a5fd8777f9aec85410163a49d1b54a43d55"
  },
  "decision": "allow",
  "decided_at": "2026-10-03T14:02:11Z",
  "sequence": 118
}
```

**observed_effect.json**

```json
{
  "record": "observed_effect",
  "action": {
    "id": "A1",
    "digest_alg": "sha-256",
    "digest": "6878dd3e9ebebd804b4f643b368ec0328c56b37b363a44a9cdd7c3d4482752cc"
  },
  "outcome": "effect_observed",
  "effect": "ticket 4411 in project P-17 reported state closed",
  "ticket_title": {"state": "withheld", "reason": "third-party content", "see": "redaction_receipt"},
  "observer": {"id": "agent:operator.example/ticket-helper", "relation": "operator_controlled"},
  "receipt": {
    "kind": "http_response",
    "status": 200,
    "body_digest_alg": "sha-256",
    "body_digest": "3fde6dd47ca3594ef7a443966e7176ce723ff83944894bf4e79319a0ce557453"
  },
  "observed_at": "2026-10-03T14:02:12Z",
  "sequence": 119
}
```

**signer.json**

```json
{
  "record": "signer",
  "signer_id": "key:operator.example/2026-1",
  "trust_domain": "operator.example",
  "algorithm": "ed25519",
  "public_key": "d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a",
  "key_publication": "https://operator.example/keys/2026-1.txt",
  "custody": {"holder": "the operator", "storage": "hardware token", "agent_can_use_key": false},
  "key_status_basis": {
    "method": "operator-published status file",
    "ref": "https://operator.example/keys/status.txt",
    "status_at_signing": "active",
    "checked_at": "2026-10-04T09:29:00Z"
  },
  "previous_keys": []
}
```

**redaction_receipt.json**

```json
{
  "record": "redaction_receipt",
  "input_ref": {
    "state": "withheld",
    "reason": "original bundle digest kept private; the original holds third-party content and its digest could link this bundle to other reports"
  },
  "method": "field removal",
  "effect": "redacting",
  "removed": [
    {"slot": "observed_effect", "field": "ticket_title", "reason": "third-party content not needed for any stated claim"}
  ],
  "claims_still_verifiable": ["C1", "C2", "C3"],
  "claims_no_longer_verifiable": [],
  "original_held_by": "the operator, under its declared retention period"
}
```

**manifest.json**

```json
{
  "template": "osaa-discussion-22-evidence/0.1-candidate",
  "bundle_id": "bundle:operator.example/2026-10-04/0001-shared",
  "manifest_version": 1,
  "created_at": "2026-10-04T09:30:00Z",
  "tier": {
    "operator_size": "one person",
    "declared_consequence": "low: one write to a third-party service, reversible by its owner",
    "deployment_context": "one operator, one agent, outbound HTTPS through a local policy gate"
  },
  "retention": {"period": "P2Y", "basis": "operator choice"},
  "disclosure": {
    "audience": ["vendor.example"],
    "public_incident_id": {"state": "not_applicable", "reason": "no public identifier requested"}
  },
  "actions": [
    {"id": "A1", "action": {"method": "POST", "target": "https://api.vendor.example/v1/tickets/4411/close", "project": "P-17"}, "digest_alg": "sha-256", "digest": "6878dd3e9ebebd804b4f643b368ec0328c56b37b363a44a9cdd7c3d4482752cc"}
  ],
  "artifacts": [
    {"slot": "scope", "name": "scope.json", "media_type": "application/json", "canonicalization": "RFC 8785", "digest_alg": "sha-256", "digest": "9ba886089b8a7bd2a4fd1e83f367d78db2e6455bcaf6fa7471eaa0257a3655f7", "state": "present"},
    {"slot": "authorization", "name": "authorization.json", "media_type": "application/json", "canonicalization": "RFC 8785", "digest_alg": "sha-256", "digest": "fa9b1e9f43d97d4b035b51ef1d077a5fd8777f9aec85410163a49d1b54a43d55", "state": "present"},
    {"slot": "gate_decision", "name": "gate_decision.json", "media_type": "application/json", "canonicalization": "RFC 8785", "digest_alg": "sha-256", "digest": "5dfbccf76613909c3c46d1e46fcd4b8ec94dade045081365813661ddf9c0b5d1", "state": "present"},
    {"slot": "observed_effect", "name": "observed_effect.json", "media_type": "application/json", "canonicalization": "RFC 8785", "digest_alg": "sha-256", "digest": "b7b80edb59ee5f5f33f690a9dea65b88e79d4d17a663e00966a9c8d400918989", "state": "present"},
    {"slot": "signer", "name": "signer.json", "media_type": "application/json", "canonicalization": "RFC 8785", "digest_alg": "sha-256", "digest": "61fcd8519b173ee9896501f14f596b96f70daa5f4dfff2f9f70f86f57dc4f449", "state": "present"},
    {"slot": "redaction_receipt", "name": "redaction_receipt.json", "media_type": "application/json", "canonicalization": "RFC 8785", "digest_alg": "sha-256", "digest": "d95e3b77c4237e597106b6812c9ceab595d9f22103934a0e3a1cdab7f30e6521", "state": "present"}
  ],
  "claims": [
    {"id": "C1", "statement": "Action A1 was authorized before the gate decided it", "relies_on": ["authorization", "gate_decision"]},
    {"id": "C2", "statement": "The gate allowed action A1", "relies_on": ["gate_decision"]},
    {"id": "C3", "statement": "An effect of action A1 was observed and recorded", "relies_on": ["observed_effect"]}
  ],
  "signature": {
    "alg": "ed25519",
    "key": "key:operator.example/2026-1",
    "value": "a2c38bbffb9456d8aa146b4f856538f7de621f9c14bada371e88f4e3996d8d9270014bf213ffce56bf0ba633cd6fcdf4c3d549d235aa20f3005a17eef8ad0a06"
  }
}
```

**transfer_ack.json**, kept by the sender beside the bundle

```json
{
  "record": "transfer_ack",
  "transfer_id": "transfer:vendor.example/2026-10-04/17",
  "bundle_id": "bundle:operator.example/2026-10-04/0001-shared",
  "manifest_digest_alg": "sha-256",
  "manifest_digest": "6d354dc8145bab9067aab3ce3c4f3d1ae69536ddb0cc8fee0c3ba7e3bf889b25",
  "receiver": {
    "id": "key:vendor.example/intake-1",
    "trust_domain": "vendor.example",
    "public_key": "3d4017c3e843895a92b70aa74d1b7ebc9c982ccf2ec4968cc0cd55f12af4660c"
  },
  "outcome": "accepted",
  "accepted_at": "2026-10-04T09:41:07Z",
  "signature": {
    "alg": "ed25519",
    "value": "0a4b4f657b9b52a2f917052d0fcba4c1959db82f27c39c06d93c8dd0c818804e0c1ed18c681dc56341a6c445a33ca7b5f0d807f786bb3bd2ef1a8dc4f1697802"
  }
}
```

# Limits

This template does not decide whether an incident is reportable, whether an operator met any reporting or framework duty, or whether its evidence is legally sufficient. A bundle signed by an operator about its own agent is attributable evidence from an interested party, and reviewers should weigh it that way. The observer `relation` is the only field that speaks to independence, and it is a declaration.

The template covers one operator's evidence for a bounded set of actions. Memory export, scoping across projects and multi-party custody chains are out of scope.
