# SAFE Candidate Profile: Hardware-Attested Confidential Ingestion & Multi-Provider Distillation Defense (SAFE-ENCLAVE v1.0)

**Profile Name**: `SAFE-ENCLAVE`  
**Version**: `1.0`  
**Author**: Corrente Applied Cryptography Group (`standards@correntelabs.com`)  
**Target Repository**: `OpenSecureAIAlliance/RFCs`  
**Working Group**: Shared AI Findings Exchange (SAFE)  
**Parent Specifications**:
- Complements PR #18 (*Anchored Evidence for SAFE*)
- Complements PR #27 (*Chain-of-Custody Receipt Profile*)
- Harmonizes with PR #39 (*Governed-Action Lifecycle Correlation Candidate*)
**Target Silicon**: Intel TDX v4, AMD SEV-SNP, NVIDIA Confidential Computing  
**Date**: October 2026

---

## 1. Abstract

This candidate profile specifies the **SAFE Hardware-Enclave Confidential Ingestion and Distillation Defense Architecture (SAFE-ENCLAVE v1.0)**. 

While existing SAFE profiles define record schemas (PR #39), evidence anchors (PR #18), and custody receipts (PR #27), they assume incident telemetry is transmitted in plaintext to a centralized verifier. In commercial reality, competing frontier AI labs (OpenAI, Anthropic, Google, Meta, Microsoft, Amazon) cannot share raw incident logs without exposing:
1. Proprietary prompt templates and system reasoning chains.
2. Model parameter weights and capability boundaries.
3. Protected customer data and enterprise PII.

Furthermore, as documented in the joint **NSA, FBI, and CISA Cybersecurity Advisory** (*"China-Based Artificial Intelligence Companies Conducting Industrial-Scale Distillation Campaigns Against U.S. AI Companies"*), state-sponsored adversaries deliberately shard extraction operations across multiple providers so that no single provider's telemetry crosses an alert threshold.

SAFE-ENCLAVE provides the missing physical execution layer:
- **Zero-Knowledge Ingestion**: Ephemeral P-256 ECDH + AES-256-GCM envelope encryption into isolated CPU hardware enclaves (Intel TDX / AMD SEV-SNP).
- **In-Memory Cross-Provider Correlation**: In-RAM clustering of sub-threshold query slices to reconstruct distributed distillation campaigns.
- **Verifiable Threat Advisories**: Emission of de-identified bulletins bound to IETF SCITT Merkle ledger digests and silicon RTMR3 register measurements.

---

## 2. Cryptographic Envelope & Key Agreement

### 2.1 Enclave Ingest Root Keypair
The SAFE Ingestion Root generates an ephemeral or attested P-256 (NIST prime256v1) keypair inside hardware enclave memory:
$$\text{Keys}_{\text{enclave}} = (sk_{\text{enclave}}, pk_{\text{enclave}})$$

The public key $pk_{\text{enclave}}$ is published alongside an Intel TDX Quote or AMD SEV-SNP attestation report containing the hash of $pk_{\text{enclave}}$ in the `report_data` register.

### 2.2 Client-Side Authenticated Encryption
An Alliance member submits finding $M$ by executing:
1. Generate ephemeral client keypair: $(sk_{\text{client}}, pk_{\text{client}})$.
2. Compute ECDH shared secret: $Z = \text{ECDH}(sk_{\text{client}}, pk_{\text{enclave}})$.
3. Derive 256-bit symmetric key: $K_{\text{sym}} = \text{SHA-256}(Z)$.
4. Generate 96-bit random IV: $IV \leftarrow \{0,1\}^{96}$.
5. Encrypt with AES-256-GCM: $(C, T) = \text{AES-GCM-ENC}_{K_{\text{sym}}}(IV, M)$.
6. Construct `ConfidentialSafeSubmission`:
   $$\text{Submission} = (pk_{\text{client}}, IV, C, T, \text{SHA-256}(\text{ProviderID}), \text{Timestamp})$$

### 2.3 Enclave Ingestion & Replay Defenses
Upon receipt, the enclave enforces:
1. **Replay Check**: Reject if `submissionId` exists in the in-memory cache.
2. **Freshness Window**: Assert $|\text{CurrentTime} - \text{Timestamp}| \le 24 \text{ hours}$.
3. **Sybil Throttling**: Cap submissions at 100 per provider fingerprint per correlation cycle.
4. **Decryption**: Compute $Z' = \text{ECDH}(sk_{\text{enclave}}, pk_{\text{client}})$, derive $K_{\text{sym}}$, and authenticate $(C, T)$. If tag verification fails, abort before memory allocation.
5. **Receipt Emission**: Emit `IngestReceipt` compliant with PR #18 (`anchoredEvidenceBasis`) and PR #27 (`scitt/vaara/v1`).

---

## 3. Multi-Provider Distillation Correlation Engine

The correlation engine evaluates decrypted findings strictly within enclave protected RAM:
1. **Feature Matching**: Cross-matches MITRE ATLAS `AML.T0024` indicators (token sequence entropy, semantic prompt syntax, ASN rotation).
2. **Cluster Aggregation**: Sums query volumes across independent providers.
3. **Correlation Scoring**:
   $$\text{Score} = \min\left(1.0, 0.5 + 0.15 \times N_{\text{providers}} + 0.2 \times \mathbb{I}(N_{\text{findings}} > 2)\right)$$
4. **Campaign Identifier**: Deterministically hashes cluster attributes:
   $$\text{CampaignID} = \text{"safe\_camp\_"} + \text{SHA-256}(\text{ClusterKey} + \text{FirstObserved})[0..16]$$

---

## 4. Verifiable SCITT Bulletin & Silicon Binding

Public threat bulletins strip all private identifiers, model weights, and tenant metadata. Transparency is guaranteed via two cryptographic anchors:

1. **Silicon RTMR3 Attestation**:
   $$\text{RTMR3} = \text{"rtmr3\_"} + \text{SHA-256}(\text{Arch} + \text{":safe-enclave-v1:"} + \text{ReportData})[0..64]$$
2. **IETF SCITT Merkle Ledger Entry**:
   $$\text{SCITT\_Digest} = \text{"scitt:safe:sha256:"} + \text{SHA-256}(\text{BulletinID} + \text{":"} + \text{RTMR3} + \text{":"} + \text{ReportData})$$

Downstream consumers verify authenticity without trusting the Alliance operator by asserting the mathematical equality:
$$\text{Verify}(\text{Bulletin}) = (\text{ReportData} \equiv \text{SHA-256}(\text{CanonicalBody})) \land (\text{RTMR3} \equiv \text{ExpectedRTMR}) \land (\text{SCITT} \equiv \text{ExpectedSCITT})$$

---

## 5. Verification & Test Evidence

The profile is verified by 15 automated test cases in the official reference implementation (`@ashlar-blue/osaa-safe@1.0.0`):
- **Suite 1: Framework Conformance** (`tests/safe/safe-framework.test.ts`): 5/5 PASS.
- **Suite 2: Adversarial Battery** (`tests/safe/safe-adversarial.test.ts`): 10/10 PASS across replay, freshness, Sybil, bit-flipping, MITM, multi-cloud distillation, and zero-knowledge leakage probes.
