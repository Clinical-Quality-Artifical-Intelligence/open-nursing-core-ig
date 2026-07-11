# Example Glasgow Coma Scale - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Glasgow Coma Scale**

## Example Observation: Example Glasgow Coma Scale

Profile: [Glasgow Coma Scale](StructureDefinition-onc-glasgow-coma-scale.md)

**status**: Final

**category**: Survey

**code**: Glasgow coma score total

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-15 14:00:00+0000

**performer**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**value**: 14 {score}

> **component****code**: Glasgow coma score eye opening**value**: 4 {score}

> **component****code**: Glasgow coma score verbal**value**: 4 {score}

> **component****code**: Glasgow coma score motor**value**: 6 {score}



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-gcs",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-glasgow-coma-scale"]
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
      "system" : "http://loinc.org",
      "code" : "9269-2",
      "display" : "Glasgow coma score total"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-15T14:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueQuantity" : {
    "value" : 14,
    "unit" : "{score}",
    "system" : "http://unitsofmeasure.org"
  },
  "component" : [{
    "code" : {
      "coding" : [{
        "system" : "http://loinc.org",
        "code" : "9267-6",
        "display" : "Glasgow coma score eye opening"
      }]
    },
    "valueQuantity" : {
      "value" : 4,
      "unit" : "{score}",
      "system" : "http://unitsofmeasure.org"
    }
  },
  {
    "code" : {
      "coding" : [{
        "system" : "http://loinc.org",
        "code" : "9270-0",
        "display" : "Glasgow coma score verbal"
      }]
    },
    "valueQuantity" : {
      "value" : 4,
      "unit" : "{score}",
      "system" : "http://unitsofmeasure.org"
    }
  },
  {
    "code" : {
      "coding" : [{
        "system" : "http://loinc.org",
        "code" : "9268-4",
        "display" : "Glasgow coma score motor"
      }]
    },
    "valueQuantity" : {
      "value" : 6,
      "unit" : "{score}",
      "system" : "http://unitsofmeasure.org"
    }
  }]
}

```
