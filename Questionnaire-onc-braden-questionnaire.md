# Braden Scale Capture Form - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Braden Scale Capture Form**

## Questionnaire: Braden Scale Capture Form 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/Questionnaire/onc-braden-questionnaire | *Version*:1.0.0 |
| Draft as of 2026-07-11 | *Computable Name*:ONCBradenQuestionnaire |

 
SDC questionnaire for the Braden pressure-ulcer risk assessment: six subscales, total score, and a mandatory Monk Skin Tone item (the equity fairness gate is embedded at the capture layer). Coded items extract to Observations using the ONC Braden component codes; assembling them into the single component-based ONCBradenScaleAssessment Observation (including hasMember[skinTone]) is the capturing app's responsibility. 



## Resource Content

```json
{
  "resourceType" : "Questionnaire",
  "id" : "onc-braden-questionnaire",
  "extension" : [{
    "url" : "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-observationExtract",
    "valueBoolean" : true
  }],
  "url" : "https://opennursingcoreig.com/Questionnaire/onc-braden-questionnaire",
  "version" : "1.0.0",
  "name" : "ONCBradenQuestionnaire",
  "title" : "Braden Scale (Pressure Ulcer Risk)",
  "status" : "draft",
  "subjectType" : ["Patient"],
  "date" : "2026-07-11T14:17:07+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "SDC questionnaire for the Braden pressure-ulcer risk assessment: six subscales, total score, and a mandatory Monk Skin Tone item (the equity fairness gate is embedded at the capture layer). Coded items extract to Observations using the ONC Braden component codes; assembling them into the single component-based ONCBradenScaleAssessment Observation (including hasMember[skinTone]) is the capturing app's responsibility.",
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
      "valueInteger" : 1
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 4
    }],
    "linkId" : "braden-sensory",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "braden-sensory",
      "display" : "Braden Sensory Perception"
    }],
    "text" : "Sensory perception (1 = Completely limited · 2 = Very limited · 3 = Slightly limited · 4 = No impairment)",
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
      "valueInteger" : 1
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 4
    }],
    "linkId" : "braden-moisture",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "braden-moisture",
      "display" : "Braden Moisture"
    }],
    "text" : "Moisture (1 = Constantly moist · 2 = Very moist · 3 = Occasionally moist · 4 = Rarely moist)",
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
      "valueInteger" : 1
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 4
    }],
    "linkId" : "braden-activity",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "braden-activity",
      "display" : "Braden Activity"
    }],
    "text" : "Activity (1 = Bedfast · 2 = Chairfast · 3 = Walks occasionally · 4 = Walks frequently)",
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
      "valueInteger" : 1
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 4
    }],
    "linkId" : "braden-mobility",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "braden-mobility",
      "display" : "Braden Mobility"
    }],
    "text" : "Mobility (1 = Completely immobile · 2 = Very limited · 3 = Slightly limited · 4 = No limitation)",
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
      "valueInteger" : 1
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 4
    }],
    "linkId" : "braden-nutrition",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "braden-nutrition",
      "display" : "Braden Nutrition"
    }],
    "text" : "Nutrition (1 = Very poor · 2 = Probably inadequate · 3 = Adequate · 4 = Excellent)",
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
      "valueInteger" : 1
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 3
    }],
    "linkId" : "braden-friction",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "braden-friction",
      "display" : "Braden Friction/Shear"
    }],
    "text" : "Friction and shear (1 = Problem · 2 = Potential problem · 3 = No apparent problem)",
    "type" : "integer",
    "required" : true
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/StructureDefinition/questionnaire-unit",
      "valueCoding" : {
        "system" : "http://unitsofmeasure.org",
        "code" : "1",
        "display" : "{score}"
      }
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/minValue",
      "valueInteger" : 6
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 23
    }],
    "linkId" : "braden-total",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "braden-total-score",
      "display" : "Braden Total Score"
    }],
    "text" : "Braden total score (6–23; lower = higher risk)",
    "type" : "integer",
    "required" : true
  },
  {
    "linkId" : "braden-skintone",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "mst-score",
      "display" : "Monk Skin Tone Score"
    }],
    "text" : "Monk Skin Tone Scale rating (required — equity fairness gate: pressure-area assessment is incomplete without the patient's skin tone)",
    "type" : "choice",
    "required" : true,
    "answerOption" : [{
      "valueCoding" : {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
        "code" : "A",
        "display" : "Light Skin"
      }
    },
    {
      "valueCoding" : {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
        "code" : "B",
        "display" : "Light-Medium Skin"
      }
    },
    {
      "valueCoding" : {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
        "code" : "C",
        "display" : "Medium Skin"
      }
    },
    {
      "valueCoding" : {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
        "code" : "D",
        "display" : "Medium-Dark Skin"
      }
    },
    {
      "valueCoding" : {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
        "code" : "E",
        "display" : "Dark Skin"
      }
    },
    {
      "valueCoding" : {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
        "code" : "F",
        "display" : "Deep Dark Skin"
      }
    },
    {
      "valueCoding" : {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
        "code" : "G",
        "display" : "Very Dark Skin"
      }
    },
    {
      "valueCoding" : {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
        "code" : "H",
        "display" : "Deepest Dark Skin"
      }
    },
    {
      "valueCoding" : {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
        "code" : "I",
        "display" : "Ultra Dark Skin"
      }
    },
    {
      "valueCoding" : {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
        "code" : "J",
        "display" : "Black Skin"
      }
    }]
  },
  {
    "linkId" : "braden-banding",
    "text" : "Risk banding: 15–18 mild · 13–14 moderate · 10–12 high · ≤9 severe. On darker skin tones do not rely on redness/blanching alone — assess for localised heat, oedema, induration and pain.",
    "type" : "display"
  }]
}

```
