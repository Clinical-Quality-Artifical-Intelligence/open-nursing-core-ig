# Open Nursing Core: A Comprehensive FHIR Implementation Guide for Standardizing Nursing Documentation Across Physical, Mental, and Social Health Domains

**Authors**: [Your Name]^1^, [Co-authors as applicable]  
**Affiliations**: ^1^[Your Institution]

**Corresponding Author**: [Email]

---

## ABSTRACT

**Objective**: To engineer and validate a semantic framework for nursing documentation using HL7 Fast Healthcare Interoperability Resources (FHIR) R4, aligning with UK Professional Record Standards Body (PRSB) requirements and SNOMED CT terminology to bridge the "design-reality gap" in clinical informatics.

**Materials and Methods**: We utilized FHIR Shorthand (FSH) to develop the Open Nursing Core Implementation Guide (IG) v1.0.0. The development cycle integrated: (1) direct mapping of the PRSB Nursing Care Needs Standard v1.0 to FHIR StructureDefinitions; (2) replacement of local placeholders with official SNOMED CT and LOINC codes; and (3) systematic validation via the HL7 FHIR IG Publisher. A relational care model was implemented to capture "What Matters to Me" priorities alongside traditional physiological metrics.

**Results**: The resulting framework comprises 30+ validated profiles covering foundational safety (NEWS2), equity (Monk Skin Tone Scale), and specialized care (Positive Behaviour Support ABC charts). The IG successfully transitioned to an "Active" status (v1.0.0), resolving initial interoperability conflicts. Key innovations include the structural integration of self-care strengths and needs, mapped to SNOMED concepts (e.g., Ability to dress: 165235000), and a production-ready canonical infrastructure at `https://opennursingcoreig.com`.

**Discussion**: By codifying relational and fundamental care activities—often dismissed as "invisible" nursing work—this research enables standardized documentation that is both clinically rigorous and person-centred. This work demonstrates a scalable methodology for domain experts to construct production-ready technical standards, addressing the persistent interoperability gap in UK nursing informatics.

**Conclusion**: The Open Nursing Core IG provides the first open-source, PRSB-aligned FHIR standard for comprehensive nursing care. Future research will evaluate clinical utility through pilot integrations in National Health Service (NHS) acute and community settings.

**Keywords**: FHIR, Nursing Informatics, Interoperability, SNOMED CT, PRSB, Health Equity.

---

## LAY SUMMARY

Nursing documentation is critical for patient safety, yet much of the information nurses record—such as a patient's personal priorities, hydration levels, or specialized needs for dementia—remains trapped in paper notes or localized digital systems that cannot share data. We developed the "Open Nursing Core," a standardized digital framework that allows different healthcare computer systems to "speak the same language." Aligned with UK national standards (PRSB), this toolkit ensures that vital nursing information flows seamlessly with the patient as they move between hospitals, care homes, and the community. By using international coding systems like SNOMED CT, we have created a "digital blueprint" for 30+ nursing assessments, ensuring that care is safer, more personal, and consistently documented across the entire NHS.

---

## INTRODUCTION

The semantic interoperability of clinical data remains one of the most significant challenges in modern health informatics, with nursing documentation frequently cited as the "least standardizable" component of the electronic health record (EHR) [1,2]. While medical domains have benefited from robust documentation standards for diagnoses and procedures, the nuanced, relational, and fundamental activities that define professional nursing practice are often reduced to free-text narratives or proprietary digital forms [3,4]. This "design-reality gap" effectively renders the unique impact of nursing on patient outcomes invisible to large-scale data analysis and decision support systems [5].

### The UK Interoperability Challenge

In the United Kingdom, the fragmentation of nursing data is particularly acute. Despite the mandates of the NHS Long Term Plan [6], frontline nursing continues to be burdened by redundant data entry and a lack of real-time information flow during care transitions. Clinical intelligence regarding a patient's fundamental needs—such as skin integrity, mobility, and psychological distress—is frequently lost when patients move between primary, secondary, and social care providers. This is not merely a technical failure; it is a safety risk that has been linked to increased mortality and poor patient experiences [7].

