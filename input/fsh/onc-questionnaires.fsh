// =============================================================================
// STRUCTURED DATA CAPTURE (SDC) QUESTIONNAIRES
//
// FHIR Questionnaire representations of the core ONC nursing assessments, so
// they can be rendered and captured by Open Health Stack data-capture
// libraries (android-fhir Structured Data Capture, kotlin-fhir-data-capture)
// and any other SDC-conformant renderer. Tracked in GitHub issue #125.
//
// Extraction approach: OBSERVATION-BASED extraction (SDC
// sdc-questionnaire-observationExtract). Every item that carries an
// item.code extracts to an Observation with that code; items without a code
// (display/logic items) do not extract. Integer/decimal items carry the core
// questionnaire-unit extension so extracted values become valueQuantity with
// the UCUM unit the ONC profiles require (e.g. "{score}").
//
// Composite-profile note: observation-based extraction produces one
// Observation per coded item. Profiles that additionally require
// Observation.component (Braden 6..6, MUST 3..3) or the equity-gate
// hasMember[skinTone] reference (Braden, Waterlow) need the capturing app
// (or a StructureMap) to assemble those elements from the extracted set —
// all required codes are captured by these questionnaires, including a
// mandatory Monk Skin Tone item inside the Braden and Waterlow forms, so the
// assembly is mechanical. Apps SHOULD also set Observation.category to
// observation-category#survey per the ONCNursingAssessment base profile.
// =============================================================================

Alias: $LNC = http://loinc.org
Alias: $SCT = http://snomed.info/sct
Alias: $UCUM = http://unitsofmeasure.org
Alias: $obsExtract = http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-observationExtract
Alias: $qUnit = http://hl7.org/fhir/StructureDefinition/questionnaire-unit
Alias: $minValue = http://hl7.org/fhir/StructureDefinition/minValue
Alias: $maxValue = http://hl7.org/fhir/StructureDefinition/maxValue

// -----------------------------------------------------------------------------
// 1. NEWS2 - National Early Warning Score 2
// -----------------------------------------------------------------------------
Instance: onc-news2-questionnaire
InstanceOf: Questionnaire
Usage: #definition
Title: "NEWS2 Capture Form"
Description: "SDC questionnaire for capturing the NEWS2 physiological parameter set and total score. Coded items extract to Observations conforming to the ONC NEWS2 and vital-sign profiles. Scoring and escalation logic is computable via the ONC_NEWS2_Logic CQL library and the news2-escalation PlanDefinition."
* url = "https://opennursingcoreig.com/Questionnaire/onc-news2-questionnaire"
* name = "ONCNEWS2Questionnaire"
* title = "NEWS2 (National Early Warning Score 2)"
* status = #draft
* subjectType = #Patient
* extension[0].url = $obsExtract
* extension[0].valueBoolean = true

* item[0].linkId = "resp-rate"
* item[0].text = "Respiration rate (breaths per minute)"
* item[0].type = #integer
* item[0].required = true
* item[0].code = $LNC#9279-1 "Respiratory rate"
* item[0].extension[0].url = $qUnit
* item[0].extension[0].valueCoding = $UCUM#"/min" "/min"
* item[0].extension[1].url = $minValue
* item[0].extension[1].valueInteger = 0
* item[0].extension[2].url = $maxValue
* item[0].extension[2].valueInteger = 90

* item[1].linkId = "spo2"
* item[1].text = "Oxygen saturation, SpO2 (%)"
* item[1].type = #integer
* item[1].required = true
* item[1].code = $LNC#59408-5 "Oxygen saturation in Arterial blood by Pulse oximetry"
* item[1].extension[0].url = $qUnit
* item[1].extension[0].valueCoding = $UCUM#"%" "%"
* item[1].extension[1].url = $minValue
* item[1].extension[1].valueInteger = 0
* item[1].extension[2].url = $maxValue
* item[1].extension[2].valueInteger = 100

* item[2].linkId = "spo2-scale2"
* item[2].text = "Use SpO2 Scale 2? (Prescribed target saturation 88–92%, e.g. hypercapnic respiratory failure — decision made by a competent clinician)"
* item[2].type = #boolean
* item[2].required = true

* item[3].linkId = "o2-status"
* item[3].text = "Air or supplemental oxygen?"
* item[3].type = #choice
* item[3].required = true
* item[3].code = $LNC#3151-8 "Inhaled oxygen flow rate"
* item[3].answerOption[0].valueCoding = $SCT#722742002 "Breathing room air"
* item[3].answerOption[1].valueCoding = $SCT#371825009 "Patient on oxygen"

