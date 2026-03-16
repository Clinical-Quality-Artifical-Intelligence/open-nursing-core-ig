
<div align="center">

![Open Nursing Core Banner](assets/onc_project_banner.png)

# 🌍 Open Nursing Core (ONC)
### Standards-Aware AI Engine for Nurse-Led Clinical Intelligence

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/NurseCitizenDeveloper/relational-ai-4-nursing)
[![Standard: FHIR R4](https://img.shields.io/badge/Standard-FHIR%20R4-firebrick)](http://hl7.org/fhir/R4/)
[![Alignment: PRSB](https://img.shields.io/badge/Alignment-PRSB-green)](https://theprsb.org/)
[![Build Status](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/actions/workflows/docs.yml/badge.svg)](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/actions/workflows/docs.yml)
[![IG Status](https://img.shields.io/website?url=https%3A%2F%2Fopennursingcoreig.com&label=IG%20Status)](https://opennursingcoreig.com)

[**Deutsch**](README.de.md) | [**Español**](README.es.md) | [**Français**](README.fr.md) | [**日本語**](README.ja.md) | [**한국어**](README.kr.md) | [**Português**](README.pt.md) | [**Русский**](README.ru.md) | [**中文**](README.zh.md)

---
</div>

## 📖 View the Implementation Guide
**[👉 Click here to view the full Open Nursing Core FHIR Implementation Guide](https://opennursingcoreig.com)**
*Contains all FHIR profiles, extensions, and terminology.*

## 🌟 What is the Open Nursing Core?
**Open Nursing Core (ONC)** is an open-source platform and standards-aware AI engine for **nurse-led clinical intelligence**. It combines healthcare standards, clinical reasoning, and deployable tools to support safe, person-centred nursing practice. ONC is designed to deliver:
- **🫀 Clinical Safety**: Validated against "Safety Gates" (e.g., Waterlow, NEWS2).
- **💚 Relational Care**: Prioritizes empathetic and person-centred language.
- **🛡️ Evidence-Based**: Grounded in PRSB Standards and FONS nursing literature.

## 🚀 Key Features

### 🩺 1. Advanced Clinical Assistant
A specialized LLM fine-tuned on British Nursing Standards to draft high-quality care plans.
- **Input**: "Write a care plan for Mrs. Singh, 78, with dementia."
- **Output**: A structured ADPIE plan that is empathetic and clinically safe.

### 🏥 2. Virtual Multi-Disciplinary Team (MDT)
A streamlined AI synthesis tool that simulates a specialist discussion to provide a holistic care summary:
- **🩹 Tissue Viability**: Assessment prompts for skin integrity & equity (Fitzpatrick tones).
- **💚 Relational Care**: Prompts for dignity and respect.
- **🛡️ Patient Safety**: Validates against safety protocols.

### 🧠 3. Clinical Semantic Audit
Performs a deep audit of documentation against the **ONC Relational Care Logical Model** and suggests formal **NANDA-I** mappings.

---

## 🏗️ Open Nursing Core Architecture

### 1. Standards Layer
- **FHIR R4**
- **PRSB documentation standards**
- **NANDA nursing diagnoses**
- **NHS clinical frameworks**

### 2. Intelligence Layer
- **Care plan generation**
- **Clinical documentation audit**
- **Evidence retrieval**
- **MDT reasoning agents**

### 3. Application Layer
- **Nursing education tools**
- **Clinical audit tools**
- **Simulation environments**
- **Specialist apps**

### 4. Deployment Layer
- **Docker**
- **Hugging Face**
- **Cloud platforms**

---

## 🛠️ Quick Start

### Try the Live Demo
👉 [**Launch the App on Hugging Face**](https://huggingface.co/spaces/NurseCitizenDeveloper/relational-ai-4-nursing)

### Run Locally
```bash
git clone https://github.com/ClinyQAi/open-nursing-core-ig.git
cd open-nursing-core-ig/hf_space
pip install -r requirements.txt
python app.py
```

---

## 👥 Project Leadership

| Name | Role |
|------|------|
| **Kumbi Kariwo** | Health Inequalities & AI Equity Lead · Co-lead (Monk Skin Tone & Equity profiles) |
| **Lincoln** | Nurse Citizen Developer · FHIR IG Lead · Practice Educator, NMC Registered |

ONC-IG is a nurse-led initiative. Clinical leadership by nurses, for nurses —
built on open standards and hosted by the [United Nations (UNICC)](https://opensource.unicc.org/nursecitizendeveloper/open-nursing-core-ig).

---

## 🤝 Contributing

We welcome contributions from nurses, developers, clinical informaticians, and researchers.
See [ROADMAP.md](ROADMAP.md) for current priorities and [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

**Quick links:**
- 🩺 [Report a clinical error](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/new?template=clinical-review.yml)
- 🧬 [Propose a new FHIR profile](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/new?template=fhir-profile-suggestion.yml)
- 🏛️ [openEHR archetype alignment](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/new?template=archetype-openehr.yml)
- 💬 [Join the discussion](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/discussions)

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

Alternatively, use the **"Cite this repository"** button in the GitHub sidebar.

---
**Powered by [NurseCitizenDeveloper](https://huggingface.co/NurseCitizenDeveloper)** | *Together, we code care.*
