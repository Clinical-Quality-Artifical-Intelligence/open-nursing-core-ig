# Mapping ONC Relational Concepts to NANDA-I - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Mapping ONC Relational Concepts to NANDA-I**

## ConceptMap: Mapping ONC Relational Concepts to NANDA-I 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ConceptMap/onc-to-nanda | *Version*:1.0.0 |
| Draft as of 2026-07-04 | *Computable Name*:ONCToNandaMapping |

 
Maps Open Nursing Core clinical findings to NANDA-I Nursing Diagnoses. NOT PRODUCTION-READY: see the placeholder-canonical note below. 



## Resource Content

```json
{
  "resourceType" : "ConceptMap",
  "id" : "onc-to-nanda",
  "url" : "https://opennursingcoreig.com/ConceptMap/onc-to-nanda",
  "version" : "1.0.0",
  "name" : "ONCToNandaMapping",
  "title" : "Mapping ONC Relational Concepts to NANDA-I",
  "status" : "draft",
  "date" : "2026-07-04T09:17:49+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Maps Open Nursing Core clinical findings to NANDA-I Nursing Diagnoses. NOT PRODUCTION-READY: see the placeholder-canonical note below.",
  "sourceCanonical" : "https://opennursingcoreig.com/ValueSet/onc-relational-findings-vs",
  "targetCanonical" : "https://opennursingcoreig.com/CodeSystem/nanda-i-PLACEHOLDER",
  "group" : [{
    "source" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
    "target" : "https://opennursingcoreig.com/CodeSystem/nanda-i-PLACEHOLDER",
    "element" : [{
      "code" : "patient-story",
      "target" : [{
        "code" : "00053",
        "display" : "Social Isolation",
        "equivalence" : "relatedto"
      }]
    },
    {
      "code" : "relational-engagement",
      "target" : [{
        "code" : "00054",
        "display" : "Risk for Loneliness",
        "equivalence" : "relatedto"
      }]
    },
    {
      "code" : "skintone-observation",
      "target" : [{
        "code" : "399912005",
        "display" : "Wound Assessment",
        "equivalence" : "specializes"
      }]
    }]
  }]
}

```
