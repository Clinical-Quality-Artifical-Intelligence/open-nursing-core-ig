# Research demonstration deployment guide

> **Not approved for clinical deployment or identifiable patient data.**

These instructions support technical evaluation with synthetic or appropriately
de-identified data. Deployment does not provide clinical assurance, regulatory
approval or information-governance approval.

## Local evaluation

1. Create an isolated Python environment.
2. Install `requirements.txt`.
3. Copy `.env.example` to `.env` and keep it outside version control.
4. Keep `APP_ENV=development` for local evaluation.
5. Initialise the database and provision an explicit test account.
6. Run `streamlit run app_phase2.py`.

There are no built-in usernames or passwords. In-memory authentication is off
by default and cannot be enabled in production.

## Hosted research environment

Before hosting:

- use a managed secret store rather than an environment file in the image;
- use an organisational identity provider with MFA;
- terminate TLS at a managed gateway;
- restrict network access and outbound connections;
- use an encrypted managed database with backups and retention controls;
- enable central audit, dependency, vulnerability and availability monitoring;
- prohibit identifiable clinical information unless the required governance is complete;
- document incident response, recovery and service ownership; and
- complete a security review and penetration test.

The supplied container is a reproducible demonstration image, not evidence
that these controls have been implemented.

## Production configuration enforcement

When `APP_ENV=production`, startup rejects:

- in-memory authentication;
- known demonstration or placeholder credentials; and
- PostgreSQL configuration without a database password.

A database outage fails authentication closed rather than falling back to an
in-memory account.

## Clinical use

Do not proceed from a technical deployment to clinical use without completing
the organisation-specific requirements in [CLINICAL_SAFETY.md](CLINICAL_SAFETY.md),
including DCB0129/DCB0160 where applicable, a DPIA, clinical content validation,
usability testing and an operational safety case.

See also [PRODUCT_BOUNDARIES.md](PRODUCT_BOUNDARIES.md) and [SECURITY.md](SECURITY.md).
