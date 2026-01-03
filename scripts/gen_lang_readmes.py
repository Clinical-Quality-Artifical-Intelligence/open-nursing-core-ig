
import os

languages = {
    "de": "Willkommen bei Open Nursing Core",
    "ja": "Open Nursing Core へようこそ",
    "kr": "Open Nursing Core에 오신 것을 환영합니다",
    "pt": "Bem-vindo ao Open Nursing Core",
    "ru": "Добро пожаловать в Open Nursing Core",
    "zh": "欢迎使用 Open Nursing Core"
}

base_content = """
<div align="center">

![Open Nursing Core Banner](hf_space/onc_project_banner.png)

# 🌍 Open Nursing Core (ONC)
### Global Relational AI for Person-Centred Care

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/NurseCitizenDeveloper/relational-ai-4-nursing)
[![Standard: FHIR R4](https://img.shields.io/badge/Standard-FHIR%20R4-firebrick)](http://hl7.org/fhir/R4/)
[![Alignment: PRSB](https://img.shields.io/badge/Alignment-PRSB-green)](https://theprsb.org/)

[**English**](README.md) | [**Deutsch**](README.de.md) | [**Español**](README.es.md) | [**Français**](README.fr.md) | [**日本語**](README.ja.md) | [**한국어**](README.kr.md) | [**Português**](README.pt.md) | [**Русский**](README.ru.md) | [**中文**](README.zh.md)

---
</div>

## {welcome_msg}
**This is a placeholder for the localized documentation.** 
*Updates coming soon.*

Please refer to the [**English Documentation**](README.md) for the full feature set.
"""

for lang_code, msg in languages.items():
    preview = base_content.format(welcome_msg=msg)
    filename = f"README.{lang_code}.md"
    print(f"Generating {filename}...")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(preview)

print("✅ All language placeholders created.")
