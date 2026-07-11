# Deployment status

> **Research deployment only — not approved for clinical use.**

The included deployment assets can host a technical demonstration using
synthetic or properly de-identified information. They do not establish a
clinical safety case, production identity management, information-governance
approval, operational monitoring or regulatory conformity.

Before hosting, read [PRODUCT_BOUNDARIES.md](PRODUCT_BOUNDARIES.md),
[CLINICAL_SAFETY.md](CLINICAL_SAFETY.md) and [SECURITY.md](SECURITY.md).

The application contains no built-in login credentials. Hosted environments
must provision users deliberately through a database or organisational identity
provider and supply secrets through the platform's secret manager.

For a clinical deployment, stop here and complete the assurance gates in
[CLINICAL_SAFETY.md](CLINICAL_SAFETY.md) with the deploying organisation.
