# PhD Research Proposal

**Project Title:** Algorithmic Justice for Cognitive Diversity: Building and Validating an AI Safety Framework for People with Learning Disabilities

**Applicant:** Lincoln Gombedza, RN (Learning Disability)

**Proposed Supervisors:** 
- Prof. Calvin Moorley (Lead Supervisor, LSBU) - Social justice, intersectionality
- Dr. Helena Hailu Habte-Asres (Co-Supervisor, KCL) - Clinical outcomes, health inequalities

**Mode of Study:** Full-time (3 years) or Part-time (4 years)

---

## Abstract

**Background:**

Artificial Intelligence is reshaping NHS healthcare [31], yet no systematic approach exists to ensure AI technologies are safe and accessible for the 1.5 million people with Learning Disabilities in the UK [4]. Current AI systems exhibit documented "ability bias"—systematically underestimating cognitive diversity and perpetuating diagnostic overshadowing [10, 15]. People with Learning Disabilities face 15-20 years reduced life expectancy from preventable causes [1, 5]. Without intervention, NHS AI adoption risks automating these inequalities at population scale.

**Aim:**

To build and validate the Cognitive Justice AI Safety Framework (CJ-ASF): a technical and governance approach ensuring AI technologies do not harm people with Learning Disabilities.

**Methods:**

This research uses Design Science Research methodology—creating a practical artifact (the CJ-ASF) through iterative cycles of design, implementation, and evaluation. Phase 1 (Year 1): Co-design framework components with people with Learning Disabilities through participatory action research, producing draft safety requirements, accessibility standards, and bias detection methods. Phase 2 (Year 2): Implement CJ-ASF as a technical validation toolkit, building on the applicant's existing open-source infrastructure (Open Nursing Core, NHS Unified Nursing Validator). Phase 3 (Year 3): Validate framework through multi-site testing with NHS AI systems, measuring detection of accessibility failures and algorithmic bias using mixed-methods evaluation.

**Impact:**

The CJ-ASF will provide NHS organizations with practical tools to audit AI technologies before deployment, protecting people with Learning Disabilities from algorithmic harm. Unlike literature-based frameworks, CJ-ASF produces working software and governance protocols testable in real procurement contexts.

---

## 1. Background and Rationale

### 1.1 The Scale of the Problem

The UK has approximately 1.5 million people with Learning Disabilities [4]. This population experiences:
- **15-20 years shorter life expectancy** [1, 5]
- **40-50% preventable factors in deaths** [2]
- **Diagnostic overshadowing:** Physical symptoms dismissed as "behavioral" manifestations of disability [6, 7, 8]

The NHS Long Term Plan prioritizes digital transformation [31]. AI is being deployed across clinical pathways—triage algorithms, symptom checkers, documentation tools, decision-support systems [35]. These technologies are approved based on performance in neurotypical populations [33].

**The risk:** AI systems that work for the majority may systematically fail, exclude, or harm people with cognitive diversity.

### 1.2 Evidence of AI Harm for People with Learning Disabilities

Recent research (2024-2025) documents concrete harms:

**Ability Bias:**
Generative AI chatbots (ChatGPT, Gemini) underestimate disability, associating people with LD with fewer favorable characteristics [10, 15]. When processing health scenarios involving LD patients, AI systems:
- Attribute symptoms to disability rather than medical causes [14]
- Generate inaccessibly complex outputs [11]
- Miss atypical illness presentations [12]

**Exclusionary Design:**
AI-powered patient portals, symptom checkers, and telehealth platforms assume:
- Literacy and numeracy
- Abstract reasoning
- Independent technology navigation

These assumptions create systematic exclusion—violating the Equality Act 2010 [36, 39].

**Algorithmic Discrimination:**
Clinical decision-support algorithms exhibit disability bias, affecting resource allocation and care pathways [11, 12]. People with LD are deprioritized based on implicit "quality of life" assumptions embedded in training data [10, 13].

### 1.3 Why Technical Artifacts, Not Just Guidelines

Existing approaches to AI ethics produce **policy documents** and **checklists**. These have limited practical impact because:
- Developers lack technical tools to operationalize principles
- Procurement teams lack methods to verify compliance
- Bias remains invisible without automated detection

This research produces **working software and validation methods**—moving from aspirational guidelines to testable technical standards.

### 1.4 Applicant's Existing Technical Foundation

The applicant has already built open-source infrastructure demonstrating capability:

