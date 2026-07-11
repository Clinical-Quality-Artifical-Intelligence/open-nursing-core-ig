# MUST Capture Form - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **MUST Capture Form**

## Questionnaire: MUST Capture Form 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/Questionnaire/onc-must-questionnaire | *Version*:1.0.0 |
| Draft as of 2026-07-11 | *Computable Name*:ONCMUSTQuestionnaire |

 
SDC questionnaire for the Malnutrition Universal Screening Tool: three step scores and the total. Coded items extract to Observations using the ONC MUST component codes; assembling them into the single component-based ONCMUSTScore Observation is the capturing app's responsibility. 



## Resource Content

```json
{
  "resourceType" : "Questionnaire",
  "id" : "onc-must-questionnaire",
  "extension" : [{
    "url" : "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-observationExtract",
    "valueBoolean" : true
  }],
  "url" : "https://opennursingcoreig.com/Questionnaire/onc-must-questionnaire",
  "version" : "1.0.0",
  "name" : "ONCMUSTQuestionnaire",
  "title" : "MUST (Malnutrition Universal Screening Tool)",
  "status" : "draft",
  "subjectType" : ["Patient"],
  "date" : "2026-07-11T18:02:47+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "SDC questionnaire for the Malnutrition Universal Screening Tool: three step scores and the total. Coded items extract to Observations using the ONC MUST component codes; assembling them into the single component-based ONCMUSTScore Observation is the capturing app's responsibility.",
  "item" : [{
    "extension" : [{
      "url" : "http://hl7.org/fhir/StructureDefinition/questionnaire-unit",
      "valueCoding" : {
        "system" : "http://unitsofmeasure.org",
        "code" : "{score}",
        "display" : "{score}"
      }
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/minValue",
      "valueInteger" : 0
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 2
    }],
    "linkId" : "must-bmi",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "must-bmi-score",
      "display" : "MUST BMI Score"
    }],
    "text" : "Step 1 — BMI score (0 = BMI >20 · 1 = BMI 18.5–20 · 2 = BMI <18.5)",
    "type" : "integer",
    "required" : true
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/StructureDefinition/questionnaire-unit",
      "valueCoding" : {
        "system" : "http://unitsofmeasure.org",
        "code" : "{score}",
        "display" : "{score}"
      }
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/minValue",
      "valueInteger" : 0
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 2
    }],
    "linkId" : "must-weight-loss",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "must-weight-loss-score",
      "display" : "MUST Weight Loss Score"
    }],
    "text" : "Step 2 — Unplanned weight loss in past 3–6 months (0 = <5% · 1 = 5–10% · 2 = >10%)",
    "type" : "integer",
    "required" : true
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/StructureDefinition/questionnaire-unit",
      "valueCoding" : {
        "system" : "http://unitsofmeasure.org",
        "code" : "{score}",
        "display" : "{score}"
      }
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/minValue",
      "valueInteger" : 0
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 2
    }],
    "linkId" : "must-acute-disease",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "must-acute-disease-score",
      "display" : "MUST Acute Disease Score"
    }],
    "text" : "Step 3 — Acute disease effect (2 = acutely ill AND no nutritional intake for >5 days, or likely; otherwise 0)",
    "type" : "integer",
    "required" : true
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/StructureDefinition/questionnaire-unit",
      "valueCoding" : {
        "system" : "http://unitsofmeasure.org",
        "code" : "{score}",
        "display" : "{score}"
      }
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/minValue",
      "valueInteger" : 0
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 6
    }],
    "linkId" : "must-total",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "must-score",
      "display" : "MUST Score"
    }],
    "text" : "MUST total score (Step 1 + Step 2 + Step 3)",
    "type" : "integer",
    "required" : true
  },
  {
    "linkId" : "must-actions",
    "text" : "Management: 0 = low risk — routine care, repeat screening · 1 = medium risk — observe, document intake for 3 days · ≥2 = high risk — treat: refer to dietitian/nutrition support team, set goals, monitor and review.",
    "type" : "display"
  }]
}

```
