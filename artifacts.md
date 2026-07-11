# Artifacts Summary - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* **Artifacts Summary**

## Artifacts Summary

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Knowledge Artifacts: Plan Definitions 

These define workflows, rules, strategies, or protocols as part of content in this implementation guide.

| | |
| :--- | :--- |
| [NEWS2 Escalation Protocol](PlanDefinition-news2-escalation-plan.md) | Computable escalation protocol for NEWS2 results, encoding the RCP response bands: 0-4 routine monitoring; 3 in any single parameter registered-nurse review; 5-6 urgent review by a clinician competent in acute illness; 7+ emergency response. |

### Knowledge Artifacts: Libraries 

These define logic, asset collections and other libraries as part of content in this implementation guide.

| | |
| :--- | :--- |
| [ONC NEWS2 Auto-Calculation Logic](Library-onc-news2-cql.md) | Logic library for calculating National Early Warning Score 2 (NEWS2) from FHIR Observations. |

### Structures: Logical Models 

These define data models that represent the domain covered by this implementation guide in more business-friendly terms than the underlying FHIR resources.

| | |
| :--- | :--- |
| [Relational Care Logical Model](StructureDefinition-ONCRelationalCareModel.md) | A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR. |

### Structures: Questionnaires 

These define forms used by systems conforming to this implementation guide to capture or expose data to end users.

| | |
| :--- | :--- |
| [Braden Scale Capture Form](Questionnaire-onc-braden-questionnaire.md) | SDC questionnaire for the Braden pressure-ulcer risk assessment: six subscales, total score, and a mandatory Monk Skin Tone item (the equity fairness gate is embedded at the capture layer). Coded items extract to Observations using the ONC Braden component codes; assembling them into the single component-based ONCBradenScaleAssessment Observation (including hasMember[skinTone]) is the capturing app's responsibility. |
| [MUST Capture Form](Questionnaire-onc-must-questionnaire.md) | SDC questionnaire for the Malnutrition Universal Screening Tool: three step scores and the total. Coded items extract to Observations using the ONC MUST component codes; assembling them into the single component-based ONCMUSTScore Observation is the capturing app's responsibility. |
| [Monk Skin Tone Capture Form](Questionnaire-onc-monk-skintone-questionnaire.md) | SDC questionnaire capturing the patient's skin tone on the 10-point Monk Skin Tone Scale (A–J). Extracts to an Observation conforming to ONCMonkSkinToneObservation. This record is the required input to the IG's equity fairness gate for wound and pressure-area assessment. |
| [NEWS2 Capture Form](Questionnaire-onc-news2-questionnaire.md) | SDC questionnaire for capturing the NEWS2 physiological parameter set and total score. Coded items extract to Observations conforming to the ONC NEWS2 and vital-sign profiles. Scoring and escalation logic is computable via the ONC_NEWS2_Logic CQL library and the news2-escalation PlanDefinition. |
| [Person-Centred Care Capture Form](Questionnaire-onc-person-centred-questionnaire.md) | SDC questionnaire capturing 'What Matters to Me' and reasonable adjustments (Equality Act 2010) as structured, retrievable records. Items extract to Observations conforming to ONCWhatMattersToMe and ONCReasonableAdjustment. |
| [Waterlow Score Capture Form](Questionnaire-onc-waterlow-questionnaire.md) | SDC questionnaire for the Waterlow pressure-ulcer risk assessment total score, with a mandatory Monk Skin Tone item (equity fairness gate embedded at the capture layer). The total extracts to an Observation using the ONC Waterlow code; linking the skin-tone Observation via hasMember[skinTone] is the capturing app's responsibility. |

### Structures: Resource Profiles 

