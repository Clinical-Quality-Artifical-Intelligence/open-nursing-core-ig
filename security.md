# Security & Privacy - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* **Security & Privacy**

## Security & Privacy

# Security and Privacy

Compliance with data protection regulations is mandatory for all implementations of the Open Nursing Core IG.

## Data Protection

Implementations **MUST** adhere to local data protection laws:

* **UK**: UK GDPR & Data Protection Act 2018.
* **EU**: GDPR.
* **USA**: HIPAA.

## Patient Safety & Identification

* **Anonymization**: When exchanging data for secondary uses (research, analytics), patient identifiers **MUST** be removed or pseudonymized.
* **Encryption**: All data in transit **MUST** use TLS 1.2 or higher. Data at rest **SHOULD** be encrypted.

## Access Control

* **Role-Based Access (RBAC)**: Only authorized clinical staff should access full patient records.
* **Audit Trails**: All access to patient data **MUST** be logged.

