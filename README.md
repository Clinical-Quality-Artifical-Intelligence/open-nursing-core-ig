
<div align="center">

![Open Nursing Core Banner](https://huggingface.co/spaces/NurseCitizenDeveloper/relational-ai-4-nursing/resolve/main/onc_project_banner.png)

# 🌍 Open Nursing Core (ONC)
### Global Relational AI for Person-Centred Care

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/NurseCitizenDeveloper/relational-ai-4-nursing)
[![Standard: FHIR R4](https://img.shields.io/badge/Standard-FHIR%20R4-firebrick)](http://hl7.org/fhir/R4/)
[![Alignment: PRSB](https://img.shields.io/badge/Alignment-PRSB-green)](https://theprsb.org/)

[**Deutsch**](README.de.md) | [**Español**](README.es.md) | [**Français**](README.fr.md) | [**日本語**](README.ja.md) | [**한국어**](README.kr.md) | [**Português**](README.pt.md) | [**Русский**](README.ru.md) | [**中文**](README.zh.md)

---
</div>

## 🌟 What is the Open Nursing Core?
**Open Nursing Core (ONC)** is an open-source initiative to build the world's first **Relational AI** for nursing. Unlike traditional AI that focuses only on biomedical facts, ONC is designed to understand:
- **🫀 Clinical Safety**: Validated against "Safety Gates" (e.g., Waterlow, NEWS2).
- **💚 Relational Care**: Prioritizes "What Matters to Me" and person-centred language.
- **🛡️ Evidence-Based**: Grounded in PRSB Standards and FONS nursing literature.

## 🚀 Features

### 🩺 1. Advanced Clinical Assistant
A specialized LLM fine-tuned on British Nursing Standards to draft high-quality care plans.
- **Input**: "Write a care plan for Mrs. Singh, 78, with dementia."
- **Output**: A structured ADPIE plan that is empathetic and clinically safe.

### 🏥 2. Virtual Multi-Disciplinary Team (MDT)
A collaborative AI system where specialized agents discuss patient care:
- **🩹 Tissue Viability Specialist**: Checks skin integrity and equity (Fitzpatrick tones).
- **💚 Relational Lead**: Ensures dignity and respect.
- **🛡️ Patient Safety Auditor**: Validates against safety protocols.

### 🧠 3. Person-Centred Memory (Dadi's Mirror)
The AI remembers patient preferences across sessions (e.g., "Mrs. Singh prefers to be called Dadi").

### 📚 4. Global Knowledge Base
Integrated with a massive **61MB Evidence Hub** hosted on Hugging Face, allowing the AI to cite specific nursing literature.

---

## 🛠️ Quick Start

### Try the Live Demo
👉 [**Lunch the App on Hugging Face**](https://huggingface.co/spaces/NurseCitizenDeveloper/relational-ai-4-nursing)

### Run Locally
```bash
git clone https://github.com/ClinyQAi/open-nursing-core-ig.git
cd open-nursing-core-ig/hf_space
pip install -r requirements.txt
python app.py
```

---

## 🤝 Contributing
We welcome contributions from nurses, developers, and researchers!
1. Fork the repo.
2. Create your branch: `git checkout -b feature/amazing-feature`.
3. Commit your changes: `git commit -m 'Add amazing feature'`.
4. Push to the branch: `git push origin feature/amazing-feature`.
5. Open a Pull Request.

---
**Powered by [NurseCitizenDeveloper](https://huggingface.co/NurseCitizenDeveloper)** | *Together, we code care.*
