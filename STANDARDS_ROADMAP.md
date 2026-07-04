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

## Two parallel tracks

Formal endorsement for a nursing-process FHIR IG realistically runs on two tracks that can proceed **in parallel**, not in sequence — they have different sponsors, timelines and scope.

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

---

## Dependencies that block full readiness regardless of track

- **NANDA-I licensing and terminology canonical.** The `onc-to-nanda` ConceptMap currently targets an explicit local placeholder (see `input/fsh/onc-terminology-mapping.fsh`) because NANDA-I is a proprietary, licensed terminology with no public FHIR canonical this project controls. Tracked in [issue #123](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/123). Any ballot or PRSB submission touching the diagnosis phase should either resolve this first or explicitly scope it out.
- **Independent clinical/peer review.** Separate from formal balloting, the clinical-safety and equity design claims in the accompanying academic paper are motivated by cited literature, not by a clinical pilot or usability study of this IG itself. A simulated or live nursing-documentation study (ADPIE-structured vs. conventional) is identified as future work in that paper and would materially strengthen either track's submission.

---

## Phased plan

| Phase | Timeframe | Actions |
|-------|-----------|---------|
| **Now** | Immediate | Trial-use disclaimers live across IG, README, history page ✅ · Open NANDA-I tracking issue ✅ · Fitzpatrick/Monk primary-vs-secondary language reconciled across FSH and docs ✅ |
| **Near-term** | 0–3 months | Contact PRSB to scope assurance requirements (Track A) · Identify and submit a Connectathon track (Track B, step 2) · Recruit clinical reference group volunteers |
| **Medium-term** | 3–12 months | PRSB clinical review cycle · Approach Patient Care WG for PSS sponsorship (Track B, steps 1–3) · Resolve NANDA-I licensing (issue #123) |
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

See [CONTRIBUTING.md](CONTRIBUTING.md) for general contribution guidelines and [ROADMAP.md](ROADMAP.md) for the feature/profile roadmap (this document covers standards governance only).

---

<div align="center">

*This roadmap is a living document, reviewed alongside each release. To suggest changes, [open a discussion](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/discussions).*

</div>
