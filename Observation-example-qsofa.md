# Example qSOFA - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example qSOFA**

## Example Observation: Example qSOFA

Profile: [qSOFA (Quick SOFA)](StructureDefinition-onc-qsofa.md)

**status**: Final

**category**: Survey

**code**: SOFA Total Score

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-15 08:05:00+0000

**performer**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**value**: 1 {score}



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-qsofa",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-qsofa"]
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
      "code" : "96790-1",
      "display" : "SOFA Total Score"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-15T08:05:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueQuantity" : {
    "value" : 1,
    "unit" : "{score}",
    "system" : "http://unitsofmeasure.org"
  }
}

```
