# PhD Research Proposal

**Project Title:** Bridging the Reasonable Adjustments Gap: AI-Enabled Accessible Diabetes Self-Management for People with Learning Disabilities

**Applicant:** Lincoln Gombedza, RN (Learning Disability)

**Proposed Supervisors:** 
- Prof. Calvin Moorley (Lead Supervisor, LSBU) - Social justice, intersectionality, health equity
- Dr. Helena Hailu Habte-Asres (Co-Supervisor, KCL) - Diabetes care, long-term conditions

**Mode of Study:** Full-time (3 years) or Part-time (4 years)

**Proposed Start Date:** TBC

---

## Abstract

**Background:**

People with Learning Disabilities (LD) experience profound health inequalities, dying on average 15-20 years earlier than the general population from preventable causes (Heslop et al., 2014; Diabetes UK, 2023). Diabetes prevalence is 2-3 times higher in LD populations (Emerson et al., 2012), yet outcomes are significantly worse: faster disease progression requiring earlier insulin initiation, and doubled all-cause mortality despite similar glycemic control (Florio & Trollor, 2015; Hosking et al., 2016). Key contributors include communication barriers that prevent effective self-management, inaccessible care plans that assume literacy and numeracy skills, and a persistent "reasonable adjustments gap" where standard NHS diabetes services fail to adapt for cognitive diversity (NHS England LeDeR, 2024; NHS RightCare, 2023). The LeDeR programme consistently identifies failures in accessible health communication as contributors to preventable deaths (NHS England LeDeR, 2024).

Emerging Large Language Models (LLMs) and AI documentation tools could address these structural inequities by translating complex clinical protocols into accessible formats. However, current AI systems are trained on neurotypical communication standards, risking further marginalization of LD communities if deployed without adaptation (Whittaker et al., 2019; Trewin et al., 2019).

**Aim:**

To develop and evaluate an AI framework that translates diabetes care documentation into accessible formats for people with Learning Disabilities, closing the reasonable adjustments gap through automated Easy Read generation and accessible self-management support.

**Methods:**

This study employs Design Science Research methodology across three phases. Phase 1 (Year 1): Co-design accessibility requirements with people with LD through participatory workshops, and fine-tune a Large Language Model on Easy Read diabetes resources and LD-friendly health materials. Phase 2 (Year 2): Comparative evaluation where 30-40 diabetes scenarios are processed through both the LD-specific AI model and a generic baseline, with outputs scored by LD nurses and people with LD for accessibility, comprehension, and clinical safety. Phase 3 (Year 3): Implementation research exploring barriers and enablers through interviews with LD nurses and diabetes teams, analyzed using Normalisation Process Theory.

**Impact:**

This research will produce the first validated AI tool specifically designed to close the reasonable adjustments gap in diabetes care for people with Learning Disabilities. Outputs include: (1) an accessible diabetes documentation assistant; (2) FHIR profiles for LD-inclusive health records; (3) evidence-based guidance for deploying equity-focused AI in LD services. The ultimate goal is improving diabetes self-management and reducing preventable complications in LD populations.

---

## 1. Background and Rationale

### 1.1 Health Inequalities in Learning Disabilities

People with Learning Disabilities face stark health inequalities. The Confidential Inquiry into premature deaths of people with learning disabilities (CIPOLD) found that people with LD die on average 16 years younger (men) and 20 years younger (women) than the general population (Heslop et al., 2014). The LeDeR programme continues to identify preventable factors in 40-50% of deaths (NHS England LeDeR, 2024).

**Key Contributors to Health Inequalities:**
- **Communication Barriers:** Health professionals struggle to elicit symptoms; people with LD unable to articulate concerns (NHS RightCare, 2023; Cardol et al., 2012)
- **Inaccessible Healthcare:** Standard health information assumes literacy, numerical skills, and abstract reasoning (Mencap, 2012)
- **Reasonable Adjustments Gap:** Despite legal requirements under the Equality Act 2010, services frequently fail to adapt (NHS England LeDeR, 2024; NHS RightCare, 2023)
- **Late Diagnosis:** Delayed recognition of conditions due to atypical presentations and access barriers (Emerson et al., 2012)
- **Underscreening:** Lower rates of health screening uptake, including retinal and foot examinations (NHS RightCare, 2023; Florio & Trollor, 2015)

### 1.2 Diabetes as a Critical Health Inequality

Diabetes prevalence is 2-3 times higher in LD populations compared to the general population (Emerson et al., 2012; Diabetes UK, 2023), yet outcomes are dramatically worse:

