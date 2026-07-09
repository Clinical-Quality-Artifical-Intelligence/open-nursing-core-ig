<div align="center">

# 🧭 Standards & Governance Roadmap

**How the Open Nursing Core Implementation Guide moves from a pre-ballot community release to a formally endorsed standard**

</div>

---

## Where we are today

ONC-IG version 1.0.0 is a **trial-use, pre-ballot community release**. Concretely, that means:

- It has **not** been submitted to, or passed, formal standards balloting through HL7 International or any other standards development organisation (SDO).
- It has **not** undergone independent clinical or peer review beyond the project's own contributors.
- Its `status: active` / `releaseLabel: release` fields in `sushi-config.yaml` are **FHIR conformance codes describing this project's own development lifecycle** (i.e. "this is our current, non-draft working version"), not a claim of external endorsement.
- It is a **specification**, not a deployed product. It does not discharge an implementing organisation's own DCB0129/DCB0160 clinical-safety obligations, DSPT completion, or Data Protection Impact Assessment.

This document exists so that claim is never ambiguous, and so there is a concrete, checkable plan — not just an acknowledgement — for closing the gap. It is informational; publishing it does not itself constitute a submission to any standards body.

---

## Why this matters

An implementation guide that looks production-ready but hasn't been balloted or peer-reviewed creates real risk: an NHS trust, EHR vendor, or another health system could adopt profiles believing they carry more external assurance than they do. Two things must both be true before that risk is acceptable:

1. **The IG must say what it is, everywhere it is discoverable** (homepage, history page, README, `sushi-config.yaml` description) — done as part of this remediation pass.
2. **There must be a real path to closing the gap**, not just a disclaimer. That path is set out below.

---

## Parallel tracks

Formal endorsement for a nursing-process FHIR IG realistically runs on multiple tracks that can proceed **in parallel**, not in sequence — they have different sponsors, timelines and scope.

### Track A — PRSB formal assurance (UK-specific, more tractable near-term)

The IG already grounds its assessment/diagnosis/planning profiles in the **Professional Record Standards Body (PRSB) Nursing Care Needs standard**. PRSB runs a standards-assurance process for exactly this kind of artifact, and — because ONC-IG is explicitly UK/NHS-scoped — this is the more directly relevant and more achievable near-term endorsement route.

- [ ] Contact PRSB to scope what assurance would require for a FHIR IG that implements one of their standards (rather than proposing a new PRSB standard from scratch)
- [ ] Assemble a clinical reference group (nurses, practice educators, tissue-viability and safety leads) to support PRSB's clinical review requirements
- [ ] Submit for PRSB review once the reference group and any requested evidence base are in place

### Track B — HL7 International formal balloting (broader, longer-horizon)

HL7 balloting is the recognised route to a globally-portable FHIR standard, but it requires organisational sponsorship and is a multi-cycle process:

1. **Find a sponsoring Work Group.** An individual or organisation cannot submit an IG to ballot alone — it needs an HL7 Work Group co-sponsor. **Patient Care WG** is the most relevant home for nursing-process and care-plan content; this should be the first approach.
2. **Build implementation experience before balloting.** HL7 expects evidence that an IG has been tried by more than its own authors. The practical, low-barrier way to start this is:
   - [ ] Submit a track to an upcoming **HL7 FHIR Connectathon** (quarterly, open to non-members as participants) to get real implementers to build against the IG and report friction
3. **Draft and approve a Project Scope Statement (PSS)** with the sponsoring Work Group, defining what is and isn't in scope for ballot.
4. **Submit for Standard for Trial Use (STU) ballot.** This is the first formal ballot tier — it invites structured, recorded negative/affirmative votes from the HL7 ballot pool.
5. **Reconcile negative ballot comments.** Every substantive negative vote must be formally addressed (accepted, countered, or withdrawn) before the ballot can close — this is typically the most time-consuming step.
6. **Publish as STU**, gather real-world implementation experience (HL7 requires this for the next tier), then pursue **Normative** ballot once that evidence exists.

Realistically, Track B is a **multi-year** undertaking requiring sustained Work Group engagement — it should not block Track A or continued open development in the meantime.

### Track C — WHO / Open Health Stack ecosystem alignment (global reach + implementation evidence)

