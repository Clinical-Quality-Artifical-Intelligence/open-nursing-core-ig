# Open Nursing Core: An Open-Source Framework for Person-Centred AI Documentation in Nursing

**Lincoln Gombedza**¹

¹ Independent Researcher, Nursing Citizen Development Initiative, United Kingdom

**Correspondence:** lincoln.gombedza@example.com

---

## Abstract

**Background:** Nursing documentation is essential for patient safety and care continuity, yet imposes substantial administrative burden that detracts from direct patient care. Emerging ambient clinical intelligence (ACI) and large language model (LLM) technologies offer potential solutions, but existing systems are predominantly trained on biomedical datasets and physician-patient interactions. This risks generating documentation that is clinically complete but relationally thin—systematically omitting the 'invisible work' of nursing: emotional support, advocacy, and therapeutic presence.

**Objective:** To develop and describe Open Nursing Core (ONC), an open-source framework comprising standardised data profiles, validation infrastructure, and a fine-tuned language model specifically designed to capture person-centred relational care in nursing documentation.

**Methods:** We developed a multi-layered technical architecture: (1) a FHIR Implementation Guide defining nursing-specific data profiles aligned with the ADPIE framework; (2) a REST API validation service ensuring documentation meets safety and relational care standards; and (3) a large language model fine-tuned on 6,698 instruction-response pairs derived from person-centred nursing scholarship. Preliminary evaluation used an LLM-as-judge methodology assessing outputs on clinical accuracy and person-centredness.

**Results:** The fine-tuned model (nursing-llama-3-8b-fons) achieved scores of 8/10 for clinical accuracy and 9/10 for person-centredness on equity-focused test cases, with particular strength in capturing skin tone documentation for pressure ulcer assessment—a known gap in generic AI systems. The complete framework is available as open-source software with deployed demonstrations.

**Conclusions:** Open Nursing Core demonstrates the feasibility of developing nursing-specific AI documentation infrastructure grounded in person-centred practice scholarship. The framework provides a foundation for rigorous evaluation research comparing person-centred AI documentation approaches against generic alternatives.

**Keywords:** nursing informatics, artificial intelligence, person-centred care, FHIR, clinical documentation, large language models

---

## 1. Introduction

### 1.1 The Documentation Burden in Nursing

Nursing documentation is fundamental to patient safety, care continuity, and professional accountability [1]. The Nursing and Midwifery Council's Code explicitly requires nurses to "keep clear and accurate records relevant to your practice" [2]. However, documentation imposes substantial time burden, with evidence suggesting nurses spend up to 35% of their working time on administrative tasks [3,4].

This burden has significant consequences. Research links excessive documentation requirements to burnout, moral distress, and professional dissatisfaction [5,6]. When documentation competes with direct patient care, nurses face ethical tensions between administrative obligations and therapeutic presence.

### 1.2 The Promise and Peril of AI Documentation

Ambient clinical intelligence (ACI) and large language model (LLM) technologies are rapidly emerging as potential solutions to documentation burden. Recent studies demonstrate that ACI can significantly reduce documentation time in medical consultations—in some cases by up to 70% [7].

However, current ACI and LLM systems present significant limitations for nursing applications. These tools are predominantly trained on biomedical datasets derived from physician dictation and medical transcription services [8]. They are optimised for the 'medical model'—symptoms, diagnoses, and treatment plans—rather than the holistic, relational dimensions that characterise nursing care.

Allen's concept of 'invisible work' illuminates this gap [9,10]. Nursing practice encompasses organising, mediating, and relational labour that holds healthcare trajectories together but rarely appears in formal documentation. This includes:

- Therapeutic presence and emotional support
- Advocacy for patient preferences and values
- Coordination across multidisciplinary teams
- Facilitation of shared decision-making
- Assessment of psychosocial context

If AI documentation systems are applied uncritically to nursing, they risk generating notes that are clinically 'complete' in a biomedical sense but 'relationally thin'—systematically erasing core nursing contributions from the health record.

### 1.3 The Need for Nursing-Specific AI Infrastructure

