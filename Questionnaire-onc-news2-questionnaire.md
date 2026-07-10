# NEWS2 Capture Form - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **NEWS2 Capture Form**

## Questionnaire: NEWS2 Capture Form 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/Questionnaire/onc-news2-questionnaire | *Version*:1.0.0 |
| Draft as of 2026-07-10 | *Computable Name*:ONCNEWS2Questionnaire |

 
SDC questionnaire for capturing the NEWS2 physiological parameter set and total score. Coded items extract to Observations conforming to the ONC NEWS2 and vital-sign profiles. Scoring and escalation logic is computable via the ONC_NEWS2_Logic CQL library and the news2-escalation PlanDefinition. 



## Resource Content

```json
{
  "resourceType" : "Questionnaire",
  "id" : "onc-news2-questionnaire",
  "extension" : [{
    "url" : "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-observationExtract",
    "valueBoolean" : true
  }],
  "url" : "https://opennursingcoreig.com/Questionnaire/onc-news2-questionnaire",
  "version" : "1.0.0",
  "name" : "ONCNEWS2Questionnaire",
  "title" : "NEWS2 (National Early Warning Score 2)",
  "status" : "draft",
  "subjectType" : ["Patient"],
  "date" : "2026-07-10T11:01:35+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "SDC questionnaire for capturing the NEWS2 physiological parameter set and total score. Coded items extract to Observations conforming to the ONC NEWS2 and vital-sign profiles. Scoring and escalation logic is computable via the ONC_NEWS2_Logic CQL library and the news2-escalation PlanDefinition.",
  "item" : [{
    "extension" : [{
      "url" : "http://hl7.org/fhir/StructureDefinition/questionnaire-unit",
      "valueCoding" : {
        "system" : "http://unitsofmeasure.org",
        "code" : "/min",
        "display" : "/min"
      }
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/minValue",
      "valueInteger" : 0
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 90
    }],
    "linkId" : "resp-rate",
    "code" : [{
      "system" : "http://loinc.org",
      "code" : "9279-1",
      "display" : "Respiratory rate"
    }],
    "text" : "Respiration rate (breaths per minute)",
    "type" : "integer",
    "required" : true
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/StructureDefinition/questionnaire-unit",
      "valueCoding" : {
        "system" : "http://unitsofmeasure.org",
        "code" : "%",
        "display" : "%"
      }
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/minValue",
      "valueInteger" : 0
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 100
    }],
    "linkId" : "spo2",
    "code" : [{
      "system" : "http://loinc.org",
      "code" : "59408-5",
      "display" : "Oxygen saturation in Arterial blood by Pulse oximetry"
    }],
    "text" : "Oxygen saturation, SpO2 (%)",
    "type" : "integer",
    "required" : true
  },
  {
    "linkId" : "spo2-scale2",
    "text" : "Use SpO2 Scale 2? (Prescribed target saturation 88–92%, e.g. hypercapnic respiratory failure — decision made by a competent clinician)",
    "type" : "boolean",
    "required" : true
  },
  {
    "linkId" : "o2-status",
    "code" : [{
      "system" : "http://loinc.org",
      "code" : "3151-8",
      "display" : "Inhaled oxygen flow rate"
    }],
    "text" : "Air or supplemental oxygen?",
    "type" : "choice",
    "required" : true,
    "answerOption" : [{
      "valueCoding" : {
        "system" : "http://snomed.info/sct",
        "code" : "722742002",
        "display" : "Breathing room air"
      }
    },
    {
      "valueCoding" : {
        "system" : "http://snomed.info/sct",
        "code" : "371825009",
        "display" : "Patient on oxygen"
      }
    }]
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/StructureDefinition/questionnaire-unit",
      "valueCoding" : {
        "system" : "http://unitsofmeasure.org",
        "code" : "mm[Hg]",
        "display" : "mm[Hg]"
      }
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/minValue",
      "valueInteger" : 20
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 300
    }],
    "linkId" : "systolic-bp",
    "code" : [{
      "system" : "http://loinc.org",
      "code" : "8480-6",
      "display" : "Systolic blood pressure"
    }],
    "text" : "Systolic blood pressure (mmHg)",
    "type" : "integer",
    "required" : true
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/StructureDefinition/questionnaire-unit",
      "valueCoding" : {
        "system" : "http://unitsofmeasure.org",
        "code" : "mm[Hg]",
        "display" : "mm[Hg]"
      }
    }],
    "linkId" : "diastolic-bp",
    "code" : [{
      "system" : "http://loinc.org",
      "code" : "8462-4",
      "display" : "Diastolic blood pressure"
    }],
    "text" : "Diastolic blood pressure (mmHg) — recorded, not scored",
    "type" : "integer",
    "required" : false
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/StructureDefinition/questionnaire-unit",
      "valueCoding" : {
        "system" : "http://unitsofmeasure.org",
        "code" : "/min",
        "display" : "/min"
      }
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/minValue",
      "valueInteger" : 0
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueInteger" : 350
    }],
    "linkId" : "heart-rate",
    "code" : [{
      "system" : "http://loinc.org",
      "code" : "8867-4",
      "display" : "Heart rate"
    }],
    "text" : "Pulse / heart rate (beats per minute)",
    "type" : "integer",
    "required" : true
  },
  {
    "extension" : [{
      "url" : "http://hl7.org/fhir/StructureDefinition/questionnaire-unit",
      "valueCoding" : {
        "system" : "http://unitsofmeasure.org",
        "code" : "Cel",
        "display" : "Cel"
      }
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/minValue",
      "valueDecimal" : 25
    },
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/maxValue",
      "valueDecimal" : 45
    }],
    "linkId" : "temperature",
    "code" : [{
      "system" : "http://loinc.org",
      "code" : "8310-5",
      "display" : "Body temperature"
    }],
    "text" : "Body temperature (°C)",
    "type" : "decimal",
    "required" : true
  },
  {
    "linkId" : "acvpu",
    "code" : [{
      "system" : "http://snomed.info/sct",
      "code" : "1104441000000107",
      "display" : "ACVPU (Alert Confusion Voice Pain Unresponsive) scale score"
    }],
    "text" : "Level of consciousness (ACVPU)",
    "type" : "choice",
    "required" : true,
    "answerOption" : [{
      "valueCoding" : {
        "system" : "http://snomed.info/sct",
        "code" : "248234008",
        "display" : "Mentally alert"
      }
    },
    {
      "valueCoding" : {
        "system" : "http://snomed.info/sct",
        "code" : "130987000",
        "display" : "Acute confusion"
      }
    },
    {
      "valueCoding" : {
        "system" : "http://snomed.info/sct",
        "code" : "300202002",
        "display" : "Responds to voice"
      }
    },
    {
      "valueCoding" : {
        "system" : "http://snomed.info/sct",
        "code" : "450847001",
        "display" : "Responds to pain"
      }
    },
    {
      "valueCoding" : {
        "system" : "http://snomed.info/sct",
        "code" : "422768004",
        "display" : "Unresponsive"
      }
    }]
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
      "valueInteger" : 20
    }],
    "linkId" : "news2-total",
    "code" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "news2-score",
      "display" : "NEWS2 Score"
    }],
    "text" : "NEWS2 total score (0–20)",
    "type" : "integer",
    "required" : true
  },
  {
    "linkId" : "escalation-guidance",
    "text" : "Escalation (RCP NEWS2): 0–4 low risk — routine monitoring · 3 in any single parameter — registered nurse review · 5–6 medium risk — urgent review by a clinician competent in acute illness · 7+ high risk — emergency response. The ONC_NEWS2_Logic CQL library computes the score and the news2-escalation PlanDefinition encodes this protocol; this form does not replace clinical judgement.",
    "type" : "display"
  }]
}

```