These define constraints on FHIR resources for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [4AT Delirium Assessment](StructureDefinition-onc-4at-delirium.md) | Rapid clinical test for delirium (4AT) comprising Alertness, AMT4, Attention, and Acute Change/Fluctuating Course. A total score of 4 or more suggests possible delirium. |
| [ACVPU Consciousness Level](StructureDefinition-onc-acvpu.md) | ACVPU consciousness level assessment for NEWS2 (Alert, Confusion, Voice, Pain, Unresponsive) |
| [Abbey Pain Scale](StructureDefinition-onc-abbey-pain-scale.md) | Pain assessment for people with dementia or who cannot verbalise. Assesses 6 parameters: Vocalization, Facial Expression, Body Language, Behavioral Change, Physiological Change, Physical Changes. Total score determines pain severity (0-2 No pain, 3-7 Mild, 8-13 Moderate, 14+ Severe). |
| [Barthel Index](StructureDefinition-onc-barthel-index.md) | Barthel Index for measuring independence in activities of daily living (ADL). Score 0-20=total dependency, 91-99=slight dependency, 100=independent. Total range 0-100. |
| [Bladder Assessment](StructureDefinition-onc-bladder-assessment.md) | Detailed assessment of bladder function, including voiding patterns. |
| [Blood Pressure](StructureDefinition-onc-blood-pressure.md) | Blood pressure observation for NEWS2 (systolic BP used for scoring) |
| [Body Temperature](StructureDefinition-onc-body-temperature.md) | Body temperature observation for NEWS2 |
| [Bowel Assessment](StructureDefinition-onc-bowel-assessment.md) | Detailed assessment of bowel function and regularity. |
| [Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md) | A profile for the Braden Scale pressure ulcer risk assessment |
| [Bristol Stool Chart](StructureDefinition-onc-bristol-stool-chart.md) | Assessment of stool form using the Bristol Stool Chart (Types 1-7). Gold standard for bowel function assessment. |
| [Catheter Care](StructureDefinition-onc-catheter-care.md) | Documentation of catheter site care and status. |
| [Clinical Frailty Scale (CFS)](StructureDefinition-onc-clinical-frailty-scale.md) | Assessment of frailty using the Rockwood Clinical Frailty Scale (1-9). Essential for older adults to determine baseline functional status. |
| [Continence Assessment](StructureDefinition-onc-continence-assessment.md) | Assessment of bladder and bowel control status. |
| [Device Use Statement](StructureDefinition-onc-device-use-statement.md) | Documentation of mobility aids or other devices used by the patient. |
| [Dietary Requirements](StructureDefinition-onc-dietary-requirements.md) | Documentation of specific dietary needs (e.g. textural modification, cultural). |
| [Dressing and Undressing Assessment](StructureDefinition-onc-dressing-assessment.md) | Assessment of assistance required for dressing and undressing, as per PRSB Personal Hygiene section. |
| [Fluid Balance](StructureDefinition-onc-fluid-balance.md) | Assessment of fluid intake, output, and balance. Critical for renal function, hydration status, and heart failure monitoring. |
| [Glasgow Coma Scale](StructureDefinition-onc-glasgow-coma-scale.md) | Glasgow Coma Scale (GCS) for assessing level of consciousness. Total score 3-15 with three required components: Eye (1-4), Verbal (1-5), Motor (1-6). |
| [Heart Rate](StructureDefinition-onc-heart-rate.md) | Heart rate (pulse) observation for NEWS2 |
| [Inspired Oxygen](StructureDefinition-onc-inspired-oxygen.md) | Inspired oxygen observation for NEWS2 (air vs supplemental oxygen) |
| [MUST Score (Malnutrition Universal Screening Tool)](StructureDefinition-onc-must-score.md) | Malnutrition Universal Screening Tool for identifying adults at risk of malnutrition. Score 0=low risk, 1=medium risk, 2+=high risk. NHS-standard nutritional screening. |
| [Medication Management Ability](StructureDefinition-onc-medication-ability.md) | Assessment of the patient's ability to manage their own medication. |
| [Medication Self-Administration Observation](StructureDefinition-onc-medication-self-admin.md) | Observation of the patient performing self-administration. |
| [Mental Capacity Assessment](StructureDefinition-onc-mental-capacity.md) | Records the outcome of a Mental Capacity Assessment for a specific decision. Fundamental legal safeguard in UK nursing practice. |
| [Mini Mental State Examination (MMSE)](StructureDefinition-onc-mmse.md) | Mini Mental State Examination for cognitive function screening. Score 24-30=no impairment, 18-23=mild, 0-17=severe. Total range 0-30. |
| [Mobility Assessment](StructureDefinition-onc-mobility-assessment.md) | Assessment of capability to move and limitations. |
| [Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.md) | Observation of patient skin tone using the Monk Skin Tone Scale (10-point scale A-J). Provides more granular skin tone assessment than Fitzpatrick scale, particularly for darker skin tones. Supports equitable care and accurate clinical assessment across diverse populations. |
| [Morse Fall Scale](StructureDefinition-onc-morse-fall-scale.md) | Morse Fall Scale for assessing fall risk. Score 0-24=no risk, 25-50=low risk, ≥51=high risk. Total range 0-125. |
| [NEWS2 Score](StructureDefinition-onc-news2-score.md) | National Early Warning Score 2 (NEWS2) for detecting clinical deterioration. Fully aligned with NHS CareConnect-NEWS2-Observation-1. |
| [NEWS2 Sub-Score](StructureDefinition-onc-news2-subscore.md) | Individual parameter sub-score for NEWS2 (0-3 for most parameters). References the related vital sign observation. |
| [Nursing Problem](StructureDefinition-onc-nursing-problem.md) | Nursing diagnosis or problem identified during assessment. Represents clinical judgments about individual, family, or community responses to actual or potential health problems. Part of the ADPIE framework's Diagnosis phase. |
| [ONC Goal Evaluation](StructureDefinition-onc-goal-evaluation.md) | Explicit evaluation of whether a nursing goal was achieved, closing the ADPIE loop. |
| [ONC NHS Patient](StructureDefinition-onc-nhs-patient.md) | A patient profile for use in NHS nursing contexts with ethnic category extension. |
| [ONC Nursing Clinical Impression](StructureDefinition-onc-nursing-clinical-impression.md) | Nurse's synthesis of patient progress against care plan, aggregating multiple goal evaluations. |
| [ONC Nursing Goal](StructureDefinition-onc-nursing-goal.md) | Patient-centered goal with mandatory evaluation requirements. Serves as the 'spine' of the CarePlan, linking problems to outcomes. |
| [ONC Nursing Intervention](StructureDefinition-onc-nursing-intervention.md) | Nursing intervention performed to achieve patient goals. Part of ADPIE Implementation phase. |
| [ONC Nursing Need](StructureDefinition-onc-nursing-need.md) | A structured representation of a nursing care need as defined by the PRSB standard. Maps to the 'Needs' section of the information model. |
| [ONC Nursing Strength](StructureDefinition-onc-nursing-strength.md) | A structured representation of a patient's strength or capability. Explicitly required by PRSB to move away from deficit-based models. |
| [Open Nursing Core Assessment](StructureDefinition-onc-nursing-assessment.md) | Base profile for nursing assessment observations conforming to UK Core standards. Captures structured nursing assessment data as part of the ADPIE (Assessment, Diagnosis, Planning, Implementation, Evaluation) nursing process framework. Used as parent for specialized assessments like NEWS2, Braden Scale, and clinical observations. |
| [Oral Care Needs Assessment](StructureDefinition-onc-oral-care-assessment.md) | Assessment of mouth care needs and oral health. |
| [Oral Health Assessment](StructureDefinition-onc-oral-health.md) | Assessment of oral cavity health. Critical for prevention of pneumonia in frail elderly and maintaining nutrition/hydration. |
| [Oral Intake Assessment](StructureDefinition-onc-oral-intake-assessment.md) | Assessment of ability to take food and fluids orally. |
| [Oxygen Saturation](StructureDefinition-onc-oxygen-saturation.md) | Oxygen saturation (SpO2) observation for NEWS2 |
| [PBS ABC Chart](StructureDefinition-onc-abc-chart.md) | Antecedent-Behaviour-Consequence (ABC) Chart for recording behaviours of concern. Fundamental tool in Positive Behaviour Support (PBS) for Learning Disabilities. |
| [Pain Assessment (NRS 0-10)](StructureDefinition-onc-pain-assessment.md) | Pain severity assessment using the Numeric Rating Scale (0-10) |
| [Patient Story](StructureDefinition-onc-patient-story.md) | A narrative summary of the patient's background, biography, preferences, and personhood. Goes beyond clinical history to capture 'who the person is'. |
| [Personal Hygiene Needs Assessment](StructureDefinition-onc-hygiene-assessment.md) | Assessment of assistance required for personal hygiene. |
| [Reasonable Adjustment](StructureDefinition-onc-reasonable-adjustment.md) | Captures specific strict requirements for care adjustments under the Equality Act (e.g., 'Needs BSL Interpreter', 'Cannot use stairs', 'Requires large print'). |
| [Relational Engagement Score](StructureDefinition-onc-relational-observation.md) | Assessment of the quality and depth of the nurse-patient relationship or engagement level. Supports the relational aspect of care. |
| [Respiration Rate](StructureDefinition-onc-respiration-rate.md) | Respiration rate observation for NEWS2 |
| [Seizure Record](StructureDefinition-onc-seizure-record.md) | Record of a specific seizure event, including type, duration, triggers, and recovery phases. Essential for epilepsy management and identifying patterns. |
| [Skin Integrity Assessment](StructureDefinition-onc-skin-assessment.md) | Detailed assessment of skin condition (e.g., intact, dry, broken), separate from pressure ulcer risk. |
| [Skin Tone Observation (Fitzpatrick -- secondary/legacy)](StructureDefinition-onc-skintone-observation.md) | Observation of patient skin tone using the Fitzpatrick skin type classification. Fitzpatrick was designed to describe UV photosensitivity, not clinical skin tone, and compresses the darker end of the range into few categories. This profile is RETAINED FOR BACKWARD COMPATIBILITY with systems that already record Fitzpatrick phototypes; it is secondary to, and SHOULD NOT be used in place of, the Monk Skin Tone Scale (see ONCMonkSkinToneObservation), which is this IG's primary and recommended skin-tone vocabulary. |
| [Sleep Pattern](StructureDefinition-onc-sleep-pattern.md) | Observation of sleep quality, duration, and disturbances. Sleep pattern disturbance is a key indicator for delirium and general wellbeing. |
| [Swallowing Assessment](StructureDefinition-onc-swallowing-assessment.md) | Screening for dysphagia and swallowing difficulties. |
| [Urinalysis](StructureDefinition-onc-urinalysis.md) | Point-of-care urine dipstick test results. Used to screen for urinary tract infection (UTI), diabetes (glucose/ketones), and kidney health. |
| [Waterlow Score](StructureDefinition-onc-waterlow-score.md) | Waterlow Pressure Ulcer Risk Assessment - NHS standard tool. Score ≥10 indicates at risk, ≥15 high risk, ≥20 very high risk. |
| [What Matters to Me](StructureDefinition-onc-what-matters.md) | Captures the patient's specific, personal priorities and non-clinical goals (e.g., 'I want to walk my daughter down the aisle'). Fundamental to person-centred care. |
| [Wound Assessment](StructureDefinition-onc-wound-assessment.md) | Comprehensive wound assessment including staging and dimensions |
| [qSOFA (Quick SOFA)](StructureDefinition-onc-qsofa.md) | Quick Sequential Organ Failure Assessment for sepsis screening. Score ≥2 indicates high risk. Total range 0-3. |

