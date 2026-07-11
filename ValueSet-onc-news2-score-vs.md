# NEWS2 Score Categories Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **NEWS2 Score Categories Value Set**

## ValueSet: NEWS2 Score Categories Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/onc-news2-score-vs | *Version*:1.0.0 |
| Active as of 2026-07-11 | *Computable Name*:NEWS2ScoreVS |

 
NEWS2 total score categories. 

 **References** 

This value set is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)

### Logical Definition (CLD)

 

### Expansion

-------

 Explanation of the columns that may appear on this page: 

| | |
| :--- | :--- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the*display*element of a[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "onc-news2-score-vs",
  "url" : "https://opennursingcoreig.com/ValueSet/onc-news2-score-vs",
  "version" : "1.0.0",
  "name" : "NEWS2ScoreVS",
  "title" : "NEWS2 Score Categories Value Set",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-07-11T18:02:47+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "NEWS2 total score categories.",
  "compose" : {
    "include" : [{
      "system" : "http://snomed.info/sct",
      "concept" : [{
        "code" : "50601000000100",
        "display" : "National Early Warning Score 2 low risk"
      },
      {
        "code" : "50602000000101",
        "display" : "National Early Warning Score 2 medium risk"
      },
      {
        "code" : "50604000000104",
        "display" : "National Early Warning Score 2 high risk"
      }]
    }]
  }
}

```
