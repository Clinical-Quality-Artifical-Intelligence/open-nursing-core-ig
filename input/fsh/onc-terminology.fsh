// ==============================================================================
// VALUE SETS
// ==============================================================================

ValueSet: NursingProblemValueSet
Id: nursing-problem-valueset
Title: "Nursing Problem Value Set"
Description: "Value set for nursing problems and diagnoses"
* ^experimental = false
* include http://snomed.info/sct#129839007 "At risk for falls"
* include ONCObservationCodes#risk-falls "Risk of falls"
* include http://snomed.info/sct#300893006 "Nutritional finding"
* include http://snomed.info/sct#22253000 "Pain"

ValueSet: NursingInterventionValueSet
Id: nursing-intervention-valueset
Title: "Nursing Intervention Value Set"
Description: "Value set for nursing interventions"
* ^experimental = false
* include http://snomed.info/sct#71388002 "Procedure"
* include http://snomed.info/sct#225358003 "Wound care"
* include http://snomed.info/sct#386373004 "Nutrition therapy"

ValueSet: GoalEvaluationValueSet
Id: goal-evaluation-valueset
Title: "Goal Evaluation Value Set"
Description: "Value set for evaluating patient goal outcomes"
* ^experimental = false
* include http://snomed.info/sct#385652002 "Objective achieved"
* include http://snomed.info/sct#385651009 "Objective not achieved"
* include http://snomed.info/sct#255609007 "Partial achievement"
* include http://snomed.info/sct#723510000 "Sustained improvement"
* include http://snomed.info/sct#260388008 "Worsening"

ValueSet: ProblemCategoryValueSet
Id: problem-category-valueset
Title: "Problem Category Value Set"
Description: "Value set for categorizing nursing problems"
* ^experimental = false
* include codes from system ONCProblemType

ValueSet: SkinToneVS
Id: skintone-vs
Title: "Skin Tone Value Set"
Description: "Monk and Fitzpatrick scales for equitable skin assessment."
* ^experimental = false
* include codes from system ONCMonkScale
* include codes from system ONCObservationCodes where code is-a #fitzpatrick-1

ValueSet: NEWS2ScoreVS
Id: news2-score-vs
Title: "NEWS2 Score Categories Value Set"
Description: "Value set for NEWS2 risk categories (Low, Medium, High)."
* ^experimental = false
* include http://snomed.info/sct#50601000000100 "National Early Warning Score 2 low risk"
* include http://snomed.info/sct#50602000000101 "National Early Warning Score 2 medium risk"
* include http://snomed.info/sct#50604000000104 "National Early Warning Score 2 high risk"

ValueSet: PainScoreVS
Id: pain-score-vs
Title: "Pain Score Value Set"
Description: "Standard 0-10 or Abbey Pain Scale scores."
* ^experimental = false
* include http://snomed.info/sct#260385009 "Negative" // Equivalent to 0
* include http://snomed.info/sct#225330006 "Pain score"
* include codes from system ONCObservationCodes where code concept is-a #abbey-score

ValueSet: HousingStatusVS
Id: housing-status-vs
Title: "Housing Status Value Set"
Description: "Value set for patient housing status"
* ^experimental = false
* include http://snomed.info/sct#266935003 "Housing lack"
* include http://snomed.info/sct#224224003 "Lives in staffed home"

// ==============================================================================
// CODE SYSTEMS
// ==============================================================================

CodeSystem: ONCProblemType
Id: onc-problem-type
Title: "Problem Type CodeSystem"
Description: "Code system for categorizing types of nursing problems"
* ^url = "https://opennursingcoreig.com/CodeSystem/onc-problem-type"
* ^experimental = false
* ^caseSensitive = true
* #nursing-diagnosis "Nursing Diagnosis" "A clinical judgment about individual, family, or community responses to actual or potential health problems"
* #risk-diagnosis "Risk Diagnosis" "A clinical judgment about an individual's vulnerability to developing an undesirable health condition"
* #health-promotion "Health Promotion Diagnosis" "A clinical judgment about motivation to increase wellbeing"
