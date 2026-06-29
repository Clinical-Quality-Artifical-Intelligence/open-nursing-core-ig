# Example Nursing Need: Dressing Difficulty - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Nursing Need: Dressing Difficulty**

## Example Condition: Example Nursing Need: Dressing Difficulty

Profile: [ONC Nursing Need](StructureDefinition-onc-nursing-need.md)

**clinicalStatus**: Active

**verificationStatus**: Confirmed

**code**: Nursing Care Needs

**subject**: [Patient/example-patient](Patient/example-patient)

**note**: 

> 

Patient requires assistance with buttons and zippers due to arthritis.




## Resource Content

```json
{
  "resourceType" : "Condition",
  "id" : "ExampleNursingNeed-Dressing",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-nursing-need"]
  },
  "clinicalStatus" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/condition-clinical",
      "code" : "active"
    }]
  },
  "verificationStatus" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/condition-ver-status",
      "code" : "confirmed"
    }]
  },
  "code" : {
    "coding" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "nursing-needs"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "note" : [{
    "text" : "Patient requires assistance with buttons and zippers due to arthritis."
  }]
}

```
