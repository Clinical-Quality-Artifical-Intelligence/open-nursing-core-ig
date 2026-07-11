# Example Wound Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Wound Assessment**

## Example Observation: Example Wound Assessment

Profile: [Wound Assessment](StructureDefinition-onc-wound-assessment.md)

**ONC Equity Marker**: true

**status**: Final

**category**: Survey

**code**: Pressure Ulcer

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-15 11:00:00+0000

**performer**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**value**: Stage 2

**hasMember**: [Observation Skin type [Fitzpatrick Classification Scale]](Observation-observation-skin-tone.md)

> **component****code**: Length**value**: 3.5 cm

> **component****code**: Width of wound**value**: 2 cm



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-wound-assessment",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-wound-assessment"]
  },
  "extension" : [{
    "url" : "https://opennursingcoreig.com/StructureDefinition/onc-equity-marker",
    "valueBoolean" : true
  }],
  "status" : "final",
  "category" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
      "code" : "survey"
    }]
  }],
  "code" : {
    "coding" : [{
      "system" : "http://snomed.info/sct",
      "code" : "399912005",
      "display" : "Pressure Ulcer"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-15T11:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueCodeableConcept" : {
    "coding" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "stage-2",
      "display" : "Stage 2"
    }]
  },
  "hasMember" : [{
    "reference" : "Observation/observation-skin-tone"
  }],
  "component" : [{
    "code" : {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "410668003",
        "display" : "Length"
      }]
    },
    "valueQuantity" : {
      "value" : 3.5,
      "unit" : "cm"
    }
  },
  {
    "code" : {
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "401239006",
        "display" : "Width of wound"
      }]
    },
    "valueQuantity" : {
      "value" : 2,
      "unit" : "cm"
    }
  }]
}

```
