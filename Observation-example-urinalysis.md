# example-urinalysis - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-urinalysis**

## Example Observation: example-urinalysis

Profile: [Urinalysis](StructureDefinition-onc-urinalysis.md)

**status**: Final

**category**: Survey

**code**: Urinalysis Panel

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2026-01-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Suggestive of UTI

> **component****code**: Leukocytes**value**: ++

> **component****code**: Nitrites**value**: Positive

> **component****code**: Blood**value**: Negative

> **component****code**: pH**value**: 6 {pH}



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-urinalysis",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-urinalysis"]
  },
  "status" : "final",
  "category" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
      "code" : "survey"
    }]
  }],
  "code" : {
    "coding" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "urinalysis-panel"
    }]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "effectiveDateTime" : "2026-01-15T10:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/practitioner-example"
  }],
  "valueString" : "Suggestive of UTI",
  "component" : [{
    "code" : {
      "coding" : [{
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "code" : "ua-leukocytes"
      }]
    },
    "valueString" : "++"
  },
  {
    "code" : {
      "coding" : [{
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "code" : "ua-nitrites"
      }]
    },
    "valueString" : "Positive"
  },
  {
    "code" : {
      "coding" : [{
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "code" : "ua-blood"
      }]
    },
    "valueString" : "Negative"
  },
  {
    "code" : {
      "coding" : [{
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "code" : "ua-ph"
      }]
    },
    "valueQuantity" : {
      "value" : 6,
      "unit" : "{pH}"
    }
  }]
}

```
