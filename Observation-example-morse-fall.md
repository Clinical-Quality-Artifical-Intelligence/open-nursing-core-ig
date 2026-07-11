# Example Morse Fall Scale - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Morse Fall Scale**

## Example Observation: Example Morse Fall Scale

Profile: [Morse Fall Scale](StructureDefinition-onc-morse-fall-scale.md)

**status**: Final

**category**: Survey

**code**: Fall risk assessment

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-15 10:30:00+0000

**performer**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**value**: 55 {score}



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-morse-fall",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-morse-fall-scale"]
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
      "code" : "73830-2",
      "display" : "Fall risk assessment"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-15T10:30:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueQuantity" : {
    "value" : 55,
    "unit" : "{score}",
    "system" : "http://unitsofmeasure.org"
  }
}

```
