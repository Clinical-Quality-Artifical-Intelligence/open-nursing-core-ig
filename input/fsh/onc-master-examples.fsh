// ==============================================================================
// 1. FOUNDATION
// ==============================================================================
Instance: patient-example-jane
InstanceOf: ONCNHSPatient
Usage: #example
Description: "Worked example: patient example jane (ONCNHSPatient). Synthetic data - not a real person."
* name.family = "Doe"
* name.given = "Jane"
* gender = #female
* extension[ethnicCategory].valueCodeableConcept = https://fhir.hl7.org.uk/CodeSystem/UKCore-EthnicCategory#A "British, Mixed British"

Instance: practitioner-example
InstanceOf: Practitioner
Usage: #example
Description: "Worked example: practitioner example (Practitioner). Synthetic data - not a real person."
* name.family = "Nightingale"

// ==============================================================================
// 2. EQUITY
// ==============================================================================
Instance: observation-skin-tone
InstanceOf: ONCSkinToneObservation
Usage: #example
Description: "Worked example: observation skin tone (ONCSkinToneObservation). Synthetic data - not a real person."
* status = #final
* effectiveDateTime = "2026-01-15T10:00:00Z"
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
// FIX: Added the mandatory Nursing Category
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* code = http://loinc.org#66555-4
* valueCodeableConcept = ONCObservationCodes#fitzpatrick-2 "Type II"

// ==============================================================================
// 3. SAFETY
// ==============================================================================
Instance: observation-braden-scale
InstanceOf: ONCBradenScaleAssessment
Usage: #example
Description: "Worked example: observation braden scale (ONCBradenScaleAssessment). Synthetic data - not a real person."
* status = #final
* effectiveDateTime = "2026-01-15T10:00:00Z"
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueQuantity.value = 18
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* valueQuantity.code = #1
* component[sensoryPerception].code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#braden-sensory "Braden Sensory Perception"
* component[sensoryPerception].valueQuantity.value = 3
* component[sensoryPerception].valueQuantity.unit = "{score}"
* component[sensoryPerception].valueQuantity.system = "http://unitsofmeasure.org"
* component[sensoryPerception].valueQuantity.code = #1
* component[moisture].code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#braden-moisture "Braden Moisture"
* component[moisture].valueQuantity.value = 4
* component[moisture].valueQuantity.unit = "{score}"
* component[moisture].valueQuantity.system = "http://unitsofmeasure.org"
* component[moisture].valueQuantity.code = #1
* component[activity].code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#braden-activity "Braden Activity"
* component[activity].valueQuantity.value = 2
* component[activity].valueQuantity.unit = "{score}"
* component[activity].valueQuantity.system = "http://unitsofmeasure.org"
* component[activity].valueQuantity.code = #1
* component[mobility].code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#braden-mobility "Braden Mobility"
* component[mobility].valueQuantity.value = 3
* component[mobility].valueQuantity.unit = "{score}"
* component[mobility].valueQuantity.system = "http://unitsofmeasure.org"
* component[mobility].valueQuantity.code = #1
* component[nutrition].code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#braden-nutrition "Braden Nutrition"
* component[nutrition].valueQuantity.value = 3
* component[nutrition].valueQuantity.unit = "{score}"
* component[nutrition].valueQuantity.system = "http://unitsofmeasure.org"
* component[nutrition].valueQuantity.code = #1
* component[frictionAndShear].code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#braden-friction "Braden Friction/Shear"
* component[frictionAndShear].valueQuantity.value = 3
* component[frictionAndShear].valueQuantity.unit = "{score}"
* component[frictionAndShear].valueQuantity.system = "http://unitsofmeasure.org"
* component[frictionAndShear].valueQuantity.code = #1
* hasMember[skinTone] = Reference(observation-skin-tone)


// ==============================================================================
// 4. CARE PLANNING
// ==============================================================================
Instance: example-nursing-problem
InstanceOf: ONCNursingProblem
Usage: #example
Description: "Worked example: nursing problem (ONCNursingProblem). Synthetic data - not a real person."
* subject = Reference(patient-example-jane)
* clinicalStatus = http://terminology.hl7.org/CodeSystem/condition-clinical#active "Active"
* category = https://opennursingcoreig.com/CodeSystem/onc-problem-type#nursing-diagnosis "Nursing Diagnosis"
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#risk-falls "Risk of falls"

Instance: example-patient-goal
InstanceOf: ONCNursingGoal
Usage: #example
Description: "Worked example: patient goal (ONCNursingGoal). Synthetic data - not a real person."
* lifecycleStatus = #active
* subject = Reference(patient-example-jane)
* description.text = "Patient will remain free from falls."
* addresses = Reference(example-nursing-problem)
* target.measure = http://loinc.org#88020-3 "Functional status"
* target.detailCodeableConcept = http://snomed.info/sct#385652002 "Objective achieved"
* target.dueDate = "2025-12-31"


Instance: example-nursing-intervention
InstanceOf: ONCNursingIntervention
Usage: #example
Description: "Worked example: nursing intervention (ONCNursingIntervention). Synthetic data - not a real person."
* status = #completed
* subject = Reference(patient-example-jane)
* performer.actor = Reference(practitioner-example)
* code = http://snomed.info/sct#71388002 "Procedure"
* extension[interventionGoal].valueReference = Reference(example-patient-goal)

Instance: example-goal-evaluation
InstanceOf: ONCGoalEvaluation
Usage: #example
Description: "Worked example: goal evaluation (ONCGoalEvaluation). Synthetic data - not a real person."
* status = #final
* effectiveDateTime = "2026-01-15T10:00:00Z"
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* category = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept = http://snomed.info/sct#385652002 "Objective achieved"
* focus = Reference(example-patient-goal)