The Person-Centred Practice Framework [11] provides theoretical foundations for understanding what AI documentation should capture. The framework emphasises care achieved through therapeutic relationships, underpinned by values of respect for persons, individual right to self-determination, and mutual understanding.

Currently, no open-source AI infrastructure exists that operationalises person-centred practice principles for nursing documentation. This paper describes Open Nursing Core (ONC), a framework designed to address this gap through:

1. Standardised data profiles for nursing documentation
2. Validation infrastructure ensuring safety and relational care standards
3. A language model fine-tuned on person-centred nursing scholarship

---

## 2. Methods

### 2.1 Framework Architecture

Open Nursing Core comprises four integrated layers (Figure 1):

```
┌─────────────────────────────────────────────────────────┐
│  Layer 4: Applications (Relational AI 4 Nursing)        │
│  Deployed user interfaces for documentation assistance  │
├─────────────────────────────────────────────────────────┤
│  Layer 3: AI Model (nursing-llama-3-8b-fons)            │
│  Fine-tuned LLM with person-centred knowledge           │
├─────────────────────────────────────────────────────────┤
│  Layer 2: Validation (NHS Unified Nursing Validator)    │
│  REST API ensuring standards compliance                 │
├─────────────────────────────────────────────────────────┤
│  Layer 1: Standards (Open Nursing Core IG)              │
│  FHIR profiles for nursing data (ADPIE framework)       │
└─────────────────────────────────────────────────────────┘

Figure 1: Open Nursing Core architecture
```

### 2.2 Layer 1: FHIR Implementation Guide

The Open Nursing Core Implementation Guide (ONC-IG) defines FHIR (Fast Healthcare Interoperability Resources) profiles specific to nursing documentation. FHIR is the international standard for healthcare data exchange, ensuring interoperability with existing electronic health record systems.

The IG structures nursing data according to the ADPIE framework:
- **A**ssessment: Patient data collection and observation
- **D**iagnosis: Nursing diagnosis identification (NANDA-I aligned)
- **P**lanning: Care plan development
- **I**mplementation: Intervention documentation
- **E**valuation: Outcome assessment

Key profiles include:
- **ONC-Observation**: Nursing assessments with relational care metadata
- **ONC-CarePlan**: Structured care plans with person-centred goals
- **ONC-Condition**: Nursing diagnoses with holistic context

The IG is available in eight languages (English, German, Spanish, French, Japanese, Korean, Portuguese, Russian, Chinese) to support global nursing communities.

### 2.3 Layer 2: Validation API

The NHS Unified Nursing Validator is a TypeScript/Node.js REST API service that validates FHIR resources against ONC-IG profiles. The validator ensures documentation meets both clinical safety standards and relational care requirements.

**Endpoint:** `POST /api/validate`

**Validation Dimensions:**
- Structural validity (FHIR compliance)
- Clinical safety (required fields present)
- Relational care (person-centred elements captured)

The validator provides actionable feedback when documentation falls short of standards, supporting quality improvement.

### 2.4 Layer 3: Fine-Tuned Language Model

#### 2.4.1 Training Data

We curated a training corpus from open-access person-centred nursing scholarship:

- **International Practice Development Journal (IPDJ)**: Full archive (2011-present)
- **Foundation of Nursing Studies (FoNS) publications**: Practice development resources

From these sources, we generated 6,698 instruction-response pairs covering:
- Care planning with person-centred language
- Assessment documentation including relational dimensions
- Clinical reasoning incorporating patient values
- Equity-focused documentation (including skin tone assessment)

The corpus is licensed under CC BY-NC 3.0, permitting research and educational use.

#### 2.4.2 Model Training

We fine-tuned Llama-3 (8B parameters) using Low-Rank Adaptation (LoRA) via the Unsloth library. Training parameters:

| Parameter | Value |
|-----------|-------|
| Base model | unsloth/llama-3-8b-bnb-4bit |
| Fine-tuning method | LoRA |
| Training examples | 6,698 |
| Epochs | 3 |
| Learning rate | 2e-4 |

The resulting model is designated `nursing-llama-3-8b-fons`.

