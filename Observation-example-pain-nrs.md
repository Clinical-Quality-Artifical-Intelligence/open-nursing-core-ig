# Example Pain Assessment (NRS) - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Pain Assessment (NRS)**

## Example Observation: Example Pain Assessment (NRS)

Profile: [Pain Assessment (NRS 0-10)](StructureDefinition-onc-pain-assessment.md)

**status**: Final

**category**: Survey

**code**: Pain severity - 0-10 verbal numeric rating [Score] - Reported

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-15 12:15:00+0000

**performer**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**value**: 6 {score}

**bodySite**: Left hip, worse on movement



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-pain-nrs",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-pain-assessment"]
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
      "code" : "72514-3",
      "display" : "Pain severity - 0-10 verbal numeric rating [Score] - Reported"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-15T12:15:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueQuantity" : {
    "value" : 6,
    "unit" : "{score}",
    "system" : "http://unitsofmeasure.org"
  },
  "bodySite" : {
    "text" : "Left hip, worse on movement"
  }
}

```
