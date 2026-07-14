<div align="center">

![Open Nursing Core logo — a nurse held within open care arcs and structured-data nodes](assets/open-nursing-core-logo.png)

# 🌍 Open Nursing Core (ONC)

### Trial-Use FHIR Foundation for Structured Nursing Information

**An open, FHIR-based data foundation for nursing documentation, clinical reasoning, safety and equity — built by nurses, in the open.**

<!-- Project -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Standard: FHIR R4](https://img.shields.io/badge/Standard-FHIR%20R4-firebrick)](http://hl7.org/fhir/R4/)
[![Alignment: PRSB](https://img.shields.io/badge/Alignment-PRSB-green)](https://theprsb.org/)
[![Hugging Face Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/NurseCitizenDeveloper/relational-ai-4-nursing)

<!-- Status -->
[![Build & Publish IG](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/actions/workflows/docs.yml/badge.svg)](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/actions/workflows/docs.yml)
[![CodeQL](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/actions/workflows/codeql.yml/badge.svg)](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/actions/workflows/codeql.yml)
[![IG Status](https://img.shields.io/website?url=https%3A%2F%2Fopennursingcoreig.com&label=live%20IG)](https://opennursingcoreig.com)

<!-- Community & traffic -->
[![Stars](https://img.shields.io/github/stars/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig?style=flat&logo=github)](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/stargazers)
[![Clones](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FClinical-Quality-Artifical-Intelligence%2Fopen-nursing-core-ig%2Ftraffic-data%2Ftraffic%2Fclones-badge.json)](traffic/)
[![Views](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FClinical-Quality-Artifical-Intelligence%2Fopen-nursing-core-ig%2Ftraffic-data%2Ftraffic%2Fviews-badge.json)](traffic/)

[**Deutsch**](README.de.md) · [**Español**](README.es.md) · [**Français**](README.fr.md) · [**日本語**](README.ja.md) · [**한국어**](README.kr.md) · [**Português**](README.pt.md) · [**Русский**](README.ru.md) · [**中文**](README.zh.md)

**[📖 Read the Implementation Guide](https://opennursingcoreig.com)** ·
**[🚀 Try the Live Demo](https://huggingface.co/spaces/NurseCitizenDeveloper/relational-ai-4-nursing)** ·
**[🤝 Contribute](CONTRIBUTING.md)** ·
**[⭐ Star this repo](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/stargazers)**

*If ONC is useful to your work, starring it helps other nurses and health-tech teams find it — that's the whole point of building this in the open.*

</div>

---

> **⚠️ Standards status: Trial Use — Pre-Ballot Community Release.** ONC-IG has not undergone formal HL7 standards balloting or independent clinical/peer review. Version and status labels reflect this project's own development lifecycle, not external endorsement. It is a specification, not a deployed product — implementers remain responsible for their own DCB0129/DCB0160 clinical safety case. The included applications and AI features are research prototypes for synthetic or appropriately de-identified data, not clinical decision systems. Read [PRODUCT_BOUNDARIES.md](PRODUCT_BOUNDARIES.md), [CLINICAL_SAFETY.md](CLINICAL_SAFETY.md) and [STANDARDS_ROADMAP.md](STANDARDS_ROADMAP.md).

---

## Contents

- [What is the Open Nursing Core?](#-what-is-the-open-nursing-core)
- [Why it matters](#-why-it-matters)
- [Key features](#-key-features)
- [Architecture](#️-architecture)
- [Quick start](#️-quick-start)
- [Repository map](#-repository-map)
- [Project leadership](#-project-leadership)
- [Standards & governance](#-standards--governance)
- [Contributing & security](#-contributing--security)
- [Repository traffic](#-repository-traffic)
- [Citation](#-citation)
- [License](#-license)

---

## 🌟 What is the Open Nursing Core?

**Open Nursing Core (ONC)** is an open-source platform and standards-aware AI engine for **nurse-led clinical intelligence**. It combines healthcare standards, clinical reasoning and deployable tools to support safe, person-centred nursing practice.

It is organised around the complete nursing process — **A**ssessment, **D**iagnosis, **P**lanning, **I**mplementation, **E**valuation (**ADPIE**) — rather than a purely pathology-driven medical model, and is informed by **PRSB** documentation standards, the **NANDA-I** taxonomy and open-access person-centred practice literature from the [International Practice Development Journal (IPDJ)](https://www.fons.org/library/journal/).

| Pillar | What it means |
|--------|---------------|
| 🫀 **Clinical safety** | Validated "safety gate" instruments (NEWS2, Braden, Waterlow, MUST…) with computable escalation logic. |
| 💚 **Relational care** | First-class "What Matters to Me" and patient-story data, and empathetic, person-centred language. |
| 🛡️ **Equitable by design** | Leads with the Monk Skin Tone Scale and structured reasonable-adjustment records (Equality Act 2010). |
| 🔗 **Interoperable** | HL7 FHIR R4 profiles with SNOMED CT / LOINC bindings, ready for real EHRs. |

The current release ships **60 profiles, 27 value sets, 3 code systems, 4 extensions, 1 logical model and 49 worked examples**.

---

## 🎯 Why it matters

Too much nursing knowledge — assessment, risk, escalation, safeguarding, the person-centred detail — stays trapped in free text and disconnected systems that cannot understand what nursing contributes. That is at once a **documentation**, **interoperability**, **data-quality**, **patient-safety** and **nursing-visibility** problem. ONC exists to make nursing knowledge **visible, reusable, structured and clinically meaningful**.

---

## 🚀 Experimental application demonstrations

The following demonstrations are not part of the normative FHIR specification
and have not been approved for clinical deployment.

### 🩺 1. Advanced Clinical Assistant
A research LLM demonstration that can draft candidate care-plan text for qualified human review.
- **Input:** "Write a care plan for Mrs. Singh, 78, with dementia."
- **Output:** a structured ADPIE plan that is empathetic and clinically safe.

### 🏥 2. Virtual Multi-Disciplinary Team (MDT)
An AI synthesis demonstration that simulates several perspectives for research and education. It is not a real MDT review and must not be represented as one.

### 🧠 3. Clinical Semantic Audit
A research audit of synthetic or de-identified documentation against the **ONC Relational Care Logical Model**. NANDA-I mappings remain subject to licensing and verification.

---

## 🏗️ Architecture

| Layer | Components |
|-------|-----------|
| **Standards** | FHIR R4 · PRSB documentation standards · NANDA-I diagnoses · NHS clinical frameworks |
| **Intelligence** | Care-plan generation · documentation audit · evidence retrieval · MDT reasoning agents |
| **Application** | Nursing education · clinical audit · simulation · specialist apps |
| **Deployment** | Docker · Hugging Face · cloud platforms |

---

## 🛠️ Quick start

### View the standard
The full Implementation Guide — every profile, extension and terminology — is published at **[opennursingcoreig.com](https://opennursingcoreig.com)**.

### Try the AI demo
👉 **[Launch the app on Hugging Face](https://huggingface.co/spaces/NurseCitizenDeveloper/relational-ai-4-nursing)**

### Build the IG locally
Requires [Node.js](https://nodejs.org/) and [SUSHI](https://fshschool.org/docs/sushi/) (`npm install -g fsh-sushi`).
```bash
git clone https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig.git
cd open-nursing-core-ig
sushi .          # compile the FSH profiles to FHIR resources
```

### Run the research demonstration
```bash
cd open-nursing-core-ig
pip install -r requirements.txt
streamlit run app_phase2.py
```

---

## 📂 Repository map

| Path | Contents |
|------|----------|
| `input/fsh/` | FHIR Shorthand (FSH) profile, extension and terminology sources |
| `input/pagecontent/` | Narrative IG pages (ADPIE, safety, equity, security, terminology…) |
| `core/`, `db/`, `ml/` | Experimental application components (auth, database, ML analytics) |
| `analytics/equity/` | Equity analytics pipeline — pressure-ulcer detection timeliness by Monk skin tone |
| `okf/` | Agent-readable knowledge bundle ([Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)) generated from the IG |
| `app_phase2.py` | Streamlit application entry point |
| `hf_space/` | Hugging Face Space (model demo) |
| `.github/workflows/` | CI: IG publish, PR validation, CodeQL, traffic tracking |

---

## 👥 Project leadership

| Name | Role |
|------|------|
| **Kumbi Kariwo** | Health Inequalities & AI Equity Lead · Co-lead (Monk Skin Tone & Equity profiles) |
| **Lincoln** | Nurse Citizen Developer · FHIR IG Lead · Practice Educator, NMC Registered |

ONC-IG is a nurse-led initiative — clinical leadership by nurses, for nurses — built on open standards and hosted by the [United Nations (UNICC)](https://opensource.unicc.org/nursecitizendeveloper/open-nursing-core-ig).

GitHub `main` is the source of truth and is synchronised to the UNICC GitLab
repository using the guarded process described in [MIRRORING.md](MIRRORING.md).

---

## 🧭 Standards & governance

ONC-IG is a **trial-use, pre-ballot community release** — see the callout at the top of this page. [STANDARDS_ROADMAP.md](STANDARDS_ROADMAP.md) sets out the concrete path toward formal review and endorsement, including:

- Immediate, loud "trial use" labelling across the IG so nothing is mistaken for a balloted standard
- Engagement with the **Professional Record Standards Body (PRSB)** formal assurance process, since the IG already grounds itself in the PRSB Nursing Care Needs standard
- Participation in an **HL7 FHIR Connectathon** to gather implementer feedback ahead of any ballot submission
- Identifying an **HL7 Work Group sponsor** (e.g. Patient Care WG) as a precondition for a formal Standard for Trial Use (STU) ballot
- Resolving the **NANDA-I licensing/terminology-canonical** gap tracked in [issue #123](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/123)

---

## 🤝 Contributing & security

We welcome contributions from nurses, developers, clinical informaticians and researchers. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and the current priorities in [ROADMAP.md](ROADMAP.md).

**Quick links**
- 🩺 [Report a clinical error](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/new?template=clinical-review.yml)
- 🧬 [Propose a new FHIR profile](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/new?template=fhir-profile-suggestion.yml)
- 🏛️ [openEHR archetype alignment](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/new?template=archetype-openehr.yml)
- 💬 [Join the discussion](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/discussions)

**How pull requests are protected.** Every PR is automatically validated (SUSHI build + Python checks), scanned for vulnerabilities with **CodeQL**, and requires review from a [code owner](.github/CODEOWNERS) before it can merge to `main`. Dependencies are monitored by **Dependabot**, and secrets are blocked by **push protection**. See [SECURITY.md](SECURITY.md) to report a vulnerability.

---

## 📈 Repository traffic

Clone and view counts are snapshotted weekly (GitHub only keeps 14 days) and stored in [`traffic/`](traffic/) with the badges shown at the top of this page. Charts below are regenerated on every snapshot. See [traffic/README.md](traffic/README.md) for the full history and CSVs.

> **Note on clone counts.** GitHub's Traffic API counts every `git clone`/`checkout` operation, including this repository's own CI workflows (CodeQL, PR validation, Hugging Face sync). A burst of pull requests or pushes will show up as a clone spike even with no new external interest — visible in the chart below around a period of heavy CI activity. Treat the trend as a proxy for repository activity, not a clean count of distinct external users; [stars](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/stargazers) are a more reliable adoption signal.

<div align="center">

![Daily repository clones](https://raw.githubusercontent.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/traffic-data/traffic/clones.png)
![Daily page views](https://raw.githubusercontent.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/traffic-data/traffic/views.png)

</div>

---

## 📑 Citation

If you use ONC-IG in research or clinical systems, please cite:

```bibtex
@software{ONC_IG_2026,
  author    = {Kariwo, Kumbi and NurseCitizenDeveloper, Lincoln},
  title     = {Open Nursing Core FHIR Implementation Guide (ONC-IG)},
  version   = {1.0.0},
  year      = {2026},
  url       = {https://opennursingcoreig.com},
  license   = {MIT}
}
```

Or use the **"Cite this repository"** button in the GitHub sidebar ([CITATION.cff](CITATION.cff)).

---

## ⚖️ License

Released under the [MIT License](LICENSE).

<div align="center">

**Powered by [NurseCitizenDeveloper](https://huggingface.co/NurseCitizenDeveloper)** · *Together, we code care.*

</div>
