# Example Nursing Assessment (base profile) - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Nursing Assessment (base profile)**

## Example Observation: Example Nursing Assessment (base profile)

Profile: [Open Nursing Core Assessment](StructureDefinition-onc-nursing-assessment.md)

**status**: Final

**category**: Survey

**code**: Evaluation note

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-15 09:30:00+0000

**performer**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**value**: Admission review completed. Alert and orientated; independent with hygiene; appetite reduced over past week - dietitian referral discussed and accepted.



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-nursing-assessment",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-nursing-assessment"]
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
      "code" : "51848-0",
      "display" : "Evaluation note"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-15T09:30:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueString" : "Admission review completed. Alert and orientated; independent with hygiene; appetite reduced over past week - dietitian referral discussed and accepted."
}

```
