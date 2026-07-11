---
model_name: Relational Ai for Nursing Nursing Llama-3
base_model: unsloth/llama-3-8b-bnb-4bit
language:
- en
license: cc-by-nc-3.0
tags:
- medical
- nursing
- person-centred-care
- fons
- llama-3
- unsloth
- 4-bit
pipeline_tag: text-generation
---

# 🏥 Relational Ai for Nursing: Nursing Llama-3 (8B)

<div align="center">

![License](https://img.shields.io/badge/License-CC_BY--NC_3.0-lightgrey.svg)
![IPDJ](https://img.shields.io/badge/Materials-IPDJ_Open_Access-blue)
![Equity](https://img.shields.io/badge/Equity-Skin_Tone_Invariant-purple)
![Finteuned with Unsloth](https://img.shields.io/badge/Finetuned%20with-Unsloth-orange)

**A research LLM fine-tuned on open-access International Practice Development Journal (IPDJ) materials for person-centred, equitable clinical documentation.**

</div>

---

## 📄 Model Description

**Relational Ai for Nursing** is a fine-tuned version of Llama-3 (8B) designed to research assistance with nursing documentation, care planning, and clinical reasoning. It was trained on **6,698 instruction-response pairs** derived from open-access IPDJ materials concerning person-centredness, relational care and practice development. Training on these materials does not ensure alignment and does not imply endorsement by IPDJ, its authors or its publisher.

- **Developed by:** NurseCitizenDeveloper / Open Nursing Core Team
- **Base Model:** `unsloth/llama-3-8b-bnb-4bit`
- **Fine-Tuning Method:** LoRA (Low-Rank Adaptation) via Unsloth
- **Language:** English
- **License:** CC BY-NC 3.0

## 📜 Dataset & Licensing
This model was fine-tuned on data derived from the **[International Practice Development Journal (IPDJ)](https://www.fons.org/library/journal/)**. IPDJ states that its articles are distributed under [CC BY-NC 3.0](https://creativecommons.org/licenses/by-nc/3.0/). Article-level attribution and provenance must be retained in derived datasets.
*   **Source:** International Practice Development Journal (IPDJ), published by FoNS in association with its journal partners
*   **Non-Commercial:** This model should be used for research and educational purposes only.

## 🌟 Key Features

*   **Person-Centred Language**: Generates documentation that respects patient dignity and preferences.
*   **Health Equity Focus**: Specifically trained to include **skin tone documentation** in pressure ulcer risk assessments (Braden Scale), addressing a critical gap in standard AI models.
*   **Structured Nursing Process**: Follows the **ADPIE** key framework (Assessment, Diagnosis, Planning, Implementation, Evaluation).
*   **IPDJ-informed approach**: Prioritises relational care and checking for understanding over generic medical jargon.

## 📊 Evaluation Results

We evaluated Relational Ai for Nursing using **Azure GPT-4o typically as an "Expert Judge"** across clinically relevant test cases.

| Metric | Score (1-10) | Description |
| :--- | :---: | :--- |
| **Clinical Accuracy** | **6.6** | Clinically sound interventions and assessments |
| **Person-Centred Language** | **7.6** | High degree of respect, dignity, and personalization |
| **IPDJ-informed practice** | **6.0** | Internal evaluation of person-centred and relational-care characteristics |

### 🏆 Spotlight Performance

*   **Equity / Skin Tone Assessment**:
    *   **Accuracy**: **8/10**
    *   **Person-Centredness**: **9/10**
    *   *The model successfully identifies the importance of documenting skin tone nuances often missed by generic models.*

*   **Nursing Process (ADPIE)**:
    *   **Accuracy**: **9/10**
    *   *Strong capability in structuring clinical reasoning.*

## 💻 How to Use

### Installation
Relational Ai for Nursing is optimized with `unsloth` for faster inference but supports standard Hugging Face `transformers`.

```bash
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install --no-deps xformers trl peft accelerate bitsandbytes
```

### Inference Code

```python
from unsloth import FastLanguageModel

# 1. Load Model
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "NurseCitizenDeveloper/nursing-llama-3-8b-fons",
    max_seq_length = 2048,
    dtype = None,
    load_in_4bit = True,
)
FastLanguageModel.for_inference(model)

# 2. Define Prompt (Alpaca Format)
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

# 3. Generate
inputs = tokenizer(
[
    alpaca_prompt.format(
        "Summarize the key nursing interventions for a patient with delirium.", # Instruction
        "Patient is an 85-year-old male presenting with acute confusion...", # Input
        "", # Leave blank for generation
    )
], return_tensors = "pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens = 128)
print(tokenizer.batch_decode(outputs)[0])
```

## ⚠️ Limitations & Ethical Considerations

*   **Clinical Assistant, Not Replacement**: This model is a support tool. All outputs must be verified by a registered nurse.
*   **Training Data**: While trained on IPDJ materials, the model may still hallucinate facts or reflect biases in the source corpus or base Llama-3 model.
*   **Scope**: Optimized for UK/NHS context but applicable broadly.

## 📚 Citation

If you use this model in your research or practice, please cite:

```bibtex
@misc{fons_ai_2025,
  author = {NurseCitizenDeveloper},
  title = {Relational Ai for Nursing: A Person-Centred Nursing Documentation Model},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face Hub},
  howpublished = {\url{https://huggingface.co/NurseCitizenDeveloper/nursing-llama-3-8b-fons}}
}
```

---
*Created with ❤️ by the Open Nursing Core Team.*