In July 2026 the **Open Health Stack Software Foundation (OHS-SF)** was established under the **Linux Foundation** (transferring Google's Open Health Stack, originally launched with WHO in 2023), and **WHO formally joined** to align the stack with WHO norms and its machine-readable **SMART Guidelines** ([smart.who.int](https://smart.who.int)). The foundation is community-governed with **no financial barrier to governance participation**, and is organised into three pillars: *FHIR Foundations* (offline-first FHIR SDKs), a *Reference Toolkit*, and an *AI Commons* for safe health AI.

This matters to ONC-IG for two reasons:

1. **It directly addresses our single-jurisdiction limitation.** The current standards base (PRSB, NEWS2, Equality Act 2010, UK GDPR) is UK-centric — flagged as Limitation #6 in the accompanying paper. Aligning with WHO SMART Guidelines authoring conventions and the OHS toolchain is the concrete route to global applicability, and nursing-process content is currently a **gap** in the SMART Guidelines / OHS content ecosystem that ONC is well placed to fill.
2. **It generates the real-world implementation evidence Track B requires.** HL7 expects an IG to have been implemented beyond its authors before balloting; OHS deployments (Ministries of Health, NGOs, startups across Sub-Saharan Africa and South Asia) are exactly that evidence base.

Concrete work items:

- [ ] **SDC Questionnaire representations** of core assessments (NEWS2, Monk Skin Tone, Braden, Waterlow, MUST, What Matters To Me) so they render in the OHS data-capture libraries ([android-fhir](https://github.com/ohs-foundation/android-fhir), [kotlin-fhir-data-capture](https://github.com/ohs-foundation/kotlin-fhir-data-capture)) — tracked in [issue #125](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/125)
- [ ] Align our CQL/PlanDefinition layer (NEWS2 scoring + escalation) with **WHO SMART Guidelines** L3 authoring conventions so ONC content is consumable alongside WHO-quality-assured content
- [ ] **Equity analytics example** using [fhir-data-pipes](https://github.com/ohs-foundation/fhir-data-pipes) (FHIR → Parquet → dashboard): pressure-ulcer detection timeliness stratified by Monk skin tone — operationalising the IG's "make inequity visible" claim
- [ ] Reference [fhir-gateway](https://github.com/ohs-foundation/fhir-gateway) on the Security & Privacy page as an open-source implementation option for the RBAC/audit conformance requirements
- [ ] Evaluate **ICD-11 mappings** for settings without a national SNOMED CT licence (SNOMED is licensed per-country; ICD-11 is free), so the IG degrades gracefully outside SNOMED member states
- [ ] Engage the **AI Commons** pillar for the Relational AI work — its safe-AI evaluation frameworks are a route to independent evaluation of the model claims currently flagged as internal-only (Limitation #7)
- [ ] Join the OHS **FHIR Foundations working group**; present ONC-IG at a monthly community call; propose nursing-process content as a foundation topic

- **NANDA-I licensing and terminology canonical.** The `onc-to-nanda` ConceptMap currently targets an explicit local placeholder (see `input/fsh/onc-terminology-mapping.fsh`) because NANDA-I is a proprietary, licensed terminology with no public FHIR canonical this project controls. Tracked in [issue #123](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/123). Any ballot or PRSB submission touching the diagnosis phase should either resolve this first or explicitly scope it out.
- **Independent clinical/peer review.** Separate from formal balloting, the clinical-safety and equity design claims in the accompanying academic paper are motivated by cited literature, not by a clinical pilot or usability study of this IG itself. A simulated or live nursing-documentation study (ADPIE-structured vs. conventional) is identified as future work in that paper and would materially strengthen either track's submission.

---

## Phased plan

| Phase | Timeframe | Actions |
|-------|-----------|---------|
| **Now** | Immediate | Trial-use disclaimers live across IG, README, history page ✅ · Open NANDA-I tracking issue ✅ · Fitzpatrick/Monk primary-vs-secondary language reconciled across FSH and docs ✅ |
| **Near-term** | 0–3 months | Contact PRSB to scope assurance requirements (Track A) · Identify and submit a Connectathon track (Track B, step 2) · Recruit clinical reference group volunteers · Join OHS Foundation Discord/mailing list and present ONC at a monthly community call (Track C) |
| **Medium-term** | 3–12 months | PRSB clinical review cycle · Approach Patient Care WG for PSS sponsorship (Track B, steps 1–3) · Resolve NANDA-I licensing (issue #123) · SDC Questionnaires for core assessments (issue #125) and fhir-data-pipes equity-analytics example (Track C) · Global Digital Health Forum, Bangkok, December 2026 |
| **Longer-term** | 12+ months | HL7 STU ballot submission and reconciliation · Usability/documentation-completeness study · Normative ballot once implementation evidence exists |

---

## How you can help

| I am a... | What's useful right now |
|-----------|--------------------------|
| **PRSB-connected clinician or informatician** | Help scope what PRSB assurance would need — [open a discussion](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/discussions) |
| **HL7 member / Work Group participant** | Advice on approaching Patient Care WG, or connecting us with a co-sponsor |
| **FHIR implementer** | Volunteer to build against the IG at a Connectathon |
| **NANDA-I licence holder or terminology specialist** | Comment on [issue #123](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/123) |
| **Nursing researcher** | Help design the documentation-completeness/usability study identified as future work |
| **Android/Kotlin developer or SDC author** | Build the OHS-compatible Questionnaires — [issue #125](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/125) |
| **Global-health implementer (MoH / NGO / startup)** | Pilot ONC nursing assessments in an [Open Health Stack](https://ohs.foundation) deployment and tell us what breaks |

See [CONTRIBUTING.md](CONTRIBUTING.md) for general contribution guidelines and [ROADMAP.md](ROADMAP.md) for the feature/profile roadmap (this document covers standards governance only).

---

<div align="center">

*This roadmap is a living document, reviewed alongside each release. To suggest changes, [open a discussion](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/discussions).*

</div>
