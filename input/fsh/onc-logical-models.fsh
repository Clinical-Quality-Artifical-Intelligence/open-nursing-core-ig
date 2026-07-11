// =============================================================================
// LOGICAL MODELS (openEHR Inspired)
// These files define the "Clinical Truth" independent of FHIR Resource constraints.
// They serve as the foundational clinical definitions for the Relational AI.
// =============================================================================

Logical: ONCRelationalCareModel
Id: ONCRelationalCareModel  // PascalCase: logical-model element paths derive from the id, and eld-20 requires simple alphanumerics
Title: "Relational Care Logical Model"
Description: "A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR."
* patientPreferences 1..1 string "The patient's personal goals and what matters most to them today."
* relationalEngagement 1..1 integer "A score from 1-5 representing the depth of the therapeutic relationship."
* empathyIndex 1..1 code "The ONC Empathy Index (1-5) measuring relational quality."
* skinToneEquity 1..1 code "The patient's skin tone classification (Monk primary, Fitzpatrick secondary/legacy) used to guide clinical assessment."
* mandatoryEquityValidation 1..1 boolean "Technical flag ensuring the 'Fairness Gate' was passed."
* adpieStatus 1..1 code "The current stage of the professional nursing process (Assessment, Diagnosis, Planning, Implementation, Evaluation)."
* clinicalNarrative 1..1 string "The person-centred narrative describing the patient's experience."

// =============================================================================
// TERMINOLOGY BINDINGS
// =============================================================================
* adpieStatus from ONCADPIEVS (required)
* skinToneEquity from https://opennursingcoreig.com/ValueSet/onc-skin-tone-vs (extensible)
* empathyIndex from ONCEmpathyIndexVS (required)

// =============================================================================
// VALUE SETS for Logical Model
// =============================================================================
ValueSet: ONCADPIEVS
Id: onc-adpie-vs
Title: "ADPIE Nursing Process Phases"
Description: "The five phases of the professional nursing process."
* ^experimental = false
* ONCObservationCodes#adpie-a "Assessment"
* ONCObservationCodes#adpie-d "Diagnosis"
* ONCObservationCodes#adpie-p "Planning"
* ONCObservationCodes#adpie-i "Implementation"
* ONCObservationCodes#adpie-e "Evaluation"
