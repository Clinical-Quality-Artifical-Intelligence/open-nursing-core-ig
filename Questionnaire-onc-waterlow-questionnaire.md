# Waterlow Score Capture Form - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Waterlow Score Capture Form**

## Questionnaire: Waterlow Score Capture Form 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/Questionnaire/onc-waterlow-questionnaire | *Version*:1.0.0 |
| Draft as of 2026-07-11 | *Computable Name*:ONCWaterlowQuestionnaire |

 
SDC questionnaire for the Waterlow pressure-ulcer risk assessment total score, with a mandatory Monk Skin Tone item (equity fairness gate embedded at the capture layer). The total extracts to an Observation using the ONC Waterlow code; linking the skin-tone Observation via hasMember[skinTone] is the capturing app's responsibility. 



## Resource Content

```json
{
  "resourceType" : "Questionnaire",
  "id" : "onc-waterlow-questionnaire",
  "extension" : [{
    "url" : "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-observationExtract",
    "valueBoolean" : true
  }],
  "url" : "https://opennursingcoreig.com/Questionnaire/onc-waterlow-questionnaire",
  "version" : "1.0.0",
  "name" : "ONCWaterlowQuestionnaire",
  "title" : "Waterlow Score (Pressure Ulcer Risk)",
  "status" : "draft",
  "subjectType" : ["Patient"],
  "date" : "2026-07-11T14:17:07+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "SDC questionnaire for the Waterlow pressure-ulcer risk assessment total score, with a mandatory Monk Skin Tone item (equity fairness gate embedded at the capture layer). The total extracts to an Observation using the ONC Waterlow code; linking the skin-tone Observation via hasMember[skinTone] is the capturing app's responsibility.",
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
      "valueInteger" : 64
    }],
    "linkId" : "waterlow-total",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "waterlow-score",
      "display" : "Waterlow Score"
    }],
    "text" : "Waterlow total score (sum of all risk-factor items on the Waterlow chart)",
    "type" : "integer",
    "required" : true
  },
  {
    "linkId" : "waterlow-factors",
    "text" : "Contributing risk factors (build/weight, skin type, continence, mobility, appetite, special risks)",
    "type" : "text",
    "required" : false
  },
  {
    "linkId" : "waterlow-skintone",
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
    "linkId" : "waterlow-banding",
    "text" : "Risk banding: ≥10 at risk · ≥15 high risk · ≥20 very high risk. On darker skin tones do not rely on redness/blanching alone — assess for localised heat, oedema, induration and pain.",
    "type" : "display"
  }]
}

```