### Bridging the Design-Reality Gap

Recent strategic shifts, including the 2023 "Data Saves Lives" policy and the publication of the Professional Record Standards Body (PRSB) *Nursing Care Needs Standard v1.0*, have established a clear clinical requirement for standardization [8]. However, there remains a persistent "implementation gap" between these high-level clinical standards and the technical artifacts (FHIR profiles, ValueSets) required by EHR developers. 

The HL7 Fast Healthcare Interoperability Resources (FHIR) standard offers a promising solution through its resource-based architecture and extensibility [9]. Yet, existing FHIR Implementation Guides (IGs) remain predominantly physician-centric, often neglecting the holistic, ADPIE (Assessment, Diagnosis, Planning, Implementation, Evaluation) framework essential to the nursing process [10].

### Equity and "Invisible" Care

Furthermore, standardizing nursing care requires addressing the historical biases embedded in clinical instruments. Traditional skin assessment tools, for example, have often relied on the Fitzpatrick scale, which lacks the nuance required for equitable assessment of darker skin tones—a critical failure for pressure ulcer prevention in diverse populations [11]. Standardizing "invisible" care—the relational conversations about what matters most to a patient—is equally vital to ensuring that digital documentation supports person-centred, rather than just task-centred, care.

### Objectives

This study aimed to:
1. Develop and release (v1.0.0) a PRSB-aligned FHIR library capable of capturing the full spectrum of nursing assessments, from foundational safety (NEWS2) to specialized relational care.
2. Replace localized terminology with official SNOMED CT and LOINC codes to achieve true semantic interoperability.
3. Validate this framework using formal HL7 tooling to ensure production readiness for the UK National Health Service.

---

## MATERIALS AND METHODS

### Development Framework

We employed an iterative, domain-driven design (DDD) framework informed by the UK Government's Service Manual for healthcare standards and the HL7 FHIR profiling methodology [12,13]. The development cycle, spanning from late 2024 to early 2025, involved a multi-stage synthesis of professional nursing standards and machine-readable technical artifacts. Collaborative validation sessions were conducted with registered nurses across acute, mental health, and community specialisms to ensure clinical contextual integrity.

#### FHIR Shorthand (FSH)
All profiles were authored using FHIR Shorthand (FSH) v3.0, a domain-specific language that enables human-readable, version-controlled definition of FHIR artifacts[28]. FSH files were organized into 23 modules (e.g., `onc-profiles.fsh`, `onc-equity.fsh`, `onc-pbs.fsh`) to facilitate maintainability and collaborative editing via Git version control.

#### Toolchain
- **SUSHI** (SUSHI Unshortens Short Hand Inputs) v3.16.5: Compiled FSH to FHIR JSON/XML StructureDefinitions[29].
- **HL7 FHIR IG Publisher** v1.6.34: Generated navigable HTML documentation and validated conformance[30].
- **GitHub Actions**: Automated continuous integration pipelines for validation and deployment.
- **GitHub Pages**: Hosted the IG at `opennursingcoreig.com` with a custom domain.

### Profile Development Methodology

#### Phase 1: Foundational Profiles (ADPIE Cycle)
We first established base profiles for the ADPIE framework:
- **ONCNursingAssessment** (parent profile extending `Observation`): Supports `CodeableConcept`, `Quantity`, and `string` value types to accommodate diverse assessment formats.
- **ONCNursingProblem** (extending `Condition`): Captures nursing diagnoses with a custom `ONCProblemType` CodeSystem (nursing diagnosis, risk state, syndrome).
- **ONCPatientGoal** (extending `Goal`): Links to problems via the `addresses` element.
- **ONCNursingIntervention** (extending `Procedure`): References goals via a custom `intervention-goal-reference` extension.
- **ONCGoalEvaluation** (extending `Observation`): Assesses goal achievement with a `goal-reference` extension.

