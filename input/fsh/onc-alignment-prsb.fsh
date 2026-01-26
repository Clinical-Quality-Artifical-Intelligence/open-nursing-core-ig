// =============================================================================
// PRSB Alignment Profiles
// Aligning with Professional Record Standards Body (PRSB) Nursing Care Needs Standard v1.0
// =============================================================================

// =============================================================================
// 0. FRAMEWORK: Needs, Strengths & Goals
// Definition: The PRSB Standard emphasizes visibility of strengths and needs.
// =============================================================================

Profile: ONCNursingNeed
Parent: Condition
Id: onc-nursing-need
Title: "ONC Nursing Need"
Description: "A structured representation of a nursing care need as defined by the PRSB standard. Maps to the 'Needs' section of the information model."
* clinicalStatus MS
* verificationStatus MS
* category = http://terminology.hl7.org/CodeSystem/condition-category#problem-list-item
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#nursing-needs
* subject only Reference(Patient)
* evidence MS

Profile: ONCNursingStrength
Parent: Observation
Id: onc-nursing-strength
Title: "ONC Nursing Strength"
Description: "A structured representation of a patient's strength or capability. Explicitly required by PRSB to move away from deficit-based models."
* status MS
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#nursing-strengths
* subject only Reference(Patient)
* value[x] only string or CodeableConcept
* note MS

// =============================================================================
// 1. Elimination
// =============================================================================
Profile: ONCContinenceAssessment
Parent: ONCNursingAssessment
Id: onc-continence-assessment
Title: "Continence Assessment"
Description: "Assessment of bladder and bowel control status."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#continence-assessment
* value[x] only CodeableConcept
* valueCodeableConcept from http://hl7.org/fhir/ValueSet/consistency-type (example)

Profile: ONCBladderAssessment
Parent: ONCNursingAssessment
Id: onc-bladder-assessment
Title: "Bladder Assessment"
Description: "Detailed assessment of bladder function, including voiding patterns."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#bladder-assessment
* value[x] only CodeableConcept

Profile: ONCBowelAssessment
Parent: ONCNursingAssessment
Id: onc-bowel-assessment
Title: "Bowel Assessment"
Description: "Detailed assessment of bowel function and regularity."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#bowel-assessment
* value[x] only CodeableConcept

Profile: ONCCatheterCare
Parent: ONCNursingAssessment
Id: onc-catheter-care
Title: "Catheter Care"
Description: "Documentation of catheter site care and status."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#catheter-care
* value[x] only string or CodeableConcept

// =============================================================================
// 2. Eating and Drinking
// =============================================================================
Profile: ONCOralIntakeAssessment
Parent: ONCNursingAssessment
Id: onc-oral-intake-assessment
Title: "Oral Intake Assessment"
Description: "Assessment of ability to take food and fluids orally."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#oral-intake
* value[x] only CodeableConcept

Profile: ONCSwallowingAssessment
Parent: ONCNursingAssessment
Id: onc-swallowing-assessment
Title: "Swallowing Assessment"
Description: "Screening for dysphagia and swallowing difficulties."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#swallowing
* value[x] only CodeableConcept

Profile: ONCDietaryRequirements
Parent: ONCNursingAssessment
Id: onc-dietary-requirements
Title: "Dietary Requirements"
Description: "Documentation of specific dietary needs (e.g. textural modification, cultural)."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#dietary-requirements
* value[x] only CodeableConcept or string

// =============================================================================
// 3. Mobility
// =============================================================================
Profile: ONCMobilityAssessment
Parent: ONCNursingAssessment
Id: onc-mobility-assessment
Title: "Mobility Assessment"
Description: "Assessment of capability to move and limitations."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#mobility
* value[x] only CodeableConcept
* obeys onc-mobility-gate
* component 0..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains empathyIndex 1..1 MS
* component[empathyIndex].code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#empathy-index
* component[empathyIndex].value[x] only CodeableConcept
* component[empathyIndex].valueCodeableConcept from ONCEmpathyIndexVS (required)

Profile: ONCDeviceUseStatement
Parent: DeviceUseStatement
Id: onc-device-use-statement
Title: "Device Use Statement"
Description: "Documentation of mobility aids or other devices used by the patient."
* subject only Reference(Patient)
* device only Reference(Device)
* timing[x] MS
* bodySite MS

// =============================================================================
// 4. Personal Hygiene and Dressing
// =============================================================================
Profile: ONCHygieneAssessment
Parent: ONCNursingAssessment
Id: onc-hygiene-assessment
Title: "Personal Hygiene Needs Assessment"
Description: "Assessment of assistance required for personal hygiene."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#hygiene-needs
* value[x] only CodeableConcept
* component 0..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains empathyIndex 1..1 MS
* component[empathyIndex].code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#empathy-index
* component[empathyIndex].value[x] only CodeableConcept
* component[empathyIndex].valueCodeableConcept from ONCEmpathyIndexVS (required)

Profile: ONCDressingAssessment
Parent: ONCNursingAssessment
Id: onc-dressing-assessment
Title: "Dressing and Undressing Assessment"
Description: "Assessment of assistance required for dressing and undressing, as per PRSB Personal Hygiene section."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#dressing-assessment
* value[x] only CodeableConcept

Profile: ONCOralCareAssessment
Parent: ONCNursingAssessment
Id: onc-oral-care-assessment
Title: "Oral Care Needs Assessment"
Description: "Assessment of mouth care needs and oral health."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#oral-care
* value[x] only CodeableConcept
* obeys onc-oral-gate
* component 0..* MS
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.ordered = false
* component ^slicing.rules = #open
* component contains empathyIndex 1..1 MS
* component[empathyIndex].code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#empathy-index
* component[empathyIndex].value[x] only CodeableConcept
* component[empathyIndex].valueCodeableConcept from ONCEmpathyIndexVS (required)

// =============================================================================
// 5. Skin (Tissue Viability)
// =============================================================================
Profile: ONCSkinAssessment
Parent: ONCNursingAssessment
Id: onc-skin-assessment
Title: "Skin Integrity Assessment"
Description: "Detailed assessment of skin condition (e.g., intact, dry, broken), separate from pressure ulcer risk."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#skin-assessment
* value[x] only CodeableConcept
* bodySite MS

// Note: Pressure Ulcer Risk is covered by ONCBradenScaleAssessment in 'onc-profiles.fsh'
// Note: Wound Staging is covered by ONCWoundObservation in 'onc-clinical-assessments.fsh' (implied)

// =============================================================================
// 6. Medication Self-Management
// =============================================================================
Profile: ONCMedicationAbility
Parent: ONCNursingAssessment
Id: onc-medication-ability
Title: "Medication Management Ability"
Description: "Assessment of the patient's ability to manage their own medication."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#medication-ability
* value[x] only CodeableConcept

Profile: ONCMedicationSelfAdmin
Parent: ONCNursingAssessment
Id: onc-medication-self-admin
Title: "Medication Self-Administration Observation"
Description: "Observation of the patient performing self-administration."
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#medication-self-admin
* value[x] only CodeableConcept