1. **Open Nursing Core (ONC):** FHIR Implementation Guide for nursing documentation (8 languages)
2. **NHS Unified Nursing Validator:** REST API for validating clinical data against standards
3. **nursing-llama-3-8b-fons:** Fine-tuned LLM with documented accessibility performance

This existing infrastructure provides the technical foundation for CJ-ASF development, demonstrating feasibility and reducing project risk.

---

## 2. Theoretical Framework

### 2.1 Algorithmic Justice

Drawing on critical data studies and disability rights scholarship [36, 37], this research positions AI evaluation as a justice concern:

**Distributive Justice:** Are AI benefits and harms equitably distributed across cognitive diversity?

**Procedural Justice:** Are people with LD included in AI design, testing, and governance?

**Epistemic Justice:** Are LD perspectives recognized as valid knowledge in AI development? [38]

Prof. Moorley's work on intersectionality [24, 25] informs analysis of how LD intersects with race, class, and other marginalized identities [26, 27] to produce compounded algorithmic harms.

### 2.2 Universal Design vs. Reasonable Adjustments

Rather than "retrofitting" accessibility, CJ-ASF embeds cognitive accessibility as foundational design principle. This shifts from:
- "Does this AI work?" → "Does this AI work for everyone?"
- "Can we add accommodations?" → "Who was excluded by design?"

### 2.3 Health Equity

Dr. Habte-Asres's research on health inequalities [28] informs clinical outcome metrics. CJ-ASF evaluates whether AI technologies reduce or widen health gaps for LD populations [29, 30].

---

## 3. Aim and Objectives

### 3.1 Aim

To build and validate the Cognitive Justice AI Safety Framework (CJ-ASF): a technical and governance toolkit ensuring AI technologies are safe, accessible, and equitable for people with Learning Disabilities.

### 3.2 Objectives

1. **Co-design** CJ-ASF safety requirements and accessibility standards through participatory action research with people with LD

2. **Build** a technical validation toolkit extending the applicant's existing open-source infrastructure to detect:
   - Accessibility failures
   - Ability bias in AI outputs
   - Diagnostic overshadowing patterns
   
3. **Validate** CJ-ASF through multi-site testing with NHS AI technologies, evaluating:
   - Detection accuracy (does CJ-ASF identify real harms?)
   - Practical utility (can procurement teams use it?)
   - Clinical relevance (does detection predict real-world impact?)

4. **Produce** implementation guidance for NHS organizations, AI developers, and clinical governance teams

---

## 4. Methodology: Design Science Research

### 4.1 Why Design Science Research?

Design Science Research (DSR) creates and evaluates artifacts to solve identified problems. Unlike literature reviews or observational studies, DSR produces practical tools validated through use.

DSR is appropriate because:
- The applicant has already built foundational artifacts (proof of feasibility)
- The problem requires technical solutions, not just analysis
- NHS needs practical tools, not more theoretical frameworks
- Validation through implementation tests real-world utility

### 4.2 DSR Cycle

```
┌──────────────────────────────────────────────────────────┐
│                  PROBLEM IDENTIFICATION                  │
│   AI technologies harm people with Learning Disabilities │
└───────────────────────────┬──────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────┐
│                      DESIGN CYCLE                        │
│                                                          │
│  ┌─────────────┐    ┌──────────────┐    ┌────────────┐  │
│  │  CO-DESIGN  │───▶│    BUILD     │───▶│  EVALUATE  │  │
│  │  with LD    │    │  Technical   │    │  Multi-site│  │
│  │  Community  │    │  Toolkit     │    │  Testing   │  │
│  └─────────────┘    └──────────────┘    └────────────┘  │
│         ▲                                      │         │
│         └──────────── ITERATE ─────────────────┘         │
└──────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────┐
│                    KNOWLEDGE OUTPUT                      │
│   CJ-ASF Framework + Toolkit + Implementation Guidance   │
└──────────────────────────────────────────────────────────┘
```

---

## 5. Research Plan

### Phase 1: Co-Design (Year 1)

**Objective:** Develop CJ-ASF safety requirements and accessibility standards through participatory research with LD communities.

**5.1.1 Participatory Action Research with People with LD (Months 1-8)**

**Recruitment:**
- 15-20 people with Learning Disabilities as co-researchers
- Through self-advocacy organizations (Mencap, CHANGE, local groups)
- Diverse in LD severity, communication methods, age, ethnicity

**Co-Research Process:**
- 6 participatory workshops (bi-monthly, Months 1-8)
- Each workshop 2 hours (shorter sessions, visual methods, Easy Read materials)
- Facilitated by experienced LD advocacy workers
- All participants paid NIHR INVOLVE rates (£25/hour + expenses)

