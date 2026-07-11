# Example MMSE - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example MMSE**

## Example Observation: Example MMSE

Profile: [Mini Mental State Examination (MMSE)](StructureDefinition-onc-mmse.md)

**status**: Final

**category**: Survey

**code**: Total score [MMSE]

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-16 11:00:00+0000

**performer**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**value**: 22 {score}



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-mmse",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-mmse"]
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
      "code" : "72106-8",
      "display" : "Total score [MMSE]"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-16T11:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueQuantity" : {
    "value" : 22,
    "unit" : "{score}",
    "system" : "http://unitsofmeasure.org"
  }
}

```