### Structures: Extension Definitions 

These define constraints on FHIR data types for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Intervention Goal Reference](StructureDefinition-intervention-goal-reference.md) | Extension to link nursing interventions to the patient goals they are intended to achieve. |
| [ONC Equity Marker](StructureDefinition-onc-equity-marker.md) | A technical extension applied to observations that have passed the Mandatory Equity Gate (i.e., they are skin-tone aware). |
| [Observation Goal Reference](StructureDefinition-observation-goal-reference.md) | Extension to link goal evaluation observations to the patient goals being evaluated. |
| [UK Core Ethnic Category](StructureDefinition-UKCore-Extension-EthnicCategory.md) | An extension to record the ethnic category of a patient, as per UK Core standards. |

### Terminology: Value Sets 

These define sets of codes used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [4AT AMT4 Value Set](ValueSet-onc-4at-amt4-vs.md) | Scoring options for AMT4 (Age, DOB, Place, Year) |
| [4AT Acute Change Value Set](ValueSet-onc-4at-acute-change-vs.md) | Scoring for Acute Change or Fluctuating Course |
| [4AT Alertness Value Set](ValueSet-onc-4at-alertness-vs.md) | Scoring options for 4AT Alertness |
| [4AT Attention Value Set](ValueSet-onc-4at-attention-vs.md) | Scoring for Months Backwards test |
| [ACVPU Value Set](ValueSet-acvpu-vs.md) | ACVPU consciousness level codes |
| [ADPIE Nursing Process Phases](ValueSet-onc-adpie-vs.md) | The five phases of the professional nursing process. |
| [Clinical Frailty Scale Value Set](ValueSet-onc-cfs-vs.md) | Codes for Rockwood Clinical Frailty Scale (1-9) |
| [Goal Evaluation Value Set](ValueSet-goal-evaluation-valueset.md) | Value set for evaluating patient goal outcomes |
| [Goal Target Measure ValueSet](ValueSet-onc-goal-target-measure-vs.md) | Codes used for goal target measures |
| [Housing Status Value Set](ValueSet-housing-status-vs.md) | Value set for patient housing status |
| [Inspired Oxygen Value Set](ValueSet-inspired-oxygen-vs.md) | Codes for inspired oxygen status |
| [Mental Capacity Finding Value Set](ValueSet-onc-mca-vs.md) | Codes indicating presence or absence of capacity |
| [Monk Skin Tone Scale ValueSet](ValueSet-onc-monk-scale-vs.md) | ValueSet for ONCMonkScaleVS used by the Open Nursing Core IG. |
| [NEWS2 Code Value Set](ValueSet-news2-code-vs.md) | LOINC and SNOMED codes for NEWS2 |
| [NEWS2 Score Categories Value Set](ValueSet-onc-news2-score-vs.md) | NEWS2 total score categories. |
| [NEWS2 Sub-Score Codes](ValueSet-news2-subscore-code-vs.md) | SNOMED codes for NEWS2 sub-scores |
| [Nursing Intervention Value Set](ValueSet-nursing-intervention-valueset.md) | Value set for nursing interventions |
| [Nursing Problem Value Set](ValueSet-nursing-problem-valueset.md) | Value set for nursing problems and diagnoses |
| [Nursing Prognosis ValueSet](ValueSet-onc-prognosis-vs.md) | Prognosis codes for clinical impression |
| [ONC Empathy & Relational Engagement Index](ValueSet-onc-empathy-index-vs.md) | A clinical scale measuring the depth of therapeutic empathy in nurse-patient interactions. Traditional EHRs ignore this; the Super-Gold Standard makes it a primary outcome. |
| [ONC Relational Care Outcomes](ValueSet-onc-relational-outcomes-vs.md) | Captures the measurable outcomes of relational and empathic nursing care. |
| [ONC Relational Findings](ValueSet-onc-relational-findings-vs.md) | The relational-care findings that the onc-to-nanda ConceptMap maps to formal nursing diagnoses. |
| [PBS Behaviour Function ValueSet](ValueSet-onc-pbs-function-vs.md) | Common functions of behaviour (SEAT) |
| [Pain Assessment Code Value Set](ValueSet-pain-assessment-code-vs.md) | LOINC codes for pain severity assessment |
| [Pain Score Value Set](ValueSet-onc-pain-score-vs.md) | Standard 0-10 or Abbey Pain Scale score |
| [Problem Category Value Set](ValueSet-problem-category-valueset.md) | Value set for categorizing nursing problems |
| [Skin Tone Value Set](ValueSet-onc-skin-tone-vs.md) | Skin tone scales for equitable skin assessment. Monk (A-J) is the primary, recommended scale; Fitzpatrick (I-VI) is retained only for backward compatibility with legacy systems. |
| [Wound Stage Value Set](ValueSet-wound-stage-vs.md) | ValueSet for WoundStageValueSet used by the Open Nursing Core IG. |

