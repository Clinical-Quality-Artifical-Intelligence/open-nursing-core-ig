# Example Nursing Clinical Impression - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Nursing Clinical Impression**

## Example ClinicalImpression: Example Nursing Clinical Impression

Profile: [ONC Nursing Clinical Impression](StructureDefinition-onc-nursing-clinical-impression.md)

**status**: Completed

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**date**: 2026-01-20 16:00:00+0000

**assessor**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**problem**: [Condition Risk of falls](Condition-example-nursing-problem.md)

**summary**: Mobility goal partially achieved: transfers now supervised rather than assisted. Nutrition improving with fortified diet. Pressure areas intact; continue current repositioning plan and re-evaluate in one week.



## Resource Content

```json
{
  "resourceType" : "ClinicalImpression",
  "id" : "example-clinical-impression",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-nursing-clinical-impression"]
  },
  "status" : "completed",
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "date" : "2026-01-20T16:00:00Z",
  "assessor" : {
    "reference" : "Practitioner/example-nurse"
  },
  "problem" : [{
    "reference" : "Condition/example-nursing-problem"
  }],
  "summary" : "Mobility goal partially achieved: transfers now supervised rather than assisted. Nutrition improving with fortified diet. Pressure areas intact; continue current repositioning plan and re-evaluate in one week."
}

```