**Evidence from Recent Research:**
- **Faster Disease Progression:** People with LD require insulin initiation earlier despite better initial glycemic control (Florio & Trollor, 2015; Hosking et al., 2016)
- **Doubled Mortality Risk:** 2x higher all-cause and diabetes-related mortality, even with similar HbA1c levels (Florio & Trollor, 2015; Hosking et al., 2016)
- **Lower Rates of Care Processes:** Less likely to receive all key diabetes checks (eye exams, foot checks) (NHS RightCare, 2023; Guo et al., 2020)
- **Higher Obesity Rates:** Around 40% of adults with LD are obese, increasing diabetes risk (Diabetes UK, 2023)

Dr. Helena Hailu Habte-Asres's research on glycemic variability and CKD progression (Habte-Asres, De Souza & Sherr, 2024) demonstrates the critical importance of consistent diabetes management. For people with LD, this consistency is undermined by:

1. **Inaccessible care plans:** Standard NHS diabetes care plans use medical terminology, numerical targets (e.g., "aim for HbA1c <58 mmol/mol"), and abstract dietary advice
2. **Assumption of self-management:** Monitoring blood glucose, counting carbohydrates, and administering insulin all assume cognitive skills that may not be present
3. **Communication failures:** Unable to report symptoms of hypo/hyperglycemia effectively

### 1.3 The "Reasonable Adjustments" Gap

The Equality Act 2010 mandates "reasonable adjustments" for disabled people accessing services. In diabetes care, this should include:

- **Easy Read** health information and care plans
- **Pictorial guides** for medication and diet
- **Communication Passports** documenting individual needs
- **Longer consultation times** with adapted communication
- **Carer involvement** where appropriate

Yet LeDeR reviews and NHS audit data consistently find these adjustments are not made (NHS England LeDeR, 2024; NHS RightCare, 2023). Key barriers include:

- **Time:** Translating a standard diabetes care plan into Easy Read format manually requires 2-3 hours specialist input
- **Skills:** Most healthcare staff lack training in accessible communication
- **Resources:** Easy Read production is expensive and rarely prioritized
- **Systems:** Electronic health records don't capture communication preferences

### 1.4 The AI Opportunity

Large Language Models (LLMs) can perform "translation" tasks: converting complex text into simplified formats. This presents an opportunity for **scalable reasonable adjustments**—AI could generate Easy Read diabetes care plans in seconds rather than hours.

However, current LLMs present significant risks if deployed uncritically:

- **Trained on neurotypical norms:** ChatGPT/GPT-4 optimize for linguistic complexity (Whittaker et al., 2019)
- **No LD-specific grounding:** Models have no exposure to Easy Read standards, Makaton, or LD communication practices
- **Potential for harm:** "Simplified" text may still be cognitively inaccessible (Trewin et al., 2019)

**This research develops AI specifically designed to close the reasonable adjustments gap, grounded in LD communication expertise and co-produced with people with Learning Disabilities.**

### 1.5 Theoretical Framework

This study integrates two theoretical perspectives:

**Social Model of Disability:**
Prof. Calvin Moorley's work on intersectionality and health equity (Moorley et al., 2022; Moorley, Cahill & Corcoran, 2016) positions this research within disability rights: the "problem" is not the person with LD, but the inaccessible system (Shakespeare, 2014; Oliver, 1990). AI is positioned as a tool for system change, removing barriers rather than "fixing" individuals.

**Health Equity Framework (Marmot):**
The research targets structural causes of health inequality (Marmot, 2010; Marmot et al., 2020), addressing determinants of poor diabetes outcomes in LD populations through improved access to understandable health information.

---

## 2. Aim and Research Questions

### 2.1 Aim

To develop and rigorously evaluate an AI framework that closes the reasonable adjustments gap in diabetes care for people with Learning Disabilities by translating clinical documentation into genuinely accessible formats.

### 2.2 Primary Research Question

Does an LD-Accessible AI documentation framework produce significantly more understandable and usable diabetes care plans for people with LD compared to generic AI or standard care plan formats?

### 2.3 Secondary Research Questions

**Framework Development (Phase 1):**
- RQ1a: What communication features define "accessibility" in diabetes documentation for people with LD?
- RQ1b: What consensus exists among people with LD, specialist nurses, and diabetes educators on priorities for accessible care plans?

**Comparative Evaluation (Phase 2):**
- RQ2a: How do LD-Accessible AI and generic AI care plans compare on comprehension, usability, and clinical accuracy?
- RQ2b: Do people with LD rate LD-Accessible AI outputs as more understandable?
- RQ2c: Do clinicians identify equivalent clinical safety in LD-Accessible AI outputs?

**Implementation (Phase 3):**
- RQ3a: What contextual factors enable or constrain deployment of accessible AI in LD health services?
- RQ3b: How do LD nurses perceive AI's impact on their communication role?
- RQ3c: What training and governance structures are needed for safe, equity-focused AI?

---

## 3. Research Plan and Methodology

**Study Design:** Design Science Research (3 years full-time)

### Phase 1: Co-Design and Development (Year 1)

