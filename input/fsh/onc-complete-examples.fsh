
// ==============================================================================
// COMPREHENSIVE EXAMPLES FOR OPEN NURSING CORE IG
// ==============================================================================

// -----------------------------------------------------------------------------
// NEWS2 Examples (Full Panel)
// -----------------------------------------------------------------------------
Instance: example-news2-score
InstanceOf: ONCNEWS2Score
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* code = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#news2-score "NEWS2 Score"
* valueQuantity.value = 5
* valueQuantity.unit = "{score}"
* hasMember[0] = Reference(example-respiration-rate)
* hasMember[1] = Reference(example-oxygen-saturation)
* hasMember[2] = Reference(example-inspired-oxygen)
* hasMember[3] = Reference(example-blood-pressure)
* hasMember[4] = Reference(example-heart-rate)
* hasMember[5] = Reference(example-acvpu)
* hasMember[6] = Reference(example-temperature)

Instance: example-respiration-rate
InstanceOf: ONCRespirationRate
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* valueQuantity.value = 22
* valueQuantity.unit = "/min"

Instance: example-oxygen-saturation
InstanceOf: ONCOxygenSaturation
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* valueQuantity.value = 94
* valueQuantity.unit = "%"

Instance: example-inspired-oxygen
InstanceOf: ONCInspiredOxygen
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* valueCodeableConcept = http://snomed.info/sct#722742002 "Breathing room air"

Instance: example-blood-pressure
InstanceOf: ONCBloodPressure
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* component[systolic].valueQuantity.value = 110
* component[systolic].valueQuantity.unit = "mm[Hg]"
* component[diastolic].valueQuantity.value = 70
* component[diastolic].valueQuantity.unit = "mm[Hg]"

Instance: example-heart-rate
InstanceOf: ONCHeartRate
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* valueQuantity.value = 95
* valueQuantity.unit = "/min"

Instance: example-acvpu
InstanceOf: ONCACVPU
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* valueCodeableConcept = http://snomed.info/sct#248234008 "Mentally alert"

Instance: example-temperature
InstanceOf: ONCBodyTemperature
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* valueQuantity.value = 38.1
* valueQuantity.unit = "Cel"

// -----------------------------------------------------------------------------
// Waterlow & MUST Examples
// -----------------------------------------------------------------------------
Instance: example-waterlow-score
InstanceOf: ONCWaterlowScore
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueQuantity.value = 12
* valueQuantity.unit = "{score}"
* hasMember[skinTone] = Reference(observation-skin-tone)

Instance: example-must-score
InstanceOf: ONCMUSTScore
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueQuantity.value = 1
* valueQuantity.unit = "{score}"
* component[bmi].valueQuantity.value = 0
* component[weightLoss].valueQuantity.value = 1
* component[acuteDisease].valueQuantity.value = 0

// -----------------------------------------------------------------------------
// PRSB / Functional Examples
// -----------------------------------------------------------------------------
Instance: example-continence-assessment
InstanceOf: ONCContinenceAssessment
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept.text = "Occasional urinary incontinence"

Instance: example-bladder-assessment
InstanceOf: ONCBladderAssessment
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept.text = "Normal voiding pattern"

Instance: example-bowel-assessment
InstanceOf: ONCBowelAssessment
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept.text = "Daily empty, no strain"

Instance: example-catheter-care
InstanceOf: ONCCatheterCare
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueString = "Catheter changed, patent, clear urine draining."

Instance: example-mobility-assessment
InstanceOf: ONCMobilityAssessment
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept.text = "Mobilses with Zimmer frame"
* component[empathyIndex].valueCodeableConcept = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#empathy-3 "Moderate Empathy"

Instance: example-oral-intake
InstanceOf: ONCOralIntakeAssessment
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept.text = "Independent with cut-up food"

Instance: example-swallowing-assessment
InstanceOf: ONCSwallowingAssessment
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept.text = "No signs of dysphagia"

Instance: example-dietary-requirements
InstanceOf: ONCDietaryRequirements
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueString = "Vegetarian diet required"

Instance: example-hygiene-assessment
InstanceOf: ONCHygieneAssessment
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept.text = "Needs assistance washing lower legs and back"
* component[empathyIndex].valueCodeableConcept = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#empathy-4 "High Empathy"

Instance: example-oral-care-assessment
InstanceOf: ONCOralCareAssessment
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept.text = "Requires assistance with denture cleaning"
* component[empathyIndex].valueCodeableConcept = https://opennursingcoreig.com/CodeSystem/onc-observation-codes#empathy-3 "Moderate Empathy"

Instance: example-medication-ability
InstanceOf: ONCMedicationAbility
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept.text = "Able to manage own medications with dosette box"

Instance: example-medication-self-admin
InstanceOf: ONCMedicationSelfAdmin
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept.text = "Observed taking morning meds correctly"

Instance: example-monk-skin-tone
InstanceOf: ONCMonkSkinToneObservation
Usage: #example
* status = #final
* subject = Reference(patient-example-jane)
* performer = Reference(practitioner-example)
* effectiveDateTime = "2025-03-15T10:00:00Z"
* category[nursing] = http://terminology.hl7.org/CodeSystem/observation-category#survey
* valueCodeableConcept = https://opennursingcoreig.com/CodeSystem/onc-monk-scale#C "Medium Skin"