* item[4].linkId = "systolic-bp"
* item[4].text = "Systolic blood pressure (mmHg)"
* item[4].type = #integer
* item[4].required = true
* item[4].code = $LNC#8480-6 "Systolic blood pressure"
* item[4].extension[0].url = $qUnit
* item[4].extension[0].valueCoding = $UCUM#"mm[Hg]" "mm[Hg]"
* item[4].extension[1].url = $minValue
* item[4].extension[1].valueInteger = 20
* item[4].extension[2].url = $maxValue
* item[4].extension[2].valueInteger = 300

* item[5].linkId = "diastolic-bp"
* item[5].text = "Diastolic blood pressure (mmHg) — recorded, not scored"
* item[5].type = #integer
* item[5].required = false
* item[5].code = $LNC#8462-4 "Diastolic blood pressure"
* item[5].extension[0].url = $qUnit
* item[5].extension[0].valueCoding = $UCUM#"mm[Hg]" "mm[Hg]"

* item[6].linkId = "heart-rate"
* item[6].text = "Pulse / heart rate (beats per minute)"
* item[6].type = #integer
* item[6].required = true
* item[6].code = $LNC#8867-4 "Heart rate"
* item[6].extension[0].url = $qUnit
* item[6].extension[0].valueCoding = $UCUM#"/min" "/min"
* item[6].extension[1].url = $minValue
* item[6].extension[1].valueInteger = 0
* item[6].extension[2].url = $maxValue
* item[6].extension[2].valueInteger = 350

* item[7].linkId = "temperature"
* item[7].text = "Body temperature (°C)"
* item[7].type = #decimal
* item[7].required = true
* item[7].code = $LNC#8310-5 "Body temperature"
* item[7].extension[0].url = $qUnit
* item[7].extension[0].valueCoding = $UCUM#"Cel" "Cel"
* item[7].extension[1].url = $minValue
* item[7].extension[1].valueDecimal = 25.0
* item[7].extension[2].url = $maxValue
* item[7].extension[2].valueDecimal = 45.0

* item[8].linkId = "acvpu"
* item[8].text = "Level of consciousness (ACVPU)"
* item[8].type = #choice
* item[8].required = true
* item[8].code = $SCT#1104441000000107 "ACVPU (Alert Confusion Voice Pain Unresponsive) scale score"
* item[8].answerOption[0].valueCoding = $SCT#248234008 "Mentally alert"
* item[8].answerOption[1].valueCoding = $SCT#130987000 "Acute confusion"
* item[8].answerOption[2].valueCoding = $SCT#300202002 "Responds to voice"
* item[8].answerOption[3].valueCoding = $SCT#450847001 "Responds to pain"
* item[8].answerOption[4].valueCoding = $SCT#422768004 "Unresponsive"

* item[9].linkId = "news2-total"
* item[9].text = "NEWS2 total score (0–20)"
* item[9].type = #integer
* item[9].required = true
* item[9].code = ONCObservationCodes#news2-score "NEWS2 Score"
* item[9].extension[0].url = $qUnit
* item[9].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[9].extension[1].url = $minValue
* item[9].extension[1].valueInteger = 0
* item[9].extension[2].url = $maxValue
* item[9].extension[2].valueInteger = 20

* item[10].linkId = "escalation-guidance"
* item[10].type = #display
* item[10].text = "Escalation (RCP NEWS2): 0–4 low risk — routine monitoring · 3 in any single parameter — registered nurse review · 5–6 medium risk — urgent review by a clinician competent in acute illness · 7+ high risk — emergency response. The ONC_NEWS2_Logic CQL library computes the score and the news2-escalation PlanDefinition encodes this protocol; this form does not replace clinical judgement."

// -----------------------------------------------------------------------------
// 2. Monk Skin Tone Observation (standalone)
// -----------------------------------------------------------------------------
Instance: onc-monk-skintone-questionnaire
InstanceOf: Questionnaire
Usage: #definition
Title: "Monk Skin Tone Capture Form"
Description: "SDC questionnaire capturing the patient's skin tone on the 10-point Monk Skin Tone Scale (A–J). Extracts to an Observation conforming to ONCMonkSkinToneObservation. This record is the required input to the IG's equity fairness gate for wound and pressure-area assessment."
* url = "https://opennursingcoreig.com/Questionnaire/onc-monk-skintone-questionnaire"
* name = "ONCMonkSkinToneQuestionnaire"
* title = "Monk Skin Tone Scale (A–J)"
* status = #draft
* subjectType = #Patient
* extension[0].url = $obsExtract
* extension[0].valueBoolean = true

