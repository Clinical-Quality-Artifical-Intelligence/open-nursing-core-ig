# Person-Centred Care Capture Form - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Person-Centred Care Capture Form**

## Questionnaire: Person-Centred Care Capture Form 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/Questionnaire/onc-person-centred-questionnaire | *Version*:1.0.0 |
| Draft as of 2026-07-11 | *Computable Name*:ONCPersonCentredQuestionnaire |

 
SDC questionnaire capturing 'What Matters to Me' and reasonable adjustments (Equality Act 2010) as structured, retrievable records. Items extract to Observations conforming to ONCWhatMattersToMe and ONCReasonableAdjustment. 



## Resource Content

```json
{
  "resourceType" : "Questionnaire",
  "id" : "onc-person-centred-questionnaire",
  "extension" : [{
    "url" : "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-observationExtract",
    "valueBoolean" : true
  }],
  "url" : "https://opennursingcoreig.com/Questionnaire/onc-person-centred-questionnaire",
  "version" : "1.0.0",
  "name" : "ONCPersonCentredQuestionnaire",
  "title" : "Person-Centred Care (What Matters to Me & Reasonable Adjustments)",
  "status" : "draft",
  "subjectType" : ["Patient"],
  "date" : "2026-07-11T14:02:42+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "SDC questionnaire capturing 'What Matters to Me' and reasonable adjustments (Equality Act 2010) as structured, retrievable records. Items extract to Observations conforming to ONCWhatMattersToMe and ONCReasonableAdjustment.",
  "item" : [{
    "linkId" : "what-matters",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "what-matters",
      "display" : "What Matters to Me"
    }],
    "text" : "What matters to you? (The person's own priorities and goals, in their own words — e.g. 'I want to walk my daughter down the aisle')",
    "type" : "text",
    "required" : true
  },
  {
    "linkId" : "reasonable-adjustment",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "reasonable-adjustment",
      "display" : "Reasonable Adjustment"
    }],
    "text" : "Reasonable adjustment required (one per entry — e.g. 'Requires a British Sign Language interpreter', 'Ground-floor appointments only', 'Requires large-print correspondence')",
    "type" : "text",
    "required" : false,
    "repeats" : true
  },
  {
    "linkId" : "adjustments-note",
    "text" : "Recording adjustments as discrete, structured entries (not free-text notes) is what makes them retrievable and actionable at every subsequent encounter, in line with the Equality Act 2010 duty and the NHS reasonable-adjustment digital flag.",
    "type" : "display"
  }]
}

```
