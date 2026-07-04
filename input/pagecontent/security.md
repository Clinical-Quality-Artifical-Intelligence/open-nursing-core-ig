# Security & Privacy

Nursing records contain some of the most sensitive personal data an organisation holds. Every implementation of the Open Nursing Core IG must protect that data throughout its lifecycle. This page sets out the governance framework and the technical controls expected of conformant systems, with particular reference to the United Kingdom and NHS context.

## Legal and regulatory framework

Implementations **MUST** comply with the data protection law applicable in their jurisdiction:

- **United Kingdom** — the **UK GDPR** and the **Data Protection Act 2018**. Health data is "special category" personal data and requires an Article 9 lawful basis in addition to an Article 6 basis.
- **European Union** — the GDPR.
- **United States** — HIPAA, where applicable.

## NHS information governance

Organisations operating within the NHS in England **MUST** additionally satisfy national information-governance requirements:

- **Data Security and Protection Toolkit (DSPT)** — the mandatory annual self-assessment against the National Data Guardian's ten data-security standards. Completion of the DSPT is a precondition for connecting to national systems.
- **The Caldicott Principles** — the eight principles governing the use of confidential patient information, including that access is on a strict need-to-know basis and that the duty to share information for care can be as important as the duty to protect confidentiality.
- **National Data Opt-Out** — patients' choices about the use of their confidential information for purposes beyond their direct care must be respected.

Each organisation should have a nominated **Caldicott Guardian** and a **Data Protection Officer**.

## Technical controls

### Access control
- **Role-based access control (RBAC)** — access to patient records **MUST** be limited to authorised staff with a legitimate care relationship.
- **Audit trails** — all access to, and modification of, patient data **MUST** be logged in a tamper-evident audit record, and those logs must be retained and reviewable.

### Data in transit and at rest
- **Encryption in transit** — all exchange of patient data **MUST** use TLS 1.2 or higher.
- **Encryption at rest** — stored patient data **SHOULD** be encrypted.

### Secondary use and de-identification
- When data is used for research, service evaluation or analytics, direct identifiers **MUST** be removed or pseudonymised, and the minimum necessary data used.
- Re-identification risk must be assessed before any onward sharing.

## Patient dignity and visibility

Protecting data is not only a technical duty. The equity and relational features of this IG — reasonable adjustments, "What Matters to Me", ethnicity and skin-tone records — carry information that, handled carelessly, could expose a person to discrimination or distress. Access to these fields **SHOULD** be governed with the same rigour as any other sensitive record, and their purpose is always to *improve* the person's care, never to label them.

---

*This page describes governance expectations for implementers; it is not legal advice. Each organisation is responsible for its own Data Protection Impact Assessment and information-governance sign-off.*
