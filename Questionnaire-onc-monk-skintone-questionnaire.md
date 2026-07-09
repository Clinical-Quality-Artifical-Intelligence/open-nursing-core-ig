# Monk Skin Tone Capture Form - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Monk Skin Tone Capture Form**

## Questionnaire: Monk Skin Tone Capture Form 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/Questionnaire/onc-monk-skintone-questionnaire | *Version*:1.0.0 |
| Draft as of 2026-07-09 | *Computable Name*:ONCMonkSkinToneQuestionnaire |

 
SDC questionnaire capturing the patient's skin tone on the 10-point Monk Skin Tone Scale (A–J). Extracts to an Observation conforming to ONCMonkSkinToneObservation. This record is the required input to the IG's equity fairness gate for wound and pressure-area assessment. 



## Resource Content

```json
{
  "resourceType" : "Questionnaire",
  "id" : "onc-monk-skintone-questionnaire",
  "extension" : [{
    "url" : "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-observationExtract",
    "valueBoolean" : true
  }],
  "url" : "https://opennursingcoreig.com/Questionnaire/onc-monk-skintone-questionnaire",
  "version" : "1.0.0",
  "name" : "ONCMonkSkinToneQuestionnaire",
  "title" : "Monk Skin Tone Scale (A–J)",
  "status" : "draft",
  "subjectType" : ["Patient"],
  "date" : "2026-07-09T22:28:17+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "SDC questionnaire capturing the patient's skin tone on the 10-point Monk Skin Tone Scale (A–J). Extracts to an Observation conforming to ONCMonkSkinToneObservation. This record is the required input to the IG's equity fairness gate for wound and pressure-area assessment.",
  "item" : [{
    "linkId" : "mst-intro",
    "text" : "Record the skin tone that best matches the patient, assessed with the patient's involvement in good lighting. Accurate skin tone recording is a patient-safety requirement: pressure damage, cyanosis, pallor and erythema present differently across skin tones.",
    "type" : "display"
  },
  {
    "linkId" : "mst-score",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "mst-score",
      "display" : "Monk Skin Tone Score"
    }],
    "text" : "Monk Skin Tone Scale rating",
    "type" : "choice",
    "required" : true,
    "answerValueSet" : "https://opennursingcoreig.com/ValueSet/onc-monk-scale-vs"
  }]
}

```
