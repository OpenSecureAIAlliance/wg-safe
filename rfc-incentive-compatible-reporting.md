# RFC: Incentive-Compatible Internal Reporting as a Precondition for the SAFE Compact

## Summary 
SAFE's Disclosure Model begins at the point at which an organization has already recognized an incident and chosen to escalate it as a "Confidential rapid alert."  This RFC addresses the step before that: whether the individual who first observes a failure has any structural reason to report it internally at all. Without this layer, every downstream commitment in SAFE (de-identification, non-punitive review, the reporting compact, etc.) has nothing to act on, because the observation never surfaces.

## Why it fits SAFE rather than being a general governance proposal

SAFE's Guiding Principles already state that "learning is separate from enforcement" and commit to "non-punitive treatment of honest mistakes." Those principles describe how a report should be *handled once made*. They do not address whether it *gets* made. The gap is structural, not aspirational: AI-attributable efficiency gains are typically credited to the business unit that deployed the system; AI-attributable degradation is slow, diffuse, and rarely attributable to any one person. In most current organizational structures, an employee who identifies a real failure mode is volunteering evidence against their own team's stated result, usually with no mechanism protecting them for doing so. This holds even where SAFE's third-party reporting compact is fully implemented, because the compact governs what happens *after* an organization decides to report, not whether an individual inside it surfaces the observation in the first place.

## Proposed additions

**To Guiding Principles:**

> **Reporting incentives are separate from reporting handling.** An organization's ability to honor SAFE's non-punitive review commitments depends on whether individuals inside that organization have a structural reason to surface an observation in the first place. Member organizations should ensure that the function that benefits from an AI deployment is not the sole route through which risks and degradation associated with that deployment are escalated, and that personnel who identify a near-miss have access to a reporting channel independent of the function responsible for the deployment.
> 

**To the Review Framework**, a scoping note distinguishing this from Issue #34's independence concern:

> *A Note on internal vs. external independence:* Independence of findings (#34) addresses conflicts of interest between organizations, including assessors, vendors, or insurers with a stake in an outcome. A related but distinct condition exists *within* a reporting organization: the individual who observes a failure and the function that would be implicated by reporting it are often not independent of each other. Where this internal independence does not exist, an organization may fully honor SAFE's external reporting compact while systematically failing to generate reports internally.
> 

**To "From Lessons to Controls":**

> A member organization's SAFE-facing reporting process should be able to demonstrate: (a) that the organizational function claiming benefit from a given AI deployment is not the sole party responsible for escalating its risks, and (b) that personnel who identify a near-miss have access to a reporting route that does not require disclosing their identity to that function.
>

## Relationship to open issues

This builds on the scope concern in #21 (first-party harm and acts of omission are structurally under-reported) by identifying a specific mechanism for why: omissions and first-party failures carry the weakest reporting incentive precisely because no external party is harmed and no external trigger exists. It is scoped separately from #34 (independence between organizations, not within one), and is intentionally agnostic to whichever incident taxonomy SAFE ultimately adopts (MITRE ATLAS, OECD, or otherwise). This proposal concerns the organizational pipeline that feeds a taxonomy, not the taxonomy itself.

## What this RFC does not propose

This RFC does not specify a technical reporting mechanism, logging architecture, or enforcement system, but only the organizational precondition any such system depends on to receive real input. Implementation is left to member organizations.

## Disclosure

The reporting-incentive argument above draws on Prewitt, "Institutionalizing Trust: HEVIDS and Reverse Game Theory as a Sociotechnical Intervention for Enterprise AI Alignment," SSRN 6915218 (2026). I maintain HEVIDS (hevids.org), an open (CC BY-SA 4.0) standard for enterprise AI governance; this work focuses on its Discernment and Safeguards functions. This proposal is intentionally scoped to organizational preconditions independent of any implementation.

AI disclosure: drafted with AI-assisted editing; the argument and organizational judgments are my own.

---

#### Signed-off-by: Anderson D. Prewitt <adp@dradpa.com>
