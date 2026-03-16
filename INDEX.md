<div align="center">

# 🏥 Open Nursing Core FHIR Implementation Guide

### *ONC-IG v1.0.0 — Production Release*

[![FHIR R4](https://img.shields.io/badge/FHIR-R4%20%284.0.1%29-red?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0xIDE1aC0ydi02aDJ2NnptMC04aC0yVjdoMnYyeiIvPjwvc3ZnPg==)](https://hl7.org/fhir/R4/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![IG Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://opennursingcoreig.com)
[![PRSB Aligned](https://img.shields.io/badge/Aligned-PRSB%20Standards-blue)](https://theprsb.org)
[![NMC Standards](https://img.shields.io/badge/NMC-Standards%202018-navy)](https://nmc.org.uk)
[![UN Hosted](https://img.shields.io/badge/Hosted-UNICC%20%7C%20United%20Nations-009edb)](https://opensource.unicc.org/nursecitizendeveloper/open-nursing-core-ig)

**[🌐 Live IG](https://opennursingcoreig.com)** &nbsp;·&nbsp;
**[📦 GitHub](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig)** &nbsp;·&nbsp;
**[🇺🇳 UNICC Mirror](https://opensource.unicc.org/nursecitizendeveloper/open-nursing-core-ig)** &nbsp;·&nbsp;
**[📖 Cite This Work](#-citation)**

---

*Foundational FHIR profiles for the nursing process (ADPIE), with Clinical Safety and Health Equity modules.*
*Built by nurses, for nurses — open source, standards-aligned, UN-hosted.*

</div>

---

## 📋 Contents

| Section | Description |
|---------|-------------|
| [🚀 Quick Start](#-quick-start) | Get oriented in 5 minutes |
| [🧬 FHIR Profiles](#-fhir-profiles) | What clinical profiles are included |
| [📁 Repository Structure](#-repository-structure) | Where everything lives |
| [📚 Documentation](#-documentation) | Guides and references |
| [🌍 Multilingual](#-multilingual-readmes) | README in 8 languages |
| [🤝 Contributing](#-contributing) | How to get involved |
| [📎 Citation](#-citation) | How to cite this work |
| [🔗 Links](#-links) | All important URLs |

---

## 🚀 Quick Start

```
New to ONC-IG? Read in this order:
1. README.md          — What ONC is and why it exists
2. This file          — Navigate the repository
3. sushi-config.yaml  — Understand the IG configuration
4. input/fsh/         — Browse the FHIR profiles
5. opennursingcoreig.com — Read the published IG
```

> 💡 **For clinicians:** Visit [opennursingcoreig.com](https://opennursingcoreig.com) — no technical knowledge needed.
> **For developers:** Clone this repo and run `sushi .` to build locally (requires [SUSHI](https://fshschool.org/docs/sushi/installation/)).

---

## 🧬 FHIR Profiles

ONC-IG ships **30+ FHIR profiles** covering the full nursing assessment lifecycle:

### 🩺 Clinical Assessment Profiles

| Profile | Description | Standard |
|---------|-------------|----------|
| `onc-news2-full` | National Early Warning Score 2 | NHS England |
| `onc-glasgow-coma-scale` | GCS neurological assessment | Teasdale & Jennett |
| `onc-must-score` | Malnutrition Universal Screening Tool | BAPEN |
| `onc-abbey` | Abbey Pain Scale (non-verbal patients) | Abbey et al. |
| `onc-bristol` | Bristol Stool Form Scale | NICE |
| `onc-mmse` | Mini-Mental State Examination | Folstein |
| `onc-frailty` | Clinical Frailty Scale | Rockwood |
| `onc-delirium` | Delirium assessment | 4AT / CAM |
| `onc-hydration` | Fluid balance & hydration | NHS Trust |
| `onc-oral-health` | Oral health assessment | BSDH |
| `onc-mental-capacity` | MCA 2005 capacity assessment | UK Law |

### 🧠 ADPIE Process Profiles

| Profile | Description |
|---------|-------------|
| `onc-logical-models` | ADPIE logical model (Assessment → Diagnosis → Planning → Implementation → Evaluation) |
| `onc-goal-evaluation` | SMART goal tracking against care plan |
| `onc-additional-assessments` | Supplementary holistic assessment forms |
| `onc-clinical-assessments` | Core clinical assessment battery |

### ⚖️ Safety & Equity Profiles

| Profile | Description |
|---------|-------------|
| `onc-equity` | Health equity flags (Fitzpatrick skin tone, SDOH) |
| `onc-alignment-prsb` | PRSB Standards of Proficiency alignment map |

### 📐 CQL Clinical Decision Support

| Resource | Description |
|----------|-------------|
| `Library-onc-news2-cql` | NEWS2 scoring logic in Clinical Quality Language |
| `PlanDefinition-news2-escalation` | NEWS2 → escalation pathway trigger rules |

---

## 📁 Repository Structure

```
open-nursing-core-ig/
│
├── 📋 input/                        ← FHIR source files (edit here)
│   ├── fsh/                         ← FHIR Shorthand profiles (30+ files)
│   ├── resources/                   ← JSON resources (CQL, PlanDefinitions)
│   ├── cql/                         ← Clinical Quality Language libraries
│   ├── pagecontent/                 ← IG narrative pages (Markdown)
│   ├── images/                      ← Diagrams and figures
│   └── includes/                    ← Reusable fragments
│
├── 📦 docs/                         ← Generated IG output (do not edit)
│
├── ⚙️  sushi-config.yaml            ← IG publisher configuration
├── ⚙️  ig.ini                       ← FHIR IG publisher settings
├── ⚙️  package-list.json            ← Published version history
│
├── 🤖 .github/workflows/
│   ├── docs.yml                     ← Build & publish IG to GitHub Pages
│   ├── hf-sync.yml                  ← Sync to Hugging Face Spaces
│   ├── production-deploy.yml        ← Production deployment pipeline
│   └── publish-package.yml          ← NPM package publish
│
├── 🐳 Dockerfile                    ← Container image
├── 🐳 docker-compose.yml            ← Local dev environment
│
├── 📊 ml/                           ← Machine learning components
├── 📱 mobile/                       ← Mobile application
├── 🧪 core/                         ← Core library
├── 🗄️  db/                          ← Database layer
├── 🌌 hf_space/                     ← Hugging Face Space app
├── 📈 visualizations/               ← Visualisation components
│
├── 📄 README.md                     ← Project overview (start here)
├── 📄 CONTRIBUTING.md               ← How to contribute
├── 📄 SECURITY.md                   ← Security policy & reporting
├── 📄 LICENSE                       ← MIT License
└── 📄 CITATION.cff                  ← How to cite this work
```

---

## 📚 Documentation

| Document | Purpose | Read Time |
|----------|---------|-----------|
| [README.md](README.md) | Project mission, architecture, key features | 10 min |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guidelines, code standards | 5 min |
| [SECURITY.md](SECURITY.md) | Security policy and vulnerability reporting | 3 min |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Deployment options and configuration | 15 min |
| [FEATURES.md](FEATURES.md) | Full feature catalogue | 10 min |
| [BUG_REPORT.md](BUG_REPORT.md) | Known issues and workarounds | As needed |

---

## 🌍 Multilingual READMEs

This project is committed to global accessibility. The README is available in:

| Language | File | Region |
|----------|------|--------|
| 🇩🇪 Deutsch | [README.de.md](README.de.md) | DACH |
| 🇪🇸 Español | [README.es.md](README.es.md) | Latin America & Spain |
| 🇫🇷 Français | [README.fr.md](README.fr.md) | Francophone |
| 🇯🇵 日本語 | [README.ja.md](README.ja.md) | Japan |
| 🇰🇷 한국어 | [README.kr.md](README.kr.md) | Korea |
| 🇧🇷 Português | [README.pt.md](README.pt.md) | Brazil & Portugal |
| 🇷🇺 Русский | [README.ru.md](README.ru.md) | Russia & CIS |
| 🇨🇳 中文 | [README.zh.md](README.zh.md) | China |

---

## 🤝 Contributing

We welcome contributions from nurses, informaticians, FHIR developers, and health systems professionals.

```
1. Fork the repository on GitHub
2. Create a branch:  git checkout -b feature/my-profile
3. Edit FSH files in input/fsh/
4. Run:              sushi .
5. Commit (GPG-signed):  git commit -S -m "feat: add new profile"
6. Open a Pull Request
```

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md) before your first PR.

> 🔒 **Security issues** — report privately via the process in [SECURITY.md](SECURITY.md), not as public issues.

---

## 📎 Citation

If you use ONC-IG in research or clinical systems, please cite:

```bibtex
@software{onc_ig_2026,
  author    = {Clinical Quality Artificial Intelligence},
  title     = {Open Nursing Core FHIR Implementation Guide (ONC-IG)},
  version   = {1.0.0},
  year      = {2026},
  url       = {https://opennursingcoreig.com},
  license   = {MIT}
}
```

> Full citation metadata: [CITATION.cff](CITATION.cff)

---

## 🔗 Links

| Resource | URL |
|----------|-----|
| 🌐 Live Implementation Guide | https://opennursingcoreig.com |
| 📦 GitHub (primary) | https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig |
| 🇺🇳 UNICC Mirror | https://opensource.unicc.org/nursecitizendeveloper/open-nursing-core-ig |
| 🐛 Issues | https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues |
| 💬 Discussions | https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/discussions |
| 🤗 Hugging Face | https://huggingface.co/NurseCitizenDeveloper |
| 🏥 HL7 FHIR R4 Spec | https://hl7.org/fhir/R4/ |
| 📐 PRSB Standards | https://theprsb.org |

---

<div align="center">

**Open Nursing Core FHIR Implementation Guide** &nbsp;·&nbsp; v1.0.0 &nbsp;·&nbsp; MIT License

*Co-led by **Kumbi Kariwo** (Health Inequalities & AI Equity) and **Lincoln** (Nurse Citizen Developer)*
*Hosted by the [United Nations International Computing Centre (UNICC)](https://www.unicc.org)*

</div>