**Step 1.1: Accessibility Standards Review (Months 1-3)**

Review of accessibility frameworks and evidence:
- NHS England Easy Read standards
- Mencap accessible information guidelines
- CHANGE accessible communication resources
- Diabetes UK resources for LD
- LeDeR thematic reviews

**Output:** Evidence-based accessibility criteria for diabetes documentation.

**Step 1.2: Participatory Co-Design with People with LD (Months 3-8)**

Co-design workshops (n=4 workshops, 8-10 participants each) with people with LD who have diabetes:
- Review existing diabetes care plans: what is confusing?
- Co-create "ideal" accessible care plan examples
- Test prototype AI outputs for comprehension
- Iterate based on feedback

**Compensation:** NIHR INVOLVE rates (£25/hour + expenses)
**Support:** Facilitation by experienced LD advocacy workers, Easy Read materials throughout

**Output:** Co-produced accessibility framework and exemplar care plans.

**Step 1.3: Expert Consultation (Months 6-10)**

Expert panel (n=20-25):
- LD nurses with diabetes expertise (n=10)
- Diabetes specialist nurses (n=5)
- Easy Read specialists (n=3)
- People with LD (n=5)

**Method:** Modified Delphi to achieve consensus (≥70% agreement) on:
- Indicators of accessible AND clinically safe diabetes documentation
- Minimum standards for AI-generated care plans

**Output:** LD-Accessible Diabetes Documentation Framework (LD-ADDF)

**Step 1.4: AI Model Development (Months 8-12)**

Building on existing Open Nursing Core infrastructure:

**Training Corpus:**
- Easy Read diabetes resources (NHS, Diabetes UK)
- Accessible communication exemplars
- LD nursing documentation standards
- Co-produced materials from Step 1.2

**Technical Approach:**
- Fine-tune Llama-3 (8B) using LoRA
- Prompt engineering for Easy Read generation
- Validation against LD-ADDF criteria

**Output:** `LD-Diabetes-AI` model

---

### Phase 2: Comparative Evaluation (Year 2)

**Step 2.1: Scenario Development (Months 1-3)**

30-40 diabetes scenarios co-designed with clinical educators and people with LD:

| Variable | Range |
|----------|-------|
| Diabetes type | Type 1, Type 2 |
| Communication level | Verbal, limited verbal, AAC user |
| Complexity | Simple (stable), moderate, complex |
| Setting | Community, inpatient, residential |

**Step 2.2: Comparative Experiment (Months 4-10)**

Each scenario processed through:
1. **Standard format:** Typical NHS diabetes care plan
2. **Generic AI:** Standard LLM with "simplify" prompt
3. **LD-Diabetes-AI:** Fine-tuned model with accessibility prompting

**Blinded Scoring by:**
- Two LD nurses using LD-ADDF criteria
- People with LD rating comprehension (1-5 scale + qualitative feedback)

**Primary Outcome:** Comprehension score from people with LD
**Secondary Outcomes:** 
- LD-ADDF total score
- Clinical accuracy (errors/omissions)
- Time to understand (observational)

**Sample Size:** n=40 scenarios (power=0.80, α=0.05)

**Analysis:** Repeated measures ANOVA, thematic analysis of qualitative feedback

---

### Phase 3: Implementation Research (Year 3)

**Step 3.1: Qualitative Interviews (Months 1-6)**

n=20-25 participants:
- LD nurses (n=12)
- Diabetes specialist nurses (n=5)
- Digital health leads (n=3)
- People with LD (n=5)

**Topic Guide** (NPT-informed):
- Current diabetes communication challenges
- Responses to AI outputs (from Phase 2)
- Perceived barriers and enablers to implementation
- Governance and safety concerns
- Training needs

**Step 3.2: Analysis (Months 6-11)**

- Reflexive Thematic Analysis (Braun & Clarke)
- NPT framework mapping
- Integration with quantitative findings (joint display)

**Output:** Implementation guidance and recommendations

---

## 4. Patient and Public Involvement (PPIE)

**Core Principle: "Nothing About Us Without Us"**

People with Learning Disabilities are co-researchers throughout:

| Role | Number | Involvement |
|------|--------|-------------|
| Co-Design Group | 8-10 | Phase 1 workshops, ongoing advisory |
| Evaluators | 10-15 | Phase 2 comprehension testing |
| Interviewees | 5 | Phase 3 lived experience |

**Support Structures:**
- Payment: NIHR rates (£25/hour + expenses)
- Accessible materials: Easy Read throughout
- Flexible formats: Shorter sessions, visual methods
- Advocacy support: Facilitation by LD advocacy workers

---

## 5. Equality, Diversity and Inclusion

This research explicitly centers disability equity:

- **Co-production:** People with LD shape the research, not just participate
- **Intersectionality:** Sampling reflects diversity in ethnicity, gender, LD severity, communication methods [24, 25, 26]
- **Non-extractive:** Outputs designed for direct community benefit (accessible AI tool)