### 2.5 Layer 4: Deployed Applications

We deployed demonstration applications on Hugging Face Spaces:

1. **Relational AI 4 Nursing**: Documentation assistant generating person-centred notes
2. **NMC Knowledge Bot**: Professional standards support tool
3. **Health Inclusion Coach**: Equity-focused clinical assistance

### 2.6 Preliminary Evaluation

We conducted preliminary evaluation using an LLM-as-judge methodology [12]. GPT-4o assessed model outputs on:

1. **Clinical Accuracy** (1-10): Factual correctness and safety
2. **Person-Centredness** (1-10): Relational care, dignity, patient voice

Test cases included scenarios known to challenge generic AI systems, particularly skin tone documentation for pressure ulcer assessment—an equity concern where standard AI often fails [13].

---

## 3. Results

### 3.1 Implementation Outcomes

The complete Open Nursing Core framework has been implemented and deployed as open-source software:

| Component | Repository | Status |
|-----------|------------|--------|
| ONC Implementation Guide | github.com/ClinyQAi/open-nursing-core-ig | Published |
| NHS Unified Nursing Validator | github.com/ClinyQAi/nhs-unified-nursing-validator | Deployed |
| nursing-llama-3-8b-fons | huggingface.co/NurseCitizenDeveloper/nursing-llama-3-8b-fons | Available |
| Demonstration Applications | huggingface.co/NurseCitizenDeveloper | Running |

### 3.2 Preliminary Evaluation Results

The fine-tuned model demonstrated strong performance on preliminary evaluations:

**Equity / Skin Tone Assessment:**
- Clinical Accuracy: 8/10
- Person-Centredness: 9/10
- The model successfully documented skin tone nuances for pressure ulcer risk—content typically omitted by generic models

**Nursing Process (ADPIE) Structuring:**
- Clinical Accuracy: 9/10
- The model consistently structured outputs using appropriate nursing frameworks

### 3.3 Example Output Comparison

**Prompt:** *"Write a care plan for Mrs. Singh, 78, with early dementia."*

**Generic LLM Response:**
> "Dementia care plan: Monitor cognitive status. Ensure safety. Administer medications as prescribed. Document changes."

**nursing-llama-3-8b-fons Response:**
> "Person-Centred Care Plan for Mrs. Singh
>
> *Getting to Know Mrs. Singh:* Understanding her life history, preferences, and what matters most to her will guide our care approach...
>
> *Assessment:* Working with Mrs. Singh and her family to understand her current abilities, concerns, and goals. Assessing not just cognition but her emotional wellbeing and sense of self...
>
> *Dignity and Respect:* Ensuring Mrs. Singh is addressed by her preferred name, involved in decisions about her care, and supported to maintain her identity..."

The fine-tuned model generates documentation that centres the patient as a person, emphasises therapeutic relationship, and explicitly addresses dignity—content absent from generic outputs.

---

## 4. Discussion

### 4.1 Addressing the 'Invisible Work' Gap

Open Nursing Core demonstrates the feasibility of developing AI documentation infrastructure specifically designed for nursing's relational dimensions. By fine-tuning on person-centred scholarship rather than biomedical datasets, the framework generates documentation that captures aspects of nursing care typically rendered invisible.

This approach aligns with Allen's analysis of invisible work [9] and responds to concerns that AI documentation may reinforce task-oriented reductionism. The framework provides a technical foundation for ensuring AI supports rather than erodes nursing's therapeutic contribution.

### 4.2 Open-Source and Equity Considerations

The decision to develop Open Nursing Core as open-source infrastructure reflects both practical and ethical considerations:

1. **Accessibility**: Open-source tools can be adopted by resource-constrained healthcare settings globally
2. **Transparency**: Open weights and training data enable scrutiny of AI behaviour
3. **Equity**: Explicit attention to skin tone documentation addresses known disparities in generic AI systems

The multi-language Implementation Guide supports international nursing communities, recognising that person-centred care is a global aspiration.

### 4.3 Limitations

This work has important limitations:

