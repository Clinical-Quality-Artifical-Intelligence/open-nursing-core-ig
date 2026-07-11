// =============================================================================
// WORKED EXAMPLES for previously un-exemplified profiles and extensions
// (GitHub issue #162). Every example doubles as a validation test: the IG
// Publisher checks each instance against its profile on every build.
// All data is SYNTHETIC - no real patients or staff.
// =============================================================================

Alias: $LNC2 = http://loinc.org

// --- Base assessment (generic admission review) ------------------------------
Instance: example-nursing-assessment
InstanceOf: ONCNursingAssessment
Usage: #example
Title: "Example Nursing Assessment (base profile)"
Description: "Worked example: a generic structured nursing assessment using the base profile directly. Synthetic data - not a real person."
* status = #final
* code = $LNC2#51848-0 "Evaluation note"
* subject = Reference(example-patient)
* performer = Reference(example-nurse)
* effectiveDateTime = "2026-01-15T09:30:00Z"
* valueString = "Admission review completed. Alert and orientated; independent with hygiene; appetite reduced over past week - dietitian referral discussed and accepted."

// --- Barthel Index ------------------------------------------------------------
Instance: example-barthel-index
InstanceOf: ONCBarthelIndex
Usage: #example
Title: "Example Barthel Index"
Description: "Worked example: Barthel Index of 65/100 indicating moderate dependency in activities of daily living. Synthetic data."
* status = #final
* subject = Reference(example-patient)
* performer = Reference(example-nurse)
* effectiveDateTime = "2026-01-15T10:00:00Z"
* valueQuantity.value = 65
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"

// --- Device Use Statement (mobility aid) --------------------------------------
Instance: example-device
InstanceOf: Device
Usage: #example
Title: "Example Device - Walking Frame"
Description: "Worked example: the mobility aid referenced by the device use statement. Synthetic data."
* deviceName.name = "Four-wheeled walking frame"
* deviceName.type = #user-friendly-name

Instance: example-device-use
InstanceOf: ONCDeviceUseStatement
Usage: #example
Title: "Example Device Use Statement"
Description: "Worked example: patient mobilises with a four-wheeled walking frame. Synthetic data."
* status = #active
* subject = Reference(example-patient)
* device = Reference(example-device)
* timingDateTime = "2026-01-15"
* note.text = "Uses frame for all transfers and walking beyond a few steps; reviewed by physiotherapy."

// --- Glasgow Coma Scale --------------------------------------------------------
Instance: example-gcs
InstanceOf: ONCGlasgowComaScale
Usage: #example
Title: "Example Glasgow Coma Scale"
Description: "Worked example: GCS 14/15 (E4 V4 M6) - mild impairment, responds to voice with some confusion. Synthetic data."
* status = #final
* subject = Reference(example-patient)
* performer = Reference(example-nurse)
* effectiveDateTime = "2026-01-15T14:00:00Z"
* valueQuantity.value = 14
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* component[eye].valueQuantity.value = 4
* component[eye].valueQuantity.unit = "{score}"
* component[eye].valueQuantity.system = "http://unitsofmeasure.org"
* component[verbal].valueQuantity.value = 4
* component[verbal].valueQuantity.unit = "{score}"
* component[verbal].valueQuantity.system = "http://unitsofmeasure.org"
* component[motor].valueQuantity.value = 6
* component[motor].valueQuantity.unit = "{score}"
* component[motor].valueQuantity.system = "http://unitsofmeasure.org"

// --- MMSE -----------------------------------------------------------------------
Instance: example-mmse
InstanceOf: ONCMMSE
Usage: #example
Title: "Example MMSE"
Description: "Worked example: MMSE 22/30 indicating mild cognitive impairment; repeat screening and collateral history arranged. Synthetic data."
* status = #final
* subject = Reference(example-patient)
* performer = Reference(example-nurse)
* effectiveDateTime = "2026-01-16T11:00:00Z"
* valueQuantity.value = 22
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"

// --- Morse Fall Scale ------------------------------------------------------------
Instance: example-morse-fall
InstanceOf: ONCMorseFallScale
Usage: #example
Title: "Example Morse Fall Scale"
Description: "Worked example: Morse Fall Scale 55 - high falls risk; hourly rounding and low bed in place. Synthetic data."
* status = #final
* subject = Reference(example-patient)
* performer = Reference(example-nurse)
* effectiveDateTime = "2026-01-15T10:30:00Z"
* valueQuantity.value = 55
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"

