# Product boundaries and maturity

Open Nursing Core is primarily a **FHIR R4 Implementation Guide**. Version
numbers describe this project's publication lifecycle; they do not indicate
HL7 ballot approval, PRSB assurance, clinical deployment approval, or medical
device conformity.

| Component | Maturity | Permitted use |
|---|---|---|
| FHIR profiles, terminology and examples | Pre-ballot trial-use specification | Evaluation, implementation testing and structured clinical review |
| SDC Questionnaires | Experimental implementation aids | Synthetic-data demonstrations and usability testing |
| Validator | Prototype/subset implementation | Developer conformance testing; not a clinical safety control |
| Streamlit and Hugging Face applications | Research demonstrations | Synthetic or properly de-identified data only |
| AI assistant and virtual MDT | Unevaluated research features | Education and research; outputs require qualified human review |
| Equity analytics | Reference pipeline | Synthetic or appropriately governed datasets |
| Mobile application | Prototype | Demonstration only |

## Explicit exclusions

This repository is not:

- a certified electronic patient record;
- a substitute for professional judgement or local escalation policy;
- an autonomous diagnostic, triage, prescribing or treatment system;
- a completed DCB0129/DCB0160 clinical safety case;
- approved for identifiable patient data by default; or
- an externally endorsed HL7, PRSB, NHS or WHO standard.

Implementing organisations remain responsible for clinical safety, information
governance, cybersecurity, accessibility, usability, terminology licences,
local validation and regulatory classification.

See [CLINICAL_SAFETY.md](CLINICAL_SAFETY.md) for the minimum assurance gates.