* item[0].linkId = "mst-intro"
* item[0].type = #display
* item[0].text = "Record the skin tone that best matches the patient, assessed with the patient's involvement in good lighting. Accurate skin tone recording is a patient-safety requirement: pressure damage, cyanosis, pallor and erythema present differently across skin tones."

* item[1].linkId = "mst-score"
* item[1].text = "Monk Skin Tone Scale rating"
* item[1].type = #choice
* item[1].required = true
* item[1].code = ONCObservationCodes#mst-score "Monk Skin Tone Score"
* item[1].answerValueSet = Canonical(ONCMonkScaleVS)

// -----------------------------------------------------------------------------
// 3. Braden Scale (pressure ulcer risk) - with embedded equity gate
// -----------------------------------------------------------------------------
Instance: onc-braden-questionnaire
InstanceOf: Questionnaire
Usage: #definition
Title: "Braden Scale Capture Form"
Description: "SDC questionnaire for the Braden pressure-ulcer risk assessment: six subscales, total score, and a mandatory Monk Skin Tone item (the equity fairness gate is embedded at the capture layer). Coded items extract to Observations using the ONC Braden component codes; assembling them into the single component-based ONCBradenScaleAssessment Observation (including hasMember[skinTone]) is the capturing app's responsibility."
* url = "https://opennursingcoreig.com/Questionnaire/onc-braden-questionnaire"
* name = "ONCBradenQuestionnaire"
* title = "Braden Scale (Pressure Ulcer Risk)"
* status = #draft
* subjectType = #Patient
* extension[0].url = $obsExtract
* extension[0].valueBoolean = true

* item[0].linkId = "braden-sensory"
* item[0].text = "Sensory perception (1 = Completely limited · 2 = Very limited · 3 = Slightly limited · 4 = No impairment)"
* item[0].type = #integer
* item[0].required = true
* item[0].code = ONCObservationCodes#braden-sensory "Braden Sensory Perception"
* item[0].extension[0].url = $qUnit
* item[0].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[0].extension[1].url = $minValue
* item[0].extension[1].valueInteger = 1
* item[0].extension[2].url = $maxValue
* item[0].extension[2].valueInteger = 4

* item[1].linkId = "braden-moisture"
* item[1].text = "Moisture (1 = Constantly moist · 2 = Very moist · 3 = Occasionally moist · 4 = Rarely moist)"
* item[1].type = #integer
* item[1].required = true
* item[1].code = ONCObservationCodes#braden-moisture "Braden Moisture"
* item[1].extension[0].url = $qUnit
* item[1].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[1].extension[1].url = $minValue
* item[1].extension[1].valueInteger = 1
* item[1].extension[2].url = $maxValue
* item[1].extension[2].valueInteger = 4

* item[2].linkId = "braden-activity"
* item[2].text = "Activity (1 = Bedfast · 2 = Chairfast · 3 = Walks occasionally · 4 = Walks frequently)"
* item[2].type = #integer
* item[2].required = true
* item[2].code = ONCObservationCodes#braden-activity "Braden Activity"
* item[2].extension[0].url = $qUnit
* item[2].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[2].extension[1].url = $minValue
* item[2].extension[1].valueInteger = 1
* item[2].extension[2].url = $maxValue
* item[2].extension[2].valueInteger = 4

* item[3].linkId = "braden-mobility"
* item[3].text = "Mobility (1 = Completely immobile · 2 = Very limited · 3 = Slightly limited · 4 = No limitation)"
* item[3].type = #integer
* item[3].required = true
* item[3].code = ONCObservationCodes#braden-mobility "Braden Mobility"
* item[3].extension[0].url = $qUnit
* item[3].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[3].extension[1].url = $minValue
* item[3].extension[1].valueInteger = 1
* item[3].extension[2].url = $maxValue
* item[3].extension[2].valueInteger = 4

* item[4].linkId = "braden-nutrition"
* item[4].text = "Nutrition (1 = Very poor · 2 = Probably inadequate · 3 = Adequate · 4 = Excellent)"
* item[4].type = #integer
* item[4].required = true
* item[4].code = ONCObservationCodes#braden-nutrition "Braden Nutrition"
* item[4].extension[0].url = $qUnit
* item[4].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[4].extension[1].url = $minValue
* item[4].extension[1].valueInteger = 1
* item[4].extension[2].url = $maxValue
* item[4].extension[2].valueInteger = 4