**Workshop Topics:**
1. "What AI Have You Used?" – Mapping LD AI experiences
2. "What Goes Wrong?" – Identifying harm patterns
3. "What Would 'Safe' Look Like?" – Defining safety requirements
4. "Can You Understand This?" – Testing AI output accessibility
5. "Who Should Decide?" – Governance and consent
6. "How Would We Check?" – Developing validation methods

**Outputs:**
- LD-defined safety requirements
- Accessibility criteria from lived experience
- Harm typology (what needs detection)

**5.1.2 Clinical and Technical Input (Months 4-10)**

Parallel consultation with:
- LD nurses (n=10) – Clinical safety perspectives
- Informaticists (n=5) – Technical feasibility
- Procurement leads (n=5) – Implementation requirements

**Method:** Semi-structured interviews (45 mins each)

**Output:** Draft CJ-ASF specification integrating LD, clinical, and technical perspectives

**5.1.3 Framework Specification (Months 10-12)**

Synthesize Phase 1 findings into:
- CJ-ASF Domain Structure (what to evaluate)
- Safety Requirements Catalog (what constitutes pass/fail)
- Accessibility Standards (measurable criteria)
- Bias Detection Methods (what to test for)

---

### Phase 2: Technical Build (Year 2)

**Objective:** Implement CJ-ASF as working software extending existing Open Nursing Core infrastructure.

**5.2.1 Technical Architecture (Months 1-3)**

Extend existing infrastructure:

| Component | Existing | CJ-ASF Extension |
|-----------|----------|------------------|
| FHIR IG (ONC) | Nursing profiles | LD accessibility profiles |
| Validator API | Clinical safety checks | Accessibility validation |
| LLM (nursing-llama) | Person-centred documentation | Bias detection prompts |

**New Components to Build:**
- **Accessibility Validator:** Tests AI outputs against LD readability criteria
- **Bias Detection Module:** Prompts AI with LD scenarios, flags overshadowing patterns
- **Governance Checklist API:** Automated compliance scoring

**5.2.2 Development Sprints (Months 4-10)**

Agile development with monthly sprints:
- Sprint reviews with LD co-researcher advisory group
- Iterative refinement based on feedback
- Open-source development (GitHub)

**5.2.3 Alpha Testing (Months 10-12)**

Internal testing with:
- 5 sample AI technologies (symptom checkers, chatbots, documentation tools)
- LD co-researchers as primary testers
- Identify bugs, usability issues, false positives/negatives

**Output:** Working CJ-ASF toolkit (beta version)

---

### Phase 3: Validation (Year 3)

**Objective:** Validate CJ-ASF through multi-site testing with real NHS AI systems.

**5.3.1 NHS Site Recruitment (Months 1-3)**

Partner with 3 NHS organizations deploying AI:
- Selection criteria: Currently using or procuring AI technologies
- Diverse settings: Acute, community, mental health
- Ethics and governance approvals obtained

**5.3.2 CJ-ASF Application (Months 4-8)**

At each site:
1. **Identify AI technologies** in use or under procurement
2. **Apply CJ-ASF toolkit** to evaluate each technology
3. **Document findings** (accessibility failures, bias detected, safety concerns)
4. **Compare to existing evaluation** (what did CJ-ASF find that current methods missed?)

**5.3.3 Mixed-Methods Evaluation (Months 4-10)**

**Quantitative Metrics:**
- Detection rate: What proportion of known LD-relevant issues does CJ-ASF identify?
- False positive rate: What proportion of flagged issues are genuine concerns?
- Coverage: What proportion of CJ-ASF domains are assessable with available information?

**Qualitative Evaluation:**
- Interviews with procurement teams (n=10): Was CJ-ASF usable? Did it change decisions?
- Interviews with LD co-researchers (n=10): Did CJ-ASF capture what matters?
- Focus groups with clinical teams (n=2): Is CJ-ASF clinically relevant?

**5.3.4 Framework Refinement (Months 10-12)**

Integrate validation findings:
- Update domains/criteria based on testing
- Refine toolkit based on usability feedback
- Develop implementation guidance based on site experiences

**Final Outputs:**
- Validated CJ-ASF Framework
- Open-source CJ-ASF Toolkit
- Implementation Guidance for NHS
- Academic publications

---

## 6. Patient and Public Involvement

### Core Principle: "Nothing About Us Without Us"

People with Learning Disabilities are **co-researchers**, not participants:

| Role | Number | Involvement |
|------|--------|-------------|
| Co-Research Group | 15-20 | All 3 phases, monthly contact |
| Advisory Board | 3 | Strategic decisions, quarterly |
| Testers | 10+ | Phase 2-3 toolkit testing |

**Support Structures:**
- Payment: NIHR rates (£25/hour + expenses)
- Accessible materials: Easy Read, visual, audio
- Flexible formats: Shorter sessions, breaks, advocacy support
- Training: Research skills development for interested co-researchers

---

## 7. Ethics and Governance

- University ethics approval (Phase 1-3)
- NHS HRA approval for NHS site work (Phase 3)
- All AI testing uses non-patient-facing scenarios
- LD co-researcher consent through accessible processes
- Data protection: No real patient data used

---

## 8. Dissemination and Impact

**Immediate Outputs:**
1. **CJ-ASF Framework:** Validated evaluation domains and criteria
2. **CJ-ASF Toolkit:** Open-source software for AI assessment
3. **Implementation Guidance:** Practical protocols for NHS use
4. **Easy Read Summary:** Accessible findings for LD community

**Target Audiences:**
- NHS Procurement: How to evaluate AI before buying
- AI Developers: How to build LD-inclusive systems
- Clinical Governance: How to monitor deployed AI
- LD Advocacy: How to challenge exclusionary AI

**Policy Impact:**
- NHS AI Lab engagement
- NICE Evidence Standards input
- CQC inspection framework recommendations

---

## 9. Timeline

| Year | Phase | Key Activities | Outputs |
|------|-------|----------------|---------|
| 1 | Co-Design | Participatory workshops, interviews, specification | Draft CJ-ASF spec |
| 2 | Build | Technical development, alpha testing | Working toolkit (beta) |
| 3 | Validate | Multi-site NHS testing, evaluation | Validated framework + toolkit |

---

## 10. Why This Is Different

| Feature | This Proposal | Typical Framework Research |
|---------|---------------|---------------------------|
| Methodology | Design Science (build + validate) | Literature review/synthesis |
| Output | Working software + governance | Policy documents/checklists |
| LD Role | Co-researchers (all phases) | Consulted (late stage) |
| Validation | Multi-site NHS testing | Expert consensus |
| Foundation | Existing technical infrastructure | Starts from scratch |

**This produces practical tools tested in real NHS contexts—not another set of aspirational guidelines.**

---

## 11. References

### Learning Disability Health Inequalities

1. Heslop P, Blair PS, Fleming P, Hoghton M, Marriott A, Russ L. The Confidential Inquiry into premature deaths of people with intellectual disabilities in the UK: a population-based study. *The Lancet*. 2014;383(9920):889-895.

2. NHS England. Learning Disabilities Mortality Review (LeDeR) Programme: Annual Report 2023. London: NHS England; 2024.

3. Mencap. Death by Indifference: 74 Deaths and Counting. London: Mencap; 2012.

4. Emerson E, Baines S, Allerton L, Welch V. Health Inequalities and People with Learning Disabilities in the UK. *Improving Health and Lives: Learning Disabilities Observatory*. 2012.

5. Glover G, Williams R, Heslop P, Oyinlola J, Grey J. Mortality in people with intellectual disabilities in England. *Journal of Intellectual Disability Research*. 2017;61(1):62-74.

### Diagnostic Overshadowing

6. Mason J, Scior K. 'Diagnostic overshadowing' amongst clinicians working with people with intellectual disabilities in the UK. *Journal of Applied Research in Intellectual Disabilities*. 2004;17(2):85-90.

7. Javaid A, Nakata V, Michael D. Diagnostic overshadowing in learning disability: think beyond the disability. *Progress in Neurology and Psychiatry*. 2019;23(2):8-10.

8. Shefer G, Henderson C, Howard LM, Murray J, Thornicroft G. Diagnostic overshadowing and other challenges involved in the diagnostic process of patients with mental illness who present in emergency departments with physical symptoms—a qualitative study. *PLoS ONE*. 2014;9(11):e111682.

### AI Bias and Disability

9. Morris MR, Zolyomi A, Yao C, Bahram S, Bigham JP, Kane SK. With most of it being pictures: an analysis of responses to emergency alerts by deaf people. *Proceedings of CHI 2016*. 2016:5215-5227.

10. Whittaker M, Alper M, Bennett CL, et al. Disability, Bias, and AI. AI Now Institute Report. New York: AI Now Institute; 2019.

11. Trewin S, Basson S, Muller M, et al. Considerations for AI fairness for people with disabilities. *AI Matters*. 2019;5(3):40-63.