### Terminology: Code Systems 

These define new code systems used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Monk Skin Tone Scale CodeSystem](CodeSystem-onc-monk-scale.md) | The ten-point (A-J) Monk Skin Tone Scale, the IG's primary vocabulary for equitable skin-tone assessment. |
| [ONC Observation Codes](CodeSystem-onc-observation-codes.md) | Custom observation codes for Open Nursing Core |
| [Problem Type CodeSystem](CodeSystem-onc-problem-type.md) | Code system for categorizing types of nursing problems |

### Terminology: Concept Maps 

These define transformations to convert between codes by systems conforming with this implementation guide.

| | |
| :--- | :--- |
| [Mapping ONC Relational Concepts to NANDA-I](ConceptMap-onc-to-nanda.md) | Maps Open Nursing Core clinical findings to NANDA-I Nursing Diagnoses. NOT PRODUCTION-READY: see the placeholder-canonical note below. |

### Example: Example Instances 

These are example instances that show what data produced and consumed by systems conforming with this implementation guide might look like.

| | |
| :--- | :--- |
| [Example Dressing Assessment](Observation-ExampleDressingAssessment.md) | Demonstration of the ONCDressingAssessment profile. |
| [Example Nursing Need: Dressing Difficulty](Condition-ExampleNursingNeed-Dressing.md) | Demonstration of the ONCNursingNeed profile. |
| [Example Nursing Strength: Motivation](Observation-ExampleNursingStrength-Motivation.md) | Demonstration of the ONCNursingStrength profile. |
| [Example Skin Assessment](Observation-ExampleSkinAssessment.md) | Demonstration of the ONCSkinAssessment profile for general skin integrity. |
| [example-4at-delirium](Observation-example-4at-delirium.md) | Worked example of a 4AT delirium screen conforming to ONC4ATDelirium. |
| [example-abbey-pain](Observation-example-abbey-pain.md) | Worked example of an Abbey Pain Scale assessment conforming to ONCAbbeyPainScale. |
| [example-abc-chart](Observation-example-abc-chart.md) |  |
| [example-acvpu](Observation-example-acvpu.md) |  |
| [example-bladder-assessment](Observation-example-bladder-assessment.md) |  |
| [example-blood-pressure](Observation-example-blood-pressure.md) |  |
| [example-bowel-assessment](Observation-example-bowel-assessment.md) |  |
| [example-bristol-stool](Observation-example-bristol-stool.md) |  |
| [example-catheter-care](Observation-example-catheter-care.md) |  |
| [example-clinical-frailty](Observation-example-clinical-frailty.md) |  |
| [example-continence-assessment](Observation-example-continence-assessment.md) |  |
| [example-dietary-requirements](Observation-example-dietary-requirements.md) |  |
| [example-fluid-balance](Observation-example-fluid-balance.md) |  |
| [example-goal-evaluation](Observation-example-goal-evaluation.md) |  |
| [example-heart-rate](Observation-example-heart-rate.md) |  |
| [example-hygiene-assessment](Observation-example-hygiene-assessment.md) |  |
| [example-inspired-oxygen](Observation-example-inspired-oxygen.md) |  |
| [example-medication-ability](Observation-example-medication-ability.md) |  |
| [example-medication-self-admin](Observation-example-medication-self-admin.md) |  |
| [example-mental-capacity](Observation-example-mental-capacity.md) |  |
| [example-mobility-assessment](Observation-example-mobility-assessment.md) |  |
| [example-monk-skin-tone](Observation-example-monk-skin-tone.md) |  |
| [example-must-score](Observation-example-must-score.md) |  |
| [example-news2-score](Observation-example-news2-score.md) |  |
| [example-nursing-intervention](Procedure-example-nursing-intervention.md) |  |
| [example-nursing-problem](Condition-example-nursing-problem.md) |  |
| [example-oral-care-assessment](Observation-example-oral-care-assessment.md) |  |
| [example-oral-health](Observation-example-oral-health.md) |  |
| [example-oral-intake](Observation-example-oral-intake.md) |  |
| [example-oxygen-saturation](Observation-example-oxygen-saturation.md) |  |
| [example-patient-goal](Goal-example-patient-goal.md) | Patient will remain free from falls. |
| [example-patient-story](Observation-example-patient-story.md) |  |
| [example-reasonable-adjustment](Observation-example-reasonable-adjustment.md) |  |
| [example-respiration-rate](Observation-example-respiration-rate.md) |  |
| [example-seizure-record](Observation-example-seizure-record.md) |  |
| [example-swallowing-assessment](Observation-example-swallowing-assessment.md) |  |
| [example-temperature](Observation-example-temperature.md) |  |
| [example-urinalysis](Observation-example-urinalysis.md) |  |
| [example-waterlow-score](Observation-example-waterlow-score.md) |  |
| [example-what-matters](Observation-example-what-matters.md) |  |
| [observation-braden-scale](Observation-observation-braden-scale.md) |  |
| [observation-skin-tone](Observation-observation-skin-tone.md) |  |
| [patient-example-jane](Patient-patient-example-jane.md) |  |
| [practitioner-example](Practitioner-practitioner-example.md) |  |

