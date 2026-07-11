# Clinical safety and assurance gates

> **Current status: not approved for clinical deployment.**

Open Nursing Core is a pre-ballot specification with research prototypes. The
following evidence must exist before any component is represented as clinical
software.

## Required gates

- Named Clinical Safety Officer and defined deploying organisation.
- Intended use, users, care settings, exclusions and foreseeable misuse agreed.
- DCB0129 manufacturer safety case and hazard log where applicable.
- DCB0160 deployment safety case for each implementing health organisation.
- Independent review of clinical content, scoring and escalation logic.
- Traceability from every computable rule to a controlled evidence source.
- Verification against authoritative assessment tools and licensed terminology.
- Representative usability and accessibility testing with nurses and patients.
- Security threat model, penetration testing and dependency review.
- DPIA, data-flow mapping, retention rules and incident-response process.
- Model evaluation, subgroup analysis and human-oversight controls for AI.
- Versioned release, rollback, monitoring and clinical-incident processes.

## Safe evaluation conditions

Until those gates are met:

- use synthetic or appropriately de-identified data;
- keep outputs outside the legal clinical record;
- do not use outputs to trigger or suppress care automatically;
- have a qualified clinician independently verify all content; and
- label demonstrations and publications as experimental.

External review and assurance cannot be completed by repository changes alone.
Progress is tracked in [STANDARDS_ROADMAP.md](STANDARDS_ROADMAP.md).
