// =============================================================================
// PRSB Alignment Examples
// Demonstrating the use of the new PRSB profiles
// =============================================================================

// -----------------------------------------------------------------------------
// 1. Framework: Needs & Strengths
// -----------------------------------------------------------------------------
Instance: ExampleNursingNeed-Dressing
InstanceOf: ONCNursingNeed
Usage: #example
Title: "Example Nursing Need: Dressing Difficulty"
Description: "Demonstration of the ONCNursingNeed profile."
* subject = Reference(Patient/example-patient)
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#nursing-needs
* clinicalStatus = http://terminology.hl7.org/CodeSystem/condition-clinical#active
* verificationStatus = http://terminology.hl7.org/CodeSystem/condition-ver-status#confirmed
* note.text = "Patient requires assistance with buttons and zippers due to arthritis."

Instance: ExampleNursingStrength-Motivation
InstanceOf: ONCNursingStrength
Usage: #example
Title: "Example Nursing Strength: Motivation"
Description: "Demonstration of the ONCNursingStrength profile."
* status = #final
* subject = Reference(Patient/example-patient)
* performer = Reference(Practitioner/example-nurse)
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#nursing-strengths
* valueString = "Highly motivated to maintain independence in upper body dressing."
* note.text = "Patient explicitly stated desire to continue buttoning own shirt if given enough time."

// -----------------------------------------------------------------------------
// 2. Personal Hygiene & Dressing
// -----------------------------------------------------------------------------
Instance: ExampleDressingAssessment
InstanceOf: ONCDressingAssessment
Usage: #example
Title: "Example Dressing Assessment"
Description: "Demonstration of the ONCDressingAssessment profile."
* status = #final
* subject = Reference(Patient/example-patient)
* performer = Reference(Practitioner/example-nurse)
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#dressing-assessment
* valueCodeableConcept.text = "Requires assistance with lower body dressing"
// In a real implementation, this would be bound to a SNOMED code, e.g., "Dependency in dressing lower body"

// -----------------------------------------------------------------------------
// 3. Skin (Tissue Viability) - Distinct from Pressure Ulcer Risk
// -----------------------------------------------------------------------------
Instance: ExampleSkinAssessment
InstanceOf: ONCSkinAssessment
Usage: #example
Title: "Example Skin Assessment"
Description: "Demonstration of the ONCSkinAssessment profile for general skin integrity."
* status = #final
* subject = Reference(Patient/example-patient)
* performer = Reference(Practitioner/example-nurse)
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#skin-assessment
* bodySite.text = "Left lower leg"
* valueCodeableConcept.text = "Dry, papery skin with no breaks"