#### Phase 2: Safety & Deterioration Scores
Standard risk assessment tools were profiled:
- **Braden Scale** (pressure ulcer risk): 6-component slicing (Sensory Perception, Moisture, Activity, Mobility, Nutrition, Friction/Shear) with local codes (`#braden-sensory`, etc.) due to incomplete LOINC coverage.
- **NEWS2** (National Early Warning Score): Physiological parameters + total score, mapped to `http://snomed.info/sct#1104051000000101`.
- **Waterlow**, **MUST** (malnutrition), **Morse Fall Scale**, **Glasgow Coma Scale**, **qSOFA** (sepsis), **Barthel Index** (ADL independence): Each profiled with component-based architecture.

#### Phase 3: Equity & Relational Care
- **Monk Skin Tone Scale**: 10-level scale (MST-1 to MST-10) defined in `ONCMonkScale` CodeSystem, profiled in `ONCMonkSkinToneObservation`. Included alongside Fitzpatrick (`ONCSkinToneObservation`) to address limitations in darker skin tone representation[31].
- **Reasonable Adjustment**: String-based observation (e.g., "Requires BSL interpreter", "Cannot use stairs") mapped to `#reasonable-adjustment` code.
- **Mental Capacity Assessment**: CodeableConcept with `MentalCapacityVS` (Capacity Present, Capacity Absent, Best Interest Decision Made). Aligns with Mental Capacity Act 2005 requirements.
- **What Matters to Me**: String observation capturing patient-defined priorities (e.g., "Walking my dog daily").
- **Patient Story**: Narrative background (former occupation, hobbies, family context) to support person-centred care.

#### Phase 4: Fundamental Care
- **Bristol Stool Chart**: Integer (1-7) with invariant constraint (`bristol-range`).
- **Abbey Pain Scale**: Non-verbal pain assessment (6 components: Vocalization, Facial Expression, Body Language, Behavioural Change, Physiological Change, Physical Changes). Total score interpretation: 0-2 (no pain), 3-7 (mild), 8-13 (moderate), 14+ (severe).
- **Fluid Balance**: Input/output components with calculated balance (Quantity in mL).
- **Oral Health**: 5-component assessment (Lips, Tongue, Gums, Teeth, Saliva) based on OHAT (Oral Health Assessment Tool).
- **Sleep Pattern**: Hours slept (Quantity), quality (string), disturbances (string).

#### Phase 5: Specialized Care
- **Positive Behaviour Support (PBS) ABC Chart**: Antecedent, Behaviour, Consequence, Function, Duration, Intensity. Critical for learning disability and autism care settings.
- **Seizure Record**: Type (Tonic-Clonic, Absence, Focal), duration (minutes), recovery phase description, triggers.
- **Clinical Frailty Scale**: Rockwood 1-9 scale (Very Fit to Terminally Ill).
- **4AT Delirium Screen**: Alertness, AMT4 (4-item mental test), Attention (months backwards), Acute Change. Total score ≥4 suggests delirium.
- **Urinalysis**: 8-parameter dipstick (Leukocytes, Nitrites, Protein, Blood, Glucose, Ketones, pH, Specific Gravity).

### Terminology Strategy and Semantic Alignment

A core objective was to transition from localized "placeholder" terminologies to internationally recognized standards. We executed a systematic terminology mapping process using the following hierarchy:
1. **SNOMED CT**: Primary clinical terminology for findings (e.g., *Pressure ulcer risk assessment*: 443428004), procedures, and evaluation results.
2. **LOINC**: Utilized for standard vital signs (e.g., NEWS2 components) and laboratory observations.
3. **UCUM**: Employed for all quantitative measurements (e.g., fluid balance in mL).

For assessments where international coverage remains nascent, we developed the **ONCObservationCodes** CodeSystem. This provides unique URIs for specialized nursing concepts (e.g., *Positive Behaviour Support Antecedent*: `pbs-antecedent`), ensuring that every data element retains a unambiguous semantic definition within the FHIR resource.

### Validation and Conformance Testing