* item[5].linkId = "braden-friction"
* item[5].text = "Friction and shear (1 = Problem · 2 = Potential problem · 3 = No apparent problem)"
* item[5].type = #integer
* item[5].required = true
* item[5].code = ONCObservationCodes#braden-friction "Braden Friction/Shear"
* item[5].extension[0].url = $qUnit
* item[5].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[5].extension[1].url = $minValue
* item[5].extension[1].valueInteger = 1
* item[5].extension[2].url = $maxValue
* item[5].extension[2].valueInteger = 3

* item[6].linkId = "braden-total"
* item[6].text = "Braden total score (6–23; lower = higher risk)"
* item[6].type = #integer
* item[6].required = true
* item[6].code = ONCObservationCodes#braden-total-score "Braden Total Score"
* item[6].extension[0].url = $qUnit
* item[6].extension[0].valueCoding = $UCUM#"1" "{score}"
* item[6].extension[1].url = $minValue
* item[6].extension[1].valueInteger = 6
* item[6].extension[2].url = $maxValue
* item[6].extension[2].valueInteger = 23

* item[7].linkId = "braden-skintone"
* item[7].text = "Monk Skin Tone Scale rating (required — equity fairness gate: pressure-area assessment is incomplete without the patient's skin tone)"
* item[7].type = #choice
* item[7].required = true
* item[7].code = ONCObservationCodes#mst-score "Monk Skin Tone Score"
* item[7].answerValueSet = Canonical(ONCMonkScaleVS)

* item[8].linkId = "braden-banding"
* item[8].type = #display
* item[8].text = "Risk banding: 15–18 mild · 13–14 moderate · 10–12 high · ≤9 severe. On darker skin tones do not rely on redness/blanching alone — assess for localised heat, oedema, induration and pain."

// -----------------------------------------------------------------------------
// 4. Waterlow Score (pressure ulcer risk) - with embedded equity gate
// -----------------------------------------------------------------------------
Instance: onc-waterlow-questionnaire
InstanceOf: Questionnaire
Usage: #definition
Title: "Waterlow Score Capture Form"
Description: "SDC questionnaire for the Waterlow pressure-ulcer risk assessment total score, with a mandatory Monk Skin Tone item (equity fairness gate embedded at the capture layer). The total extracts to an Observation using the ONC Waterlow code; linking the skin-tone Observation via hasMember[skinTone] is the capturing app's responsibility."
* url = "https://opennursingcoreig.com/Questionnaire/onc-waterlow-questionnaire"
* name = "ONCWaterlowQuestionnaire"
* title = "Waterlow Score (Pressure Ulcer Risk)"
* status = #draft
* subjectType = #Patient
* extension[0].url = $obsExtract
* extension[0].valueBoolean = true

* item[0].linkId = "waterlow-total"
* item[0].text = "Waterlow total score (sum of all risk-factor items on the Waterlow chart)"
* item[0].type = #integer
* item[0].required = true
* item[0].code = ONCObservationCodes#waterlow-score "Waterlow Score"
* item[0].extension[0].url = $qUnit
* item[0].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[0].extension[1].url = $minValue
* item[0].extension[1].valueInteger = 0
* item[0].extension[2].url = $maxValue
* item[0].extension[2].valueInteger = 64

* item[1].linkId = "waterlow-factors"
* item[1].text = "Contributing risk factors (build/weight, skin type, continence, mobility, appetite, special risks)"
* item[1].type = #text
* item[1].required = false

* item[2].linkId = "waterlow-skintone"
* item[2].text = "Monk Skin Tone Scale rating (required — equity fairness gate: pressure-area assessment is incomplete without the patient's skin tone)"
* item[2].type = #choice
* item[2].required = true
* item[2].code = ONCObservationCodes#mst-score "Monk Skin Tone Score"
* item[2].answerValueSet = Canonical(ONCMonkScaleVS)

* item[3].linkId = "waterlow-banding"
* item[3].type = #display
* item[3].text = "Risk banding: ≥10 at risk · ≥15 high risk · ≥20 very high risk. On darker skin tones do not rely on redness/blanching alone — assess for localised heat, oedema, induration and pain."

// -----------------------------------------------------------------------------
// 5. MUST - Malnutrition Universal Screening Tool
// -----------------------------------------------------------------------------
Instance: onc-must-questionnaire
InstanceOf: Questionnaire
Usage: #definition
Title: "MUST Capture Form"
Description: "SDC questionnaire for the Malnutrition Universal Screening Tool: three step scores and the total. Coded items extract to Observations using the ONC MUST component codes; assembling them into the single component-based ONCMUSTScore Observation is the capturing app's responsibility."
* url = "https://opennursingcoreig.com/Questionnaire/onc-must-questionnaire"
* name = "ONCMUSTQuestionnaire"
* title = "MUST (Malnutrition Universal Screening Tool)"
* status = #draft
* subjectType = #Patient
* extension[0].url = $obsExtract
* extension[0].valueBoolean = true

