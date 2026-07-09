<div align="center">

# 🗺️ ONC-IG Roadmap

**Open Nursing Core FHIR Implementation Guide**
*Community-driven · Standards-aligned · Open source*

</div>

---

> This roadmap reflects current priorities. Everything here is open for community input —
> if you want to work on something, [open a discussion](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/discussions) or pick up a [help wanted issue](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues?q=label%3A%22help+wanted%22).

---

## ✅ v1.0.0 — Released (January 2026)

- [x] Core ADPIE logical model
- [x] NEWS2 full profile with CQL decision support
- [x] MUST, Abbey Pain Scale, Bristol, GCS, MMSE, Frailty, Delirium
- [x] Equity module — **Monk Skin Tone Scale (A–J, primary)** + Fitzpatrick I–VI (secondary/legacy compatibility)
- [x] PRSB Standards alignment profiles
- [x] NEWS2 → escalation `PlanDefinition`
- [x] Safety constraint: skin tone required before pressure ulcer staging
- [x] Multilingual README (8 languages)
- [x] UN/UNICC mirror at opensource.unicc.org

See [STANDARDS_ROADMAP.md](STANDARDS_ROADMAP.md) for the path to formal standards balloting and endorsement — this IG is a **pre-ballot, trial-use community release**, not yet a balloted HL7 standard.

---

## 🔄 v1.1.0 — In Progress

> **Status:** Active development · [Track on GitHub](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues)

### 🌍 Open Health Stack / WHO ecosystem alignment
**Priority:** High · **Help wanted:** Android/Kotlin developers, SDC Questionnaire authors, global-health implementers

The [Open Health Stack Software Foundation](https://ohs.foundation) (Linux Foundation, July 2026 — with WHO as a member) provides the offline-first FHIR toolchain used by Ministries of Health and NGOs across Sub-Saharan Africa and South Asia. Making ONC assessments consumable by that stack takes nursing-process content global — and nursing content is currently a gap in that ecosystem.

- [ ] SDC `Questionnaire` representations of core assessments (NEWS2, Monk Skin Tone, Braden, Waterlow, MUST) — [issue #125](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/125)
- [ ] Demo: render one ONC assessment offline in the [Android FHIR SDK](https://github.com/ohs-foundation/android-fhir)
- [ ] Equity analytics example with [fhir-data-pipes](https://github.com/ohs-foundation/fhir-data-pipes) (pressure-ulcer detection timeliness by Monk skin tone)
- [ ] Align NEWS2 CQL/PlanDefinition with [WHO SMART Guidelines](https://smart.who.int) authoring conventions
- [ ] ICD-11 mappings for settings without a national SNOMED CT licence

> 🤝 **Looking for:** Kotlin/Android developers, FHIR SDC authors, community nurses in LMIC settings — see [STANDARDS_ROADMAP.md](STANDARDS_ROADMAP.md) Track C for the full plan

---

### ⚖️ Equity-driven safety constraints (extended)
**Priority:** High · **Lead:** Kumbi Kariwo · **Help wanted:** Clinical evidence review

- [ ] Extend CQL safety rules to cover wound assessment (beyond pressure ulcers)
- [ ] Add skin tone documentation constraint to falls risk assessment
- [ ] Validate constraints against Wounds UK Best Practice Statement 2021
- [ ] Clinical review of existing constraints by specialist nurses

> 🤝 **Looking for:** tissue viability nurses, clinical safety leads, FHIR/CQL developers

---

### 💚 Relational Care quality model
**Priority:** Medium · **Help wanted:** Research + clinical validation

Therapeutic empathy and relational care quality are central to nursing but absent from structured clinical data.
We are developing a computable model informed by validated instruments.

- [ ] Literature review of existing relational care / therapeutic empathy scales
- [ ] Map to FHIR `Observation` or `QuestionnaireResponse` base resource
- [ ] Clinical validation with practice educators
- [ ] openEHR CKM discussion — has anyone modelled this?

> 🤝 **Looking for:** nursing researchers, mental health nurses, practice educators, clinical informaticians

---

### 🏛️ openEHR dual-model alignment
**Priority:** Medium · **Help wanted:** openEHR expertise

Working toward formal alignment between ONC-IG FHIR profiles and openEHR archetypes
to support dual-model implementations.

- [ ] Map NEWS2 profile to openEHR NEWS2 archetype
- [ ] Map MUST profile to MUST archetype
- [ ] Explore FHIRconnect transformation for equity profiles
- [ ] Engage openEHR CKM community on skin tone archetypes

> 🤝 **Looking for:** openEHR archetype authors, FHIRconnect contributors, clinical modellers

---

## 🔮 v2.0.0 — Planned

| Feature | Status |
|---------|--------|
| Paediatric profiles (NEWS2 → PEWS) | Planned |
| Mental health nursing assessments | Planned |
| Community / district nursing profiles | Planned |
| Maternity (antenatal assessment) profiles | Planned |
| NMC Revalidation CPD evidence mapping | Planned |
| HL7 UK Core alignment (v3.0+) | Planned |
| SMART on FHIR app integration | Exploring |

---

## 🤝 How to contribute

| I am a... | Best way to help |
|-----------|-----------------|
| **Nurse / AHP** | Clinical review of profiles — [open a Clinical Review issue](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/new?template=clinical-review.yml) |
| **FHIR developer** | Pick up a [help wanted issue](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues?q=label%3A%22help+wanted%22) or propose a new profile |
| **openEHR contributor** | Join the [archetype alignment discussion](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/new?template=archetype-openehr.yml) |
| **Researcher** | Help with the relational care literature review |
| **Anyone** | [Join the discussion](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/discussions) — introduce yourself |

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

<div align="center">

**Project co-leads:** Kumbi Kariwo (Health Inequalities & AI Equity) · Lincoln (FHIR IG & Nurse Citizen Developer)

*This roadmap is a living document. Last updated: July 2026.*
*To suggest changes, [open a discussion](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/discussions).*

</div>