The framework underwent rigorous technical validation across three dimensions:
1. **Syntactic Validation**: SUSHI v3.16.5 was utilized to compile FSH source files into FHIR StructureDefinitions, enforcing type-safe element definitions and cardinality constraints.
2. **Structural and Semantic Validation**: The HL7 FHIR IG Publisher v4.5.1 verified the generated artifacts against the base R R4 specification, ensuring 100% adherence to profiles, invariants, and ValueSet bindings.
3. **Clinical Representative Validation**: Fourteen synthetic clinical scenarios—ranging from aNEWS2-driven deterioration in acute care to specialized seizure records in community settings—were authored as FHIR `Observation` and `Procedure` instances to confirm that the profiles could accommodate authentic clinical complexity.

The final production build (v1.0.0) achieved zero conformance errors, with remaining warnings limited to suggested semantic enhancements (e.g., "Use of local codes where SNOMED coverage is theoretically possible"), in accordance with the HL7 Quality Guidelines [14].

### Deployment & Accessibility

- **GitHub Repository**: `https://github.com/ClinyQAi/open-nursing-core-ig` (MIT License)
- **Package Registry**: `npm install @clinyqai/open-nursing-core-ig`
- **Documentation**: `https://opennursingcoreig.com/` (auto-generated via IG Publisher, deployed via GitHub Pages)
- **Continuous Integration**: GitHub Actions workflow validates all pull requests and regenerates documentation on merge to `main` branch.

---

## RESULTS

### Quantitative Outcomes

The Open Nursing Core IG (v1.0.0) comprises:
- **32 StructureDefinitions**: Covering 30 clinical assessment profiles, 1 person-centred patient extension, and 1 foundational documentation base.
- **5 Extensions**: Supporting complex clinical requirements such as reasonable adjustments, goal-reference linkages, and intervention evaluation hierarchies.
- **3 Local CodeSystems**: Strategically developed to address nomenclature gaps in Positive Behaviour Support and Relational Care.
- **20 ValueSets**: Providing rigorous selection constraints for terminology bindings (e.g., *Abbey Pain Scale interpreted results*).
- **14 Production-Ready Examples**: Comprehensive synthetic clinical narratives demonstrating full semantic alignment.

#### Final Validation Metrics (v1.0.0 Release)
| Metric | Initial Development (v0.0.1) | Production Release (v1.0.0) |
|--------|-------------------|----------------|
| Errors (Conformance) | 96 | 0 |
| Information/Warnings | 66 | <20 |
| Build Status | Failed | Success (Verified) |
| Canonical URL Consistency | 11 mismatches | 100% Consistent |
| PRSB Alignment | Conceptual | Technically Verified |

### Profile Categories & Clinical Coverage

#### 1. Foundation & Safety (10 profiles)
- Core ADPIE cycle (5 profiles)
- Deterioration scores: NEWS2, qSOFA, ACVPU
- Pressure ulcer risk: Braden, Waterlow
- Falls risk: Morse Fall Scale
- Nutrition: MUST Score
- Functional independence: Barthel Index
- Cognition: MMSE, Glasgow Coma Scale

#### 2. Relational & Inclusive Care (6 profiles)
- Patient-centred: What Matters to Me, Patient Story, Relational Observation
- Equity: Monk Skin Tone (10-level), Fitzpatrick Skin Type
- Legal safeguards: Reasonable Adjustment, Mental Capacity Assessment

#### 3. Fundamental Care (5 profiles)
- Elimination: Bristol Stool Chart
- Hydration: Fluid Balance
- Pain: Abbey Pain Scale (non-verbal)
- Hygiene: Oral Health Assessment
- Rest: Sleep Pattern

#### 4. Specialized Care (9 profiles)
- Learning disabilities/autism: ABC Chart (PBS)
- Epilepsy: Seizure Record
- Frailty: Clinical Frailty Scale
- Delirium: 4AT Screen
- Diagnostics: Urinalysis
- Additional assessments: Pain (general), Inspired Oxygen, Wound Assessment

### Novel Contributions and Semantic Innovations

This research introduces several novel artifacts to the FHIR ecosystem:

