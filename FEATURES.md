# Component status

This file records implemented capabilities without implying clinical readiness.
The definitive maturity and permitted-use boundaries are in
[PRODUCT_BOUNDARIES.md](PRODUCT_BOUNDARIES.md).

| Capability | Current state | Important limitation |
|---|---|---|
| FHIR Implementation Guide | Implemented, pre-ballot trial use | Not independently clinically reviewed or externally endorsed |
| ADPIE profiles and examples | Implemented | Implementers must validate against local workflows |
| SDC assessment questionnaires | Experimental | Rendering and usability require further testing |
| NEWS2 CQL and escalation plan | Experimental computable content | Must be verified against controlled source material and local policy |
| Streamlit application | Research prototype | Not approved for patient data or clinical decisions |
| Authentication and roles | Prototype | Not a replacement for enterprise identity, MFA or session governance |
| AI care-plan assistant | Research prototype | No autonomous clinical use; human review required |
| Virtual MDT | Research demonstration | Does not represent real multidisciplinary review |
| Equity analytics | Reference implementation | Requires governed data and local statistical review |
| Mobile client | Prototype | Not clinically deployed or assured |

No usernames or passwords are built into the application. Optional bootstrap
accounts must be explicitly configured, stored using a secret manager and
replaced with an organisational identity provider for any hosted deployment.
