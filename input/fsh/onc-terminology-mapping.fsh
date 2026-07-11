// =============================================================================
// TERMINOLOGY MAPPING (Semantic Alignment)
// This file maps custom ONC concepts to international nursing terminologies.
// =============================================================================

ValueSet: ONCRelationalFindingsVS
Id: onc-relational-findings-vs
Title: "ONC Relational Findings"
Description: "The relational-care findings that the onc-to-nanda ConceptMap maps to formal nursing diagnoses."
* ^experimental = false
* ONCObservationCodes#patient-story "Patient Story"
* ONCObservationCodes#relational-engagement "Relational Engagement Score"
* ONCObservationCodes#mst-score "Monk Skin Tone Score"

Instance: onc-to-nanda
InstanceOf: ConceptMap
Usage: #definition
* url = "https://opennursingcoreig.com/ConceptMap/onc-to-nanda"
* name = "ONCToNandaMapping"
* title = "Mapping ONC Relational Concepts to NANDA-I"
* status = #draft
* description = "Maps Open Nursing Core clinical findings to NANDA-I Nursing Diagnoses. NOT PRODUCTION-READY: see the placeholder-canonical note below."
* sourceCanonical = "https://opennursingcoreig.com/ValueSet/onc-relational-findings-vs"
// NANDA-I is a proprietary, licensed terminology (NANDA International / Thieme) with no
// public FHIR terminology-server canonical this project controls or can point to. The URL
// below is an explicit LOCAL PLACEHOLDER under our own canonical -- it does NOT resolve to
// an official NANDA-I or HL7 THO CodeSystem. Do not treat #00053 / #00054 below as verified
// current NANDA-I codes; they illustrate the intended mapping shape only.
// Tracking: https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/123
* targetCanonical = "https://opennursingcoreig.com/CodeSystem/nanda-i-PLACEHOLDER"

// Example Mapping (illustrative only -- see placeholder note above)
* group[0].source = "https://opennursingcoreig.com/CodeSystem/onc-observation-codes"
* group[0].target = "https://opennursingcoreig.com/CodeSystem/nanda-i-PLACEHOLDER"

// Map: Patient Story narrative mentioning isolation -> NANDA Social Isolation
* group[0].element[0].code = #patient-story
* group[0].element[0].target[0].code = #00053
* group[0].element[0].target[0].display = "Social Isolation"
* group[0].element[0].target[0].equivalence = #relatedto

// Map: Relational Engagement score low -> NANDA Risk for Loneliness
* group[0].element[1].code = #relational-engagement
* group[0].element[1].target[0].code = #00054
* group[0].element[1].target[0].display = "Risk for Loneliness"
* group[0].element[1].target[0].equivalence = #relatedto

// Map: Skin Assessment finding -> SNOMED concepts for Equity
* group[0].element[2].code = #mst-score
* group[0].element[2].target[0].code = #399912005
* group[0].element[2].target[0].display = "Wound Assessment" 
* group[0].element[2].target[0].equivalence = #specializes
