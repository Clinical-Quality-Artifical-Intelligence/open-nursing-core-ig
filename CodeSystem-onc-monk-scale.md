# Monk Skin Tone Scale CodeSystem - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Monk Skin Tone Scale CodeSystem**

## CodeSystem: Monk Skin Tone Scale CodeSystem 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/CodeSystem/onc-monk-scale | *Version*:1.0.0 |
| Active as of 2026-07-11 | *Computable Name*:ONCMonkScale |

 
The ten-point (A-J) Monk Skin Tone Scale, the IG's primary vocabulary for equitable skin-tone assessment. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [ONCMonkScaleVS](ValueSet-onc-monk-scale-vs.md)
* [SkinToneVS](ValueSet-onc-skin-tone-vs.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "onc-monk-scale",
  "url" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
  "version" : "1.0.0",
  "name" : "ONCMonkScale",
  "title" : "Monk Skin Tone Scale CodeSystem",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-07-11T14:47:20+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "The ten-point (A-J) Monk Skin Tone Scale, the IG's primary vocabulary for equitable skin-tone assessment.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 10,
  "concept" : [{
    "code" : "A",
    "display" : "Light Skin"
  },
  {
    "code" : "B",
    "display" : "Light-Medium Skin"
  },
  {
    "code" : "C",
    "display" : "Medium Skin"
  },
  {
    "code" : "D",
    "display" : "Medium-Dark Skin"
  },
  {
    "code" : "E",
    "display" : "Dark Skin"
  },
  {
    "code" : "F",
    "display" : "Deep Dark Skin"
  },
  {
    "code" : "G",
    "display" : "Very Dark Skin"
  },
  {
    "code" : "H",
    "display" : "Deepest Dark Skin"
  },
  {
    "code" : "I",
    "display" : "Ultra Dark Skin"
  },
  {
    "code" : "J",
    "display" : "Black Skin"
  }]
}

```