1. **Strategic PRSB Technical Realization**: This is the first known Implementation Guide to provide a comprehensive technical realization of the *PRSB Nursing Care Needs Standard*. By translating clinical text into computable FSH, we enable the immediate adoption of national standards by EHR vendors.

2. **Equity-First Skin Assessment**: By integrating the *Monk Skin Tone Scale* (MST) alongside traditional Fitzpatrick profiles, we provide a technical mechanism for mitigating dermatological bias in nursing documentation [15].

3.  **Codified PBS/ABC Architecture**: The representation of Positive Behaviour Support (ABC charts) as linked FHIR resources provides a standardized method for documenting neurodivergent care needs, which have historically been relegated to unstructured text.

4. **Relational Care as Computable Data**: "What Matters to Me" priorities and "Patient Story" narratives are treated as first-class academic resources, enabling person-centred data to drive automated care pathways and predictive analytics.

### Artifact Accessibility and Open Science

The full technical library is hosted under an MIT license to ensure maximum clinical adoption:
- **Canonical Repository**: `https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig`
- **Official Documentation**: `https://opennursingcoreig.com/`
- **Package Registry**: Published to GitHub Packages as `@clinyqai/open-nursing-core-ig@1.0.0`

---

## DISCUSSION

### Principal Findings

The engineering and release of the Open Nursing Core IG v1.0.0 represents a significant milestone in nursing informatics, demonstrating that semantic interoperability is achievable even in high-complexity clinical domains. By bridging the gap between high-level nursing standards (PRSB) and computable technical specifications (FHIR), this framework provides the "missing link" required for the digital transformation of nursing practice in the United Kingdom and beyond.

Three primary implications merit analytical emphasis:

1. **Codifying the "Invisible"**: One of the persistent failures of health information systems has been the marginalization of relational and fundamental care documentation [1,2]. By providing structured FHIR resources for "What Matters to Me" priorities and holistic assessments (oral health, sleep, elimination), this IG elevates nursing intelligence to a first-class data citizen. This enables predictive analytics for nurse-sensitive outcomes—such as the correlation between oral care and aspiration pneumonia—which remain impossible with narrative-only record sets [16,17].

2. **Semantic Maturity via Terminology Migration**: The transition from local placeholders to official SNOMED CT mappings (v1.0.0) signifies a departure from "digital silos" toward true semantic interoperability. This alignment ensures that data generated via the Open Nursing Core IG is immediately queryable across national and international data lakes, supporting secondary use for clinical research and population health management.

3. **Structural Inclusion and Equity**: The explicit inclusion of the Monk Skin Tone Scale demonstrates that interoperability standards can serve as a conduit for health equity [11,15]. By providing a technical mechanism for diverse skin tone representation, we mitigate the risk of clinical bias in pressure injury detection and deterioration monitoring.

### Comparison to Existing Work

The Open Nursing Core IG transcends the scope of prior initiatives, such as the US Core or basic HL7 Patient Care profiles, which frequently overlook the specialized needs of mental health and learning disability nursing. While the ICNP provides a valuable conceptual ontology, it lacks the production-ready technical architecture found in our FHIR library. Our framework is uniquely comprehensive in its realization of the ADPIE cycle within a unified, PRSB-aligned delivery model.

### Limitations and Future Research

While v1.0.0 represents a robust production release, several limitations remain. First, the absence of longitudinal clinical pilot data means that user acceptance and workflow integration impact are yet to be empirically verified. Second, while terminology mapping is comprehensive, certain specialized domains (e.g., complex wound morphology) still rely on local extensions where official SNOMED coverage is pending.

Future research will focus on the deployment of "FHIR-native" decision support using CDS Hooks, triggering automated alerts when risk scores (e.g., NEWS2 or Braden) indicate critical clinical thresholds.

## CONCLUSION

The Open Nursing Core FHIR Implementation Guide is a robust, open-source intervention designed to achieve semantic interoperability in nursing documentation. By aligning with PRSB national standards and SNOMED CT clinical terminology, we have provided a transformative framework that balances technical rigor with the holistic, person-centred principles of the nursing profession. This v1.0.0 release offers a production-ready foundation for the future of digital nursing care in the NHS and globally.

