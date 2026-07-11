# NEWS2 Escalation Protocol - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **NEWS2 Escalation Protocol**

## PlanDefinition: NEWS2 Escalation Protocol 

| | |
| :--- | :--- |
| *Official URL*:http://opennursingcore.org/PlanDefinition/news2-escalation | *Version*:1.0.0 |
| Active as of 2026-07-11 | *Computable Name*:NEWS2_Escalation_Protocol |

 
Computable escalation protocol for NEWS2 results, encoding the RCP response bands: 0-4 routine monitoring; 3 in any single parameter registered-nurse review; 5-6 urgent review by a clinician competent in acute illness; 7+ emergency response. 

* **Actions: **: **Url: **
  * : [NEWS2 Escalation Protocol](PlanDefinition-news2-escalation-plan.md)
* **Actions: **: **Version: **
  * : 1.0.0
* **Actions: **: **Title: **
  * : NEWS2 Escalation Protocol
* **Actions: **: **Date: **
  * : 2026-07-11 18:02:47+0000
* **Actions: **: **Publisher: **
  * : The Open Nursing Community
* **Actions: **: **Description: **
  * : Computable escalation protocol for NEWS2 results, encoding the RCP response bands: 0-4 routine monitoring; 3 in any single parameter registered-nurse review; 5-6 urgent review by a clinician competent in acute illness; 7+ emergency response.
* **Actions: **: **Libraries: **
  * : 
| |
| :--- |
| [ONC NEWS2 Auto-Calculation Logic](Library-onc-news2-cql.md) |




## Resource Content

```json
{
  "resourceType" : "PlanDefinition",
  "id" : "news2-escalation-plan",
  "url" : "http://opennursingcore.org/PlanDefinition/news2-escalation",
  "version" : "1.0.0",
  "name" : "NEWS2_Escalation_Protocol",
  "title" : "NEWS2 Escalation Protocol",
  "type" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/plan-definition-type",
      "code" : "clinical-protocol"
    }]
  },
  "status" : "active",
  "date" : "2026-07-11T18:02:47+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Computable escalation protocol for NEWS2 results, encoding the RCP response bands: 0-4 routine monitoring; 3 in any single parameter registered-nurse review; 5-6 urgent review by a clinician competent in acute illness; 7+ emergency response.",
  "library" : ["http://opennursingcore.org/Library/ONC-NEWS2-CQL"],
  "action" : [{
    "title" : "High Clinical Risk - Emergency Response",
    "description" : "NEWS2 Score of 7 or more indicates high clinical risk. Urgent response required.",
    "code" : [{
      "coding" : [{
        "system" : "http://snomed.info/sct",
        "code" : "225365006",
        "display" : "Care plan"
      }]
    }],
    "trigger" : [{
      "type" : "named-event",
      "name" : "news2-score-calculated"
    }],
    "condition" : [{
      "kind" : "applicability",
      "expression" : {
        "language" : "text/cql",
        "expression" : "Clinical Risk Category = 'High'"
      }
    }],
    "dynamicValue" : [{
      "path" : "description",
      "expression" : {
        "language" : "text/cql",
        "expression" : "'URGENT: NEWS2 Score is ' + ToString(\"NEWS2 Total Score\") + '. Immediate medical review required.'"
      }
    }]
  }]
}

```
