# Mapping ONC Relational Concepts to NANDA-I - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Mapping ONC Relational Concepts to NANDA-I**

## ConceptMap: Mapping ONC Relational Concepts to NANDA-I 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ConceptMap/onc-to-nanda | *Version*:1.0.0 |
| Draft as of 2026-01-27 | *Computable Name*:ONCToNandaMapping |

 
Maps Open Nursing Core clinical findings to NANDA-I Nursing Diagnoses. 



## Resource Content

```json
{
  "resourceType" : "ConceptMap",
  "id" : "ONCToNandaMapping",
  "url" : "https://opennursingcoreig.com/ConceptMap/onc-to-nanda",
  "version" : "1.0.0",
  "name" : "ONCToNandaMapping",
  "title" : "Mapping ONC Relational Concepts to NANDA-I",
  "status" : "draft",
  "date" : "2026-01-27T01:09:05+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Maps Open Nursing Core clinical findings to NANDA-I Nursing Diagnoses.",
  "sourceCanonical" : "https://opennursingcoreig.com/ValueSet/onc-relational-findings-vs",
  "targetCanonical" : "http://terminology.hl7.org/CodeSystem/nanda-i",
  "group" : [
    {
      "source" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "target" : "http://terminology.hl7.org/CodeSystem/nanda-i",
      "element" : [
        {
          "code" : "patient-story",
          "target" : [
            {
              "code" : "00053",
              "display" : "Social Isolation",
              "equivalence" : "relatedto"
            }
          ]
        },
        {
          "code" : "relational-engagement",
          "target" : [
            {
              "code" : "00054",
              "display" : "Risk for Loneliness",
              "equivalence" : "relatedto"
            }
          ]
        },
        {
          "code" : "skintone-observation",
          "target" : [
            {
              "code" : "399912005",
              "display" : "Wound Assessment",
              "equivalence" : "specializes"
            }
          ]
        }
      ]
    }
  ]
}

```