* item[0].linkId = "must-bmi"
* item[0].text = "Step 1 — BMI score (0 = BMI >20 · 1 = BMI 18.5–20 · 2 = BMI <18.5)"
* item[0].type = #integer
* item[0].required = true
* item[0].code = ONCObservationCodes#must-bmi-score "MUST BMI Score"
* item[0].extension[0].url = $qUnit
* item[0].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[0].extension[1].url = $minValue
* item[0].extension[1].valueInteger = 0
* item[0].extension[2].url = $maxValue
* item[0].extension[2].valueInteger = 2

* item[1].linkId = "must-weight-loss"
* item[1].text = "Step 2 — Unplanned weight loss in past 3–6 months (0 = <5% · 1 = 5–10% · 2 = >10%)"
* item[1].type = #integer
* item[1].required = true
* item[1].code = ONCObservationCodes#must-weight-loss-score "MUST Weight Loss Score"
* item[1].extension[0].url = $qUnit
* item[1].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[1].extension[1].url = $minValue
* item[1].extension[1].valueInteger = 0
* item[1].extension[2].url = $maxValue
* item[1].extension[2].valueInteger = 2

* item[2].linkId = "must-acute-disease"
* item[2].text = "Step 3 — Acute disease effect (2 = acutely ill AND no nutritional intake for >5 days, or likely; otherwise 0)"
* item[2].type = #integer
* item[2].required = true
* item[2].code = ONCObservationCodes#must-acute-disease-score "MUST Acute Disease Score"
* item[2].extension[0].url = $qUnit
* item[2].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[2].extension[1].url = $minValue
* item[2].extension[1].valueInteger = 0
* item[2].extension[2].url = $maxValue
* item[2].extension[2].valueInteger = 2

* item[3].linkId = "must-total"
* item[3].text = "MUST total score (Step 1 + Step 2 + Step 3)"
* item[3].type = #integer
* item[3].required = true
* item[3].code = ONCObservationCodes#must-score "MUST Score"
* item[3].extension[0].url = $qUnit
* item[3].extension[0].valueCoding = $UCUM#"{score}" "{score}"
* item[3].extension[1].url = $minValue
* item[3].extension[1].valueInteger = 0
* item[3].extension[2].url = $maxValue
* item[3].extension[2].valueInteger = 6

* item[4].linkId = "must-actions"
* item[4].type = #display
* item[4].text = "Management: 0 = low risk — routine care, repeat screening · 1 = medium risk — observe, document intake for 3 days · ≥2 = high risk — treat: refer to dietitian/nutrition support team, set goals, monitor and review."

// -----------------------------------------------------------------------------
// 6. Person-Centred Care - What Matters to Me & Reasonable Adjustments
// -----------------------------------------------------------------------------
Instance: onc-person-centred-questionnaire
InstanceOf: Questionnaire
Usage: #definition
Title: "Person-Centred Care Capture Form"
Description: "SDC questionnaire capturing 'What Matters to Me' and reasonable adjustments (Equality Act 2010) as structured, retrievable records. Items extract to Observations conforming to ONCWhatMattersToMe and ONCReasonableAdjustment."
* url = "https://opennursingcoreig.com/Questionnaire/onc-person-centred-questionnaire"
* name = "ONCPersonCentredQuestionnaire"
* title = "Person-Centred Care (What Matters to Me & Reasonable Adjustments)"
* status = #draft
* subjectType = #Patient
* extension[0].url = $obsExtract
* extension[0].valueBoolean = true

* item[0].linkId = "what-matters"
* item[0].text = "What matters to you? (The person's own priorities and goals, in their own words — e.g. 'I want to walk my daughter down the aisle')"
* item[0].type = #text
* item[0].required = true
* item[0].code = ONCObservationCodes#what-matters "What Matters to Me"

* item[1].linkId = "reasonable-adjustment"
* item[1].text = "Reasonable adjustment required (one per entry — e.g. 'Requires a British Sign Language interpreter', 'Ground-floor appointments only', 'Requires large-print correspondence')"
* item[1].type = #text
* item[1].required = false
* item[1].repeats = true
* item[1].code = ONCObservationCodes#reasonable-adjustment "Reasonable Adjustment"

* item[2].linkId = "adjustments-note"
* item[2].type = #display
* item[2].text = "Recording adjustments as discrete, structured entries (not free-text notes) is what makes them retrievable and actionable at every subsequent encounter, in line with the Equality Act 2010 duty and the NHS reasonable-adjustment digital flag."
