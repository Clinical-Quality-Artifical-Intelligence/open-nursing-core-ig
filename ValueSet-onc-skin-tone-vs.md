# Skin Tone Value Set - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Skin Tone Value Set**

## ValueSet: Skin Tone Value Set 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ValueSet/onc-skin-tone-vs | *Version*:1.0.0 |
| Active as of 2026-01-27 | *Computable Name*:SkinToneVS |

 
Monk and Fitzpatrick scales for equitable skin assessment. 

 **References** 

* [Relational Care Logical Model](StructureDefinition-onc-relational-care-logical.md)
* [Skin Tone Observation](StructureDefinition-onc-skintone-observation.md)

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
  "id" : "onc-skin-tone-vs",
  "url" : "https://opennursingcoreig.com/ValueSet/onc-skin-tone-vs",
  "version" : "1.0.0",
  "name" : "SkinToneVS",
  "title" : "Skin Tone Value Set",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-01-27T08:26:02+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Monk and Fitzpatrick scales for equitable skin assessment.",
  "compose" : {
    "include" : [
      {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale"
      },
      {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "filter" : [
          {
            "property" : "code",
            "op" : "is-a",
            "value" : "fitzpatrick-1"
          }
        ]
      }
    ]
  }
}

```