// --- NEWS2 sub-score --------------------------------------------------------------
Instance: example-news2-subscore
InstanceOf: ONCNEWS2Subscore
Usage: #example
Title: "Example NEWS2 Sub-score"
Description: "Worked example: respiratory-rate parameter contributing 2 points to the NEWS2 total. Synthetic data."
* subject = Reference(example-patient)
* performer = Reference(example-nurse)
* effectiveDateTime = "2026-01-15T08:00:00Z"
* valueQuantity.value = 2
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"

// --- Nursing Clinical Impression ----------------------------------------------------
Instance: example-clinical-impression
InstanceOf: ONCNursingClinicalImpression
Usage: #example
Title: "Example Nursing Clinical Impression"
Description: "Worked example: end-of-cycle synthesis of progress against the care plan, feeding back into reassessment. Synthetic data."
* status = #completed
* subject = Reference(example-patient)
* assessor = Reference(example-nurse)
* problem = Reference(example-nursing-problem)
* date = "2026-01-20T16:00:00Z"
* summary = "Mobility goal partially achieved: transfers now supervised rather than assisted. Nutrition improving with fortified diet. Pressure areas intact; continue current repositioning plan and re-evaluate in one week."

// --- Pain Assessment (NRS 0-10) ------------------------------------------------------
Instance: example-pain-nrs
InstanceOf: ONCPainAssessment
Usage: #example
Title: "Example Pain Assessment (NRS)"
Description: "Worked example: pain 6/10 in the left hip on movement; analgesia reviewed. Synthetic data."
* status = #final
* code = $LNC2#72514-3 "Pain severity - 0-10 verbal numeric rating [Score] - Reported"
* subject = Reference(example-patient)
* performer = Reference(example-nurse)
* effectiveDateTime = "2026-01-15T12:15:00Z"
* valueQuantity.value = 6
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"
* bodySite.text = "Left hip, worse on movement"

// --- qSOFA ------------------------------------------------------------------------------
Instance: example-qsofa
InstanceOf: ONCqSOFA
Usage: #example
Title: "Example qSOFA"
Description: "Worked example: qSOFA 1/3 (raised respiratory rate only) - below the sepsis high-risk threshold, continue monitoring. Synthetic data."
* status = #final
* subject = Reference(example-patient)
* performer = Reference(example-nurse)
* effectiveDateTime = "2026-01-15T08:05:00Z"
* valueQuantity.value = 1
* valueQuantity.unit = "{score}"
* valueQuantity.system = "http://unitsofmeasure.org"

// --- Relational Engagement Score ------------------------------------------------------------
Instance: example-relational-engagement
InstanceOf: ONCRelationalObservation
Usage: #example
Title: "Example Relational Engagement Score"
Description: "Worked example: engagement level 4/5 - active partnership in care planning. Synthetic data."
* status = #final
* subject = Reference(example-patient)
* effectiveDateTime = "2026-01-16T15:00:00Z"
* valueInteger = 4

// --- Sleep Pattern ---------------------------------------------------------------------------
Instance: example-sleep-pattern
InstanceOf: ONCSleepPattern
Usage: #example
Title: "Example Sleep Pattern"
Description: "Worked example: disturbed sleep summary - relevant to delirium screening and wellbeing. Synthetic data."
* status = #final
* subject = Reference(example-patient)
* performer = Reference(example-nurse)
* effectiveDateTime = "2026-01-16T07:30:00Z"
* valueString = "Approximately five hours' broken sleep; woke twice (pain, then noise). Settled after analgesia at 03:00. Reports feeling unrefreshed."

// --- Wound Assessment (with equity gate + equity marker) --------------------------------------
Instance: example-wound-assessment
InstanceOf: ONCWoundAssessment
Usage: #example
Title: "Example Wound Assessment"
Description: "Worked example: sacral pressure ulcer staged 2, dimensions recorded, with the mandatory skin-tone context (equity gate) and the equity marker extension. Synthetic data."
* extension[ONCEquityMarker].valueBoolean = true
* status = #final
* subject = Reference(example-patient)
* performer = Reference(example-nurse)
* effectiveDateTime = "2026-01-15T11:00:00Z"
* valueCodeableConcept = ONCObservationCodes#stage-2 "Stage 2"
* component[length].valueQuantity.value = 3.5
* component[length].valueQuantity.unit = "cm"
* component[width].valueQuantity.value = 2.0
* component[width].valueQuantity.unit = "cm"
* hasMember = Reference(observation-skin-tone)