12. Guo A, Kamar E, Vaughan JW, Wallach H, Morris MR. Toward fairness in AI for people with disabilities: a research roadmap. *ACM SIGACCESS Accessibility and Computing*. 2020;(125):1-1.

13. Gadiraju U, Yang J, Demartini G. Crowd accessibility: challenges and opportunities for crowd workers with disabilities. *Proceedings of HCOMP 2020*. 2020:80-89.

14. Hutchinson B, Prabhakaran V, Denton E, et al. Social biases in NLP models as barriers for persons with disabilities. *Proceedings of ACL 2020*. 2020:5491-5501.

15. Venkit PN, Srinath M, Wilson S. A study of implicit bias in pretrained language models against people with disabilities. *Proceedings of COLING 2022*. 2022:1324-1332.

### Design Science Research Methodology

16. Hevner AR, March ST, Park J, Ram S. Design science in information systems research. *MIS Quarterly*. 2004;28(1):75-105.

17. Peffers K, Tuunanen T, Rothenberger MA, Chatterjee S. A design science research methodology for information systems research. *Journal of Management Information Systems*. 2007;24(3):45-77.

18. Wieringa RJ. Design Science Methodology for Information Systems and Software Engineering. Berlin: Springer; 2014.

19. Gregor S, Hevner AR. Positioning and presenting design science research for maximum impact. *MIS Quarterly*. 2013;37(2):337-355.

### Participatory Research with People with Learning Disabilities

20. Walmsley J, Johnson K. Inclusive Research with People with Learning Disabilities: Past, Present and Futures. London: Jessica Kingsley Publishers; 2003.

21. Nind M. Conducting Qualitative Research with People with Learning, Communication and Other Disabilities: Methodological Challenges. NCRM Methods Review Papers, NCRM/012. Southampton: ESRC National Centre for Research Methods; 2008.

22. Bigby C, Frawley P, Ramcharan P. Conceptualizing inclusive research with people with intellectual disability. *Journal of Applied Research in Intellectual Disabilities*. 2014;27(1):3-12.

23. NIHR. Guidance on co-producing a research project. Southampton: NIHR INVOLVE; 2021.

### Social Justice and Intersectionality

24. Moorley C, Cahill S, Corcoran N. Life after Stroke: Coping Mechanisms among African Caribbean Women. *Health & Social Care in the Community*. 2016;24(6):e85-e94.

25. Moorley C, Ferrante J, Amod H, Burrowes S. Experiences of racism and the impact on the wellbeing of nurses and midwives: A systematic review. *Journal of Clinical Nursing*. 2022;32(17-18):5641-5667.

26. Crenshaw K. Mapping the margins: Intersectionality, identity politics, and violence against women of color. *Stanford Law Review*. 1991;43(6):1241-1299.

27. Collins PH, Bilge S. Intersectionality. 2nd ed. Cambridge: Polity Press; 2020.

### Health Equity and Long-Term Conditions

28. Habte-Asres HH, De Souza RM, Sherr L. Glycaemic variability and progression of chronic kidney disease in people with diabetes and comorbid kidney disease: systematic review. *Diabetic Medicine*. 2024;41(5):e15295.

29. Marmot M, Allen J, Boyce T, Goldblatt P, Morrison J. Health Equity in England: The Marmot Review 10 Years On. London: Institute of Health Equity; 2020.

30. Marmot M. Fair Society, Healthy Lives: The Marmot Review. London: Institute of Health Equity; 2010.

### NHS Digital and AI Policy

31. NHS England. NHS Long Term Plan. London: NHS England; 2019.

32. Health Education England. NHS AI and Digital Healthcare Technologies Capability Framework. London: NHS HEE; 2023.

33. NICE. Evidence Standards Framework for Digital Health Technologies. London: NICE; 2024.

34. Health Innovation Network. NHS TEST (Technology Evaluation Safety Test) Framework. London: Health Innovation Network; 2023.

35. NHS AI Lab. Lessons from the AI in Health and Care Award Programme. London: NHSX; 2024.

### Disability Rights and Digital Inclusion

36. Shakespeare T. Disability Rights and Wrongs Revisited. 2nd ed. London: Routledge; 2014.

37. Oliver M. The Politics of Disablement. Basingstoke: Macmillan; 1990.

38. Fricker M. Epistemic Injustice: Power and the Ethics of Knowing. Oxford: Oxford University Press; 2007.

39. NHS England. A Framework for NHS Action on Digital Inclusion. London: NHS England; 2024.

40. Good Things Foundation. Digital Exclusion and Health Inequalities. Sheffield: Good Things Foundation; 2022.