---

## 6. Impact and Dissemination

**Immediate Outputs:**
1. **LD-Diabetes-AI Tool:** Open-source accessible diabetes documentation assistant
2. **LD-ADDF:** Validated framework for assessing accessible documentation
3. **FHIR Profiles:** Extensions to Open Nursing Core IG for LD reasonable adjustments

**Dissemination:**
- LD nursing conferences
- Diabetes UK professional meetings
- LeDeR programme (informing quality improvement)
- Easy Read research summary for people with LD

**Policy Impact:**
- NHS RightCare Pathway for Diabetes integration
- NICE guidance on reasonable adjustments
- NHS England digital inclusion framework

---

## 7. References

### Learning Disability Health Inequalities

1. Heslop P, Blair PS, Fleming P, Hoghton M, Marriott A, Russ L. The Confidential Inquiry into premature deaths of people with intellectual disabilities in the UK: a population-based study. *The Lancet*. 2014;383(9920):889-895.

2. NHS England. Learning Disabilities Mortality Review (LeDeR) Programme: Annual Report 2023. London: NHS England; 2024.

3. Mencap. Death by Indifference: 74 Deaths and Counting. London: Mencap; 2012.

4. Emerson E, Baines S, Allerton L, Welch V. Health Inequalities and People with Learning Disabilities in the UK. *Improving Health and Lives: Learning Disabilities Observatory*. 2012.

5. Diabetes UK. Diabetes and Learning Disabilities. London: Diabetes UK; 2023.

6. NHS England. NHS RightCare Pathway: Diabetes. London: NHS England; 2023.

### Diabetes and Learning Disabilities

7. Cardol M, Rijken M, van Schrojenstein Lantman-de Valk H. People with mild to moderate intellectual disability talking about their diabetes and how they manage. *Journal of Intellectual Disability Research*. 2012;56(4):351-360.

8. Florio T, Trollor J. Mortality among a cohort of persons with an intellectual disability in New South Wales, Australia. *Journal of Applied Research in Intellectual Disabilities*. 2015;28(5):383-393.

9. Hosking FJ, Carey IM, Shah SM, et al. Mortality among adults with intellectual disability in England: comparisons with the general population. *American Journal of Public Health*. 2016;106(8):1483-1490.

### AI and Disability

10. Whittaker M, Alper M, Bennett CL, et al. Disability, Bias, and AI. AI Now Institute Report. New York: AI Now Institute; 2019.

11. Trewin S, Basson S, Muller M, et al. Considerations for AI fairness for people with disabilities. *AI Matters*. 2019;5(3):40-63.

12. Guo A, Kamar E, Vaughan JW, Wallach H, Morris MR. Toward fairness in AI for people with disabilities: a research roadmap. *ACM SIGACCESS Accessibility and Computing*. 2020;(125):1-1.

### Methodology

13. Hevner AR, March ST, Park J, Ram S. Design science in information systems research. *MIS Quarterly*. 2004;28(1):75-105.

14. Walmsley J, Johnson K. Inclusive Research with People with Learning Disabilities: Past, Present and Futures. London: Jessica Kingsley Publishers; 2003.

15. Bigby C, Frawley P, Ramcharan P. Conceptualizing inclusive research with people with intellectual disability. *Journal of Applied Research in Intellectual Disabilities*. 2014;27(1):3-12.

### Social Justice and Health Equity

24. Moorley C, Ferrante J, Amod H, Burrowes S. Experiences of racism and the impact on the wellbeing of nurses and midwives: A systematic review. *Journal of Clinical Nursing*. 2022;32(17-18):5641-5667.

25. Moorley C, Cahill S, Corcoran N. Life after Stroke: Coping Mechanisms among African Caribbean Women. *Health & Social Care in the Community*. 2016;24(6):e85-e94.

26. Crenshaw K. Mapping the margins: Intersectionality, identity politics, and violence against women of color. *Stanford Law Review*. 1991;43(6):1241-1299.

28. Habte-Asres HH, De Souza RM, Sherr L. Glycaemic variability and progression of chronic kidney disease in people with diabetes and comorbid kidney disease: systematic review. *Diabetic Medicine*. 2024;41(5):e15295.

29. Marmot M. Fair Society, Healthy Lives: The Marmot Review. London: Institute of Health Equity; 2010.

30. Marmot M, Allen J, Boyce T, Goldblatt P, Morrison J. Health Equity in England: The Marmot Review 10 Years On. London: Institute of Health Equity; 2020.

### Disability Rights

36. Shakespeare T. Disability Rights and Wrongs Revisited. 2nd ed. London: Routledge; 2014.

37. Oliver M. The Politics of Disablement. Basingstoke: Macmillan; 1990.