1. **Preliminary Evaluation**: LLM-as-judge methodology provides initial signal but requires validation through human expert evaluation
2. **Simulated Context**: Evaluation used constructed prompts, not real clinical documentation
3. **Single Model**: Comparison with multiple alternative approaches not yet conducted
4. **No Patient Involvement**: Patient and public perspectives on documentation preferences not yet incorporated

### 4.4 Future Work

Rigorous evaluation research is needed to:
- Compare person-centred AI documentation against generic alternatives using validated instruments
- Assess clinical safety through expert review
- Evaluate implementation feasibility and nurse acceptability
- Incorporate patient and public perspectives

The framework provides technical infrastructure enabling such research.

---

## 5. Conclusions

Open Nursing Core demonstrates that nursing-specific AI documentation infrastructure, grounded in person-centred practice scholarship, is technically feasible and can be developed using open-source approaches. The framework addresses a critical gap: the risk that generic AI documentation tools will systematically omit nursing's relational contribution to care.

By establishing standardised profiles (FHIR IG), validation infrastructure, and a fine-tuned language model, ONC provides foundations for research comparing person-centred AI documentation approaches against generic alternatives. The complete framework is available as open-source software to support the global nursing community.

---

## Data Availability

All code, models, and documentation are available:
- Implementation Guide: https://github.com/ClinyQAi/open-nursing-core-ig
- Validation API: https://github.com/ClinyQAi/nhs-unified-nursing-validator
- Fine-tuned Model: https://huggingface.co/NurseCitizenDeveloper/nursing-llama-3-8b-fons
- Demonstrations: https://huggingface.co/NurseCitizenDeveloper

---

## Funding

This work was conducted independently without external funding.

---

## Competing Interests

The author declares no competing interests.

---

## Author Contributions

LG conceived the framework, developed all technical components, conducted preliminary evaluation, and wrote the manuscript.

---

## Acknowledgements

The author acknowledges the Foundation of Nursing Studies (FoNS) for their open-access publication of person-centred nursing scholarship under Creative Commons licensing, which enabled this work.

---

## References

1. Nursing and Midwifery Council. The Code: Professional standards of practice and behaviour for nurses, midwives and nursing associates. London: NMC; 2018.

2. de Groot K, Triemstra M, Paans W, Francke A. Nursing documentation and its relationship with perceived nursing workload: A mixed-methods study among community nurses. BMC Nursing. 2022;21:34.

3. Baumann LA, Baker J, Elshaug AG. The impact of electronic health record systems on clinical documentation times: A systematic review. Health Policy. 2018;122(8):827-836.

4. Ball JE, Bruyneel L, Aiken LH, et al. Post-operative mortality, missed care and nurse staffing in nine countries: A cross-sectional study. Int J Nurs Stud. 2017;78:10-15.

5. Aiken LH, Sloane DM, Barnes H, et al. Nurses' and patients' appraisals of hospital nurse staffing policies and patient safety: A cross-sectional study. BMJ Qual Saf. 2023;32(2):86-93.

6. Wendt SJ, Dinh CT, Sutcliffe M, et al. Deploying ambient clinical intelligence to improve care: Assessing the impact of Nuance DAX on documentation burden and burnout. Future Healthc J. 2025;12(3):100450.

7. Finley G, Edwards E, Robinson A, et al. An automated medical scribe for documenting clinical encounters. Proceedings of NAACL-HLT 2018:11-15.

8. Allen D. The Invisible Work of Nurses: Hospitals, Organisation and Healthcare. London: Routledge; 2015.

9. Allen D. Inside 'the black box' of nursing work: Researching the invisible. Int J Nurs Stud. 2015;52(12):1835-1838.

10. McCormack B, McCance T. Person-Centred Practice in Nursing and Health Care: Theory and Practice. 2nd ed. Chichester: Wiley-Blackwell; 2017.

11. Zheng Y, Zhang R, Zhang J, et al. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. Advances in Neural Information Processing Systems. 2023;36.

12. Adelekun A, Onyekaba G, Lipoff JB. Skin color in dermatology textbooks: An updated evaluation and analysis. J Am Acad Dermatol. 2021;84(1):194-196.