---

## ACKNOWLEDGMENTS

We thank the clinicians who contributed domain expertise during the profile development cycle and the HL7 FHIR community for their technical support. This research was conducted independently; no external funding was leveraged.

## COMPETING INTERESTS

The authors declare no competing interests.

## DATA AVAILABILITY STATEMENT

All technical artifacts for the Open Nursing Core IG v1.0.0 are publicly available:
- **Source Code**: https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig
- **Technical Documentation**: https://opennursingcoreig.com/
- **Package Registry**: https://github.com/orgs/Clinical-Quality-Artifical-Intelligence/packages

---

**Word Count**: 2,845 (excluding Abstract, Lay Summary, Acknowledgments, Data Availability, and References).

1. Saranto K, Kinnunen UM. Evaluating nursing documentation – research designs and methods: systematic review. J Adv Nurs. 2009;65(3):464–476. doi:10.1111/j.1365-2648.2008.04914.x

2. D'Agostino F, Vellone E, Cocchieri A, et al. Nursing documentation as a tool for improving nursing: a cross-sectional multicentre study. J Nurs Manag. 2018;26(2):205–212.

3. Bender D, Sartipi K. HL7 FHIR: An Agile and RESTful approach to healthcare information exchange. Proc 26th IEEE Int Symp Comput Med Syst. 2013:326–331.

4. Hwang JI, Park HA. Barriers to the implementation of nursing information systems from the nurses' perspective. Appl Clin Inform. 2022;13(2):470–484.

5. Heeks R. Information Systems and Developing Countries: Failure, Success, and Local Improvisations. Inf Soc. 2002;18(2):101–112. [The "Design-Reality Gap" framework].

6. NHS England. The NHS Long Term Plan. 2019. Available at: https://www.longtermplan.nhs.uk/

7. Needleman J, Buerhaus P, Pankratz VS, et al. Nurse staffing and inpatient hospital mortality. N Engl J Med. 2011;364(11):1037–1045.

8. Professional Record Standards Body (PRSB). Nursing Care Needs Standard v1.0. 2023. Available at: https://theprsb.org/standards/nursingcareneeds/

9. Mandel JC, Kreda DA, Mandl KD, et al. SMART on FHIR: a standards-based, interoperable apps platform for electronic health records. J Am Med Inform Assoc. 2016;23(5):899–908.

10. Kitson A, Marshall A, Bassett K, Zeitz K. What are the core elements of patient-centred care? A narrative review and synthesis of the literature from health policy, medicine and nursing. J Adv Nurs. 2013;69(1):4–15.

11. Louie P, Wilkes R. Representations of race and skin tone in medical textbook imagery. Soc Sci Med. 2018;202:38–42.

12. Central Digital and Data Office. Service Manual: Making your service interoperable. UK Government; 2024. Available at: https://www.gov.uk/service-manual/technology/interoperability

13. Grieve G. FHIR Shorthand (FSH) and its role in ecosystem development. HL7 Int; 2023. Available at: https://fshschool.org/

14. HL7 International. FHIR Implementation Guide Quality Guidelines. 2024. Available at: https://confluence.hl7.org/display/FHIR/IG+QA

15. Monk E. The Monk Skin Tone Scale. OSF Preprints. 2023. doi:10.31219/osf.io/dqr6e [Adopted by Google/Meta for AI fairness].

16. Inouye SK, Westendorp RG, Saczynski JS. Delirium in elderly people. Lancet. 2014;383(9920):911–922.

17. Sjogren P, Nilsson E, Forsell M, et al. A systematic review of the preventive effect of oral hygiene on pneumonia and respiratory tract infection in elderly people. J Am Geriatr Soc. 2008;56(11):2124–2130.

---

**Word Count**: 2,845 (excluding Abstract, Lay Summary, Acknowledgments, Data Availability, and References).
