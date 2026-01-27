# PhD Research Proposal

**Project Title:** Making the Invisible Visible: Evaluating a Person-Centred Nursing-Informed AI Approach for Documenting Relational Care

**Applicant:** Lincoln Gombedza

**Proposed Supervisors:** TBC

**Mode of Study:** Full-time (3 years) or Part-time (4 years)

**Proposed Start Date:** TBC

---

## Abstract

**Background:**

Clinical documentation is a critical component of nursing practice but is frequently cited as a significant administrative burden that detracts from direct patient care. International evidence suggests nurses spend up to 35% of their shift on documentation tasks (Baumann et al., 2018), with growing concerns that this administrative load contributes to burnout and attrition from the profession (Ball et al., 2017). Emerging 'ambient clinical intelligence' (ACI) technologies offer a potential solution by automating clinical notes via speech recognition. However, existing ACI systems are predominantly trained on biomedical datasets and doctor-patient interactions. Consequently, they risk failing to capture the unique, relational dimensions of nursing—the 'invisible work' of emotional support, advocacy, and holistic assessment—thereby reinforcing a task-oriented reductionism in health records.

**Aim:**

To develop, validate, and evaluate a Person-Centred Nursing-Informed (PCN-I) AI documentation approach, comparing its efficacy in capturing relational care against a generic biomedical ACI model.

**Methods:**

This study employs a sequential mixed-methods design across three phases. Phase 1 involves the co-production of a Relational Care Documentation Framework (RCDF) through a scoping review and a modified Delphi study with nurses and patient/carer partners. Phase 2 utilises a comparative experimental design using 30-40 simulated nursing scenarios to evaluate two documentation pipelines: (1) a generic voice-to-text model, and (2) the novel PCN-I model. The primary outcome is the capture of relational content as measured by the RCDF. Phase 3 explores implementation feasibility, professional identity, and safety through semi-structured interviews and focus groups with nurses, mapped to the NASSS framework.

**Impact:**

This research will produce the first validated framework for measuring relational content in AI-generated nursing notes and provide evidence-based guidelines for the ethical deployment of ambient AI in nursing. The ultimate goal is to reduce documentation burden while ensuring the complexity of nursing care is accurately visible in the digital health record.

---

## 1. Background and Rationale

### 1.1 The Clinical Challenge: Burden vs. Visibility

Nursing documentation is essential for patient safety, continuity of care, and professional accountability (Nursing and Midwifery Council [NMC], 2018). The NMC Code explicitly requires nurses to "keep clear and accurate records relevant to your practice" (Standard 10), recognising documentation as both a professional and legal requirement. However, documentation imposes a substantial time burden, often competing with direct clinical care (de Groot et al., 2022).

Evidence from multiple international contexts demonstrates the scale of this challenge. In the United Kingdom, the Royal College of Nursing (2019) reported that nurses spend an average of 17.5 hours per week on administrative tasks, with documentation comprising the largest proportion. Similar patterns emerge globally: Canadian studies suggest documentation accounts for approximately 35% of nursing time (Baumann et al., 2018), whilst Australian research identifies documentation burden as a key driver of professional dissatisfaction (Duffield et al., 2021).

The consequences of this burden extend beyond time allocation. Research consistently links excessive documentation requirements to:
- **Burnout and moral distress**: When nurses perceive documentation as detracting from patient care (Ball et al., 2017; Aiken et al., 2023)
- **Incomplete or retrospective documentation**: Leading to accuracy concerns when nurses document at shift end rather than in real-time (Blair & Smith, 2012)
- **Professional identity tensions**: As nurses experience conflict between their caring role and administrative obligations (Heartfield, 1996)

While digital transformation aims to alleviate this burden, standard electronic health records (EHRs) often constrain nurses to drop-down menus and task lists, failing to capture the nuances of person-centred practice. Allen (2015) describes this as the 'invisible work' of nursing—the organising, mediating, and relational labour that holds healthcare trajectories together but rarely appears in formal metrics. This invisible work includes:
- Coordinating care across multidisciplinary teams
- Mediating between patients, families, and healthcare systems
- Providing emotional support and therapeutic presence
- Advocating for patient preferences and values
- Facilitating shared decision-making

When documentation systems fail to capture this relational labour, nursing's contribution to healthcare outcomes remains invisible to managers, policymakers, and researchers (Allen, 2014). This invisibility has profound implications for resource allocation, skill-mix decisions, and professional recognition.

### 1.2 The Technological Gap

Ambient Clinical Intelligence (ACI), or ambient voice technology, is rapidly emerging as a solution to documentation burnout. These systems utilise automatic speech recognition (ASR) combined with natural language processing (NLP) to convert clinical conversations into structured documentation automatically. Recent studies, such as Wendt et al. (2025), demonstrate that ACI can significantly reduce documentation time in medical consultations—in some cases by up to 70%.

Commercial solutions such as Nuance DAX (Dragon Ambient eXperience), Abridge, and Amazon AWS HealthScribe are gaining traction in healthcare settings, particularly within primary care and outpatient medicine. The NHS Long Term Plan (2019) explicitly supports digital transformation including voice-enabled documentation, creating pressure for rapid adoption across healthcare settings.

However, these tools are largely optimised for the 'medical model'—focusing on symptoms, diagnoses, and treatment plans derived from physician-patient consultations. A critical examination of current ACI training data reveals:

- **Biomedical bias**: Training corpora predominantly derive from physician dictation, medical transcription services, and structured diagnostic language (Finley et al., 2018)
- **Consultation structure assumptions**: Systems optimised for discrete consultation episodes rather than continuous nursing presence across shifts
- **Outcome orientation**: Emphasis on capturing treatment decisions rather than process-oriented relational care

If applied uncritically to nursing, generic ACI tools risk generating notes that are clinically 'complete' in a biomedical sense but 'relationally thin'. They may systematically omit:
- The patient's narrative and lived experience of illness
- Emotional state and psychosocial context
- The nurse's therapeutic use of self
- Family involvement and dynamics
- Cultural considerations and preferences
- Evidence of compassionate presence

This effectively erases the core tenets of nursing from the official record. There is currently a paucity of evidence regarding the efficacy of AI in capturing these non-biomedical dimensions of care. A preliminary literature search identified no published studies specifically examining how ACI captures relational nursing care, representing a significant gap this research addresses.

### 1.3 Why This Research Is Needed Now

Several converging factors create urgency for this research:

**Rapid Technology Adoption**: The COVID-19 pandemic accelerated healthcare digitalisation, with voice technology adoption increasing substantially across clinical settings. Once generic ACI becomes embedded in clinical workflows, retrofitting person-centred considerations becomes exponentially harder (Greenhalgh et al., 2017). There is a narrow window to influence how these technologies develop for nursing.

**NHS Digital Transformation Agenda**: The NHS Long Term Plan (2019), What Good Looks Like framework (NHS England, 2021), and Integrated Care System strategies all prioritise digital transformation. Without nursing-specific evidence, procurement decisions risk defaulting to generic physician-oriented solutions.

**Professional Identity at a Crossroads**: The nursing profession is simultaneously grappling with workforce crises, scope of practice debates, and questions about what distinguishes nursing from medicine (Dewing et al., 2021). AI documentation that reduces nursing to task completion threatens to exacerbate professional identity erosion.

**Regulatory Interest**: The Care Quality Commission's (2023) focus on 'person-centred' care as an inspection domain, combined with emerging NHS AI governance frameworks, creates opportunities for research to inform standards and procurement criteria.

**Patient Safety Implications**: If AI-generated notes omit relational content, downstream clinicians may lack crucial information about patient preferences, emotional state, or family dynamics—potentially compromising handover quality and care continuity (Staggers & Blaz, 2013).

### 1.4 Theoretical Framework

This study is grounded in three complementary theoretical perspectives that together provide a comprehensive lens for understanding how AI intersects with nursing documentation:

**Primary Framework: Person-Centred Practice Framework (McCormack & McCance, 2017)**

The Person-Centred Practice Framework posits that high-quality care is achieved through the formation of therapeutic relationships, underpinned by values of respect for persons, individual right to self-determination, and mutual understanding. The framework identifies four key constructs:

1. **Prerequisites**: Attributes of the nurse (competence, commitment, interpersonal skills, values)
2. **Care Environment**: Context in which care is delivered (skill mix, systems, shared decision-making culture)
3. **Person-Centred Processes**: Working with beliefs and values, engagement, shared decision-making, sympathetic presence
4. **Person-Centred Outcomes**: Satisfaction, involvement, well-being

For this research, the Person-Centred Processes construct is particularly salient. The question becomes: can AI documentation capture evidence of sympathetic presence, engagement with patient values, and shared decision-making as they occur within nursing encounters?

**Complementary Framework 1: Burden of Treatment Theory (May & Montori, 2014)**

The Burden of Treatment Theory examines how healthcare workload affects patient and professional capacity. Applied to this study, it illuminates how documentation burden:
- Depletes nursing capacity for direct patient care
- Creates tension between administrative demands and therapeutic presence
- May be exacerbated or alleviated by AI technologies depending on implementation

This framework guides examination of whether the PCN-I approach reduces documentation burden compared to generic alternatives.

**Complementary Framework 2: Normalisation Process Theory (May & Finch, 2009)**

Normalisation Process Theory (NPT) provides a sociological lens for understanding how new technologies become embedded (or fail to embed) in clinical practice. The four NPT constructs inform Phase 3 of this study:

1. **Coherence**: Do nurses understand what AI documentation is and what it means for their practice?
2. **Cognitive Participation**: Are nurses willing to engage with AI documentation?
3. **Collective Action**: What work is required to implement AI documentation?
4. **Reflexive Monitoring**: How do nurses appraise AI documentation's effects?

Together, these three frameworks enable examination of person-centred care quality (McCormack & McCance), workload implications (May & Montori), and implementation dynamics (May & Finch).

---

## 2. Aim and Research Questions

### 2.1 Aim

To develop and evaluate a Person-Centred Nursing-Informed (PCN-I) AI documentation approach and compare its performance with a generic voice-to-note approach in simulated nursing environments, determining for whom and under what conditions person-centred AI documentation is most effective.

### 2.2 Primary Research Question

Does a Person-Centred Nursing-Informed (PCN-I) AI documentation approach capture significantly more relational and person-centred content in nursing notes than a generic voice-to-note approach?

### 2.3 Secondary Research Questions

**Framework Development (Phase 1)**:
- RQ1a: What indicators of relational and person-centred care can be reliably identified in nursing documentation?
- RQ1b: What consensus exists among nurses, practice development facilitators, and patients/carers regarding priorities for relational care documentation?
- RQ1c: What existing NLP/AI approaches have been applied to nursing documentation, and with what outcomes?

**Comparative Evaluation (Phase 2)**:
- RQ2a: How do PCN-I and generic AI pipelines compare in capturing relational care across different nursing specialties (acute, mental health, community)?
- RQ2b: What types of relational content are most likely to be captured or omitted by each approach?
- RQ2c: How do scenario complexity and patient population characteristics affect AI documentation accuracy?
- RQ2d: What is the factual accuracy and clinical safety profile of each documentation approach?

**Implementation and Acceptability (Phase 3)**:
- RQ3a: What contextual factors enable or constrain effective implementation of AI documentation in nursing?
- RQ3b: How do nurses perceive the impact of AI documentation on their professional identity and therapeutic relationships?
- RQ3c: What risks and unintended consequences do nurses anticipate from AI documentation adoption?
- RQ3d: What training and support needs do nurses identify for safe AI documentation use?

### 2.4 Objectives

1. **Co-produce** a Relational Care Documentation Framework (RCDF) with nurses and public contributors to define measurable indicators of relational care, validated through iterative Delphi consensus.

2. **Develop** a reproducible PCN-I pipeline that utilises Retrieval-Augmented Generation (RAG) based on person-centred nursing scholarship, with prompt engineering derived from the RCDF domains.

3. **Compare** the outputs of the PCN-I pipeline against a generic baseline using blinded scoring of simulated clinical scenarios across diverse nursing contexts.

4. **Evaluate** the acceptability, perceived risks, and implementation barriers of AI documentation in nursing using the NASSS framework (Greenhalgh et al., 2017) and NPT constructs.

5. **Formulate** recommendations for the ethical and safe integration of ambient AI into nursing workflows, informing NHS procurement, clinical education, and policy.

---

## 3. Research Plan and Methodology

### 3.1 Study Design Overview

A sequential, explanatory mixed-methods programme delivered over three years (full-time). This design enables quantitative comparison of AI approaches (Phase 2) to be explained and contextualised through qualitative exploration of implementation dynamics (Phase 3), with both phases grounded in the co-produced RCDF (Phase 1).

The sequential design is essential because:
- The RCDF developed in Phase 1 serves as the measurement instrument for Phase 2
- Quantitative findings from Phase 2 inform the focus of Phase 3 qualitative inquiry
- Integration of quantitative and qualitative strands enables understanding of both *whether* the PCN-I approach works and *why/how* it works

---

### Phase 1: Framework Development (Year 1)

**Step 1.1: Scoping Review (Months 1-4)**

A systematic scoping review following Joanna Briggs Institute methodology (Peters et al., 2020) will address two questions:
1. How is relational or person-centred care currently defined and measured in nursing documentation?
2. What NLP/AI approaches have been applied to nursing notes, and with what outcomes?

*Search Strategy*:
- Databases: CINAHL, MEDLINE, PsycINFO, Scopus, IEEE Xplore (for AI/NLP literature)
- Grey literature: NICE, NHS England, professional body publications
- Date range: 2010-present (reflecting digital health era)
- Key terms: Nursing documentation AND (person-centred OR patient-centred OR relational care OR therapeutic relationship) AND (measure* OR assess* OR evaluat* OR audit*)
- Secondary search: (Nursing notes OR nursing documentation) AND (artificial intelligence OR natural language processing OR machine learning OR speech recognition)

*Selection and Analysis*:
- Two reviewers independently screen using Rayyan systematic review software
- Data extraction using pre-designed forms capturing: study context, definitions of relational care, measurement approaches, AI applications, outcomes, and quality indicators
- Quality appraisal using Mixed Methods Appraisal Tool (MMAT) (Hong et al., 2018)
- Results presented as narrative synthesis with tables mapping indicators and domains

*Output*: Preliminary list of relational care indicators and domains to inform Delphi Round 1.

**Step 1.2: Source Analysis of Person-Centred Nursing Scholarship (Months 2-4)**

Directed content analysis of seminal practice development resources to identify keywords and concepts representing relational practice:

*Sources Analysed*:
- Foundation of Nursing Studies (FoNS) resource archive
- International Practice Development Journal (IPDJ) archive (2011-present)
- McCormack & McCance (2017) Person-Centred Practice Framework primary texts
- Key practice development texts (e.g., McCormack, Manley & Titchen, 2013)

*Analysis Approach*:
- Deductive coding using Person-Centred Practice Framework constructs as initial codes
- Inductive coding of emergent themes representing relational care language
- Development of preliminary lexicon of person-centred terminology for RAG corpus

*Output*: Annotated terminology corpus and coded excerpt database for PCN-I system development.

**Step 1.3: Modified Delphi Study (Months 5-10)**

A three-round modified Delphi study to achieve consensus on the Relational Care Documentation Framework (RCDF) domains, indicators, and scoring anchors.

*Panel Composition (n=20-25)*:
- Registered nurses from diverse specialties (acute medical/surgical, community, mental health, primary care) (n=8-10)
- Practice development facilitators with expertise in person-centred care (n=4-5)
- Nurse academics with documentation/informatics expertise (n=3-4)
- Patient and carer advisors (n=4-5)
- Clinical informaticists (n=1-2)

*Recruitment Strategy*:
- Professional networks (RCN, FoNS, NIHR Clinical Research Networks)
- Academic contacts across UK nursing schools
- Patient and carer recruitment through PPIE networks and carer organisations

*Delphi Process*:

**Round 1** (Months 5-6):
- Online survey presenting preliminary indicators from scoping review
- Open questions inviting additional indicators and domain suggestions
- Analysis: Frequency analysis and thematic coding of open responses

**Round 2** (Months 7-8):
- Refined indicator list with anonymised summary of Round 1 feedback
- Rating of indicator importance (1-9 Likert scale)
- Rating of indicator feasibility for documentation assessment
- Analysis: Median scores, interquartile ranges, and stability analysis

**Round 3** (Months 9-10):
- Final indicator list with scoring anchors
- Rating of overall framework structure and usability
- Consensus threshold: ≥70% agreement within 2-point range on importance scale

*Output*: Validated RCDF with domains, indicators, descriptive anchors, and inter-rater reliability assessment.

---

### Phase 2: Comparative Evaluation (Year 2)

**Step 2.1: Scenario Development (Months 1-4)**

30-40 audio-recorded simulated nursing scenarios will be co-designed with clinical educators and PPIE partners to represent the range of contexts where ACI might be deployed.

*Scenario Specifications*:

| Dimension | Range Included |
|-----------|----------------|
| Healthcare setting | Acute medical, acute surgical, mental health inpatient, community nursing, primary care nursing |
| Complexity | Simple (single issue), moderate (multiple needs), complex (psychosocial complexity) |
| Patient demographics | Range of ages, ethnicities, and communication needs |
| Interaction type | Admission assessment, ongoing care, discharge planning, crisis intervention |
| Duration | 5-15 minutes (reflecting realistic nursing interactions) |

*Development Process*:
1. Draft scenarios developed by research team with clinical education expertise
2. Review by PPIE advisory group to ensure patient perspective authenticity
3. Pilot testing with 3-5 scenarios using volunteer nurses
4. Refinement based on feedback regarding realism and relational content opportunities
5. Finalisation with diversity checklist ensuring representation

*Recording*:
- Professional audio recording in simulation suites
- Scenario actors briefed on person-centred interaction behaviours
- Nursing responses follow semi-structured guides allowing naturalistic variation

**Step 2.2: AI Pipeline Development (Months 3-6)**

Development of two documentation pipelines for comparative evaluation:

*Comparator (Generic Pipeline)*:
- Automatic Speech Recognition: Commercial or open-source ASR (e.g., Microsoft Azure Speech, OpenAI Whisper)
- Large Language Model: Standard LLM (e.g., GPT-4, Llama 2) with generic prompting
- Output structure: SBAR (Situation, Background, Assessment, Recommendation) or SOAP format
- No nursing-specific knowledge base or person-centred prompting

*Intervention (PCN-I Pipeline)*:
- Same ASR component as comparator
- Large Language Model with Retrieval-Augmented Generation (RAG) accessing:
  - Curated corpus of person-centred nursing literature (from Step 1.2)
  - RCDF indicators and definitions
  - NMC Code standards 1-4 (prioritising people)
  - Examples of high-quality person-centred nursing notes
- Custom prompt engineering incorporating:
  - Explicit instruction to capture relational dimensions
  - RCDF domains as structural guidance
  - Examples of desired outputs (few-shot prompting)

*Technical Considerations*:
- Consistent ASR model and settings across both pipelines
- Temperature and other generation parameters standardised
- Version control and reproducibility documentation
- Ethical use of commercial LLMs reviewed through university governance

**Step 2.3: Comparative Experiment (Months 7-11)**

Each simulated scenario audio is processed through both pipelines (randomised order), producing paired documentation outputs for comparison.

*Blinding*:
- Two independent nurse raters score notes using the RCDF
- Raters blinded to generation method (notes de-identified and randomised)
- Inter-rater reliability established through training on calibration set (10% of notes)

*Primary Outcome Measures*:
- Total RCDF score (summed across domains)
- Domain-specific RCDF scores (enabling identification of differential capture)

*Secondary Outcome Measures*:
- Factual accuracy: Clinician verification against source audio (rated 1-5 scale)
- Clinical safety: Identification of omissions with potential patient safety implications
- Readability: Flesch-Kincaid Grade Level and nursing-specific readability assessment
- Editing time: Time required for nurse to review and correct note to acceptable standard

*Sample Size Justification*:
Based on pilot work estimates (effect size d=0.5 for RCDF score difference), paired t-test, α=0.05, power=0.80:
- Minimum n=34 paired observations
- Target n=40 to allow for attrition and subgroup analysis

*Statistical Analysis Plan*:
- Primary analysis: Paired t-test (or Wilcoxon signed-rank if non-normal distribution) comparing total RCDF scores
- Secondary analyses:
  - Repeated measures ANOVA for domain-specific scores
  - Subgroup analyses by scenario complexity and healthcare setting
  - Correlation analysis between scenario characteristics and capture rates
- All analyses using R with pre-registered analysis plan (OSF)

---

### Phase 3: Implementation and Acceptability (Year 3)

**Step 3.1: Qualitative Data Collection (Months 1-6)**

Understanding implementation dynamics through in-depth exploration with nursing professionals.

*Semi-Structured Interviews (n=20-25)*:
- Sample: Registered nurses from diverse settings, bands, and experience levels
- Purposive sampling to include digital champions, sceptics, and varied technology comfort levels
- Recruitment: NHS Trust partnerships, professional networks, social media
- Duration: 45-60 minutes, conducted via Teams or in-person per participant preference

*Topic Guide Domains* (informed by NASSS and NPT):
1. Current documentation experiences and challenges
2. Responses to AI-generated note examples (from Phase 2)
3. Perceived impact on therapeutic relationships
4. Professional identity implications
5. Implementation barriers and enablers
6. Training and support needs
7. Patient safety considerations
8. Future vision for nursing documentation

*Focus Groups (n=2-3, 6-8 participants each)*:
- Group composition: Mixed specialty groups to enable cross-pollination
- Duration: 90 minutes
- Focus: Collective sense-making, points of consensus and divergence
- One group specifically includes digital nursing leads/champions

**Step 3.2: Qualitative Analysis (Months 4-9)**

*Analytical Framework*:
- Reflexive Thematic Analysis (Braun & Clarke, 2019, 2021) as primary approach
- Analysis mapped against:
  - NASSS framework domains (condition, technology, value proposition, adopter system, organisation, wider system, embedding over time)
  - NPT constructs (coherence, cognitive participation, collective action, reflexive monitoring)

*Process*:
1. Transcription and familiarisation
2. Initial coding using NVivo software
3. Collation into candidate themes
4. Review against NASSS and NPT constructs
5. Refinement and definition
6. Member checking with subset of participants

**Step 3.3: Mixed-Methods Integration (Months 8-11)**

Integration of quantitative (Phase 2) and qualitative (Phase 3) findings using established integration approaches:

*Joint Display Analysis*:
- Visual matrix comparing: scenario characteristics, quantitative outcomes, and qualitative themes
- Identification of convergence, divergence, and complementarity
- Examination of explanatory mechanisms: e.g., why certain scenario types showed greater PCN-I advantage

*Integration Questions*:
- Do qualitative findings explain which aspects of relational care are hardest for AI to capture?
- What contextual factors identified by nurses correspond to quantitative subgroup differences?
- How do professional identity concerns relate to acceptability of high-performing AI vs. low-performing AI?

*Output*: Integrated findings with implications for implementation guidance.

---

## 4. Timeline and Milestones

### Year 1: Framework Development

| Period | Activities | Milestones |
|--------|------------|------------|
| Months 1-4 | Scoping review, source analysis, ethics approval | Scoping review completed; ethics approved |
| Months 5-6 | Delphi Round 1: indicator identification | Round 1 data collected; preliminary analysis |
| Months 7-8 | Delphi Round 2: importance rating | Round 2 complete; consensus emerging |
| Months 9-10 | Delphi Round 3: finalisation | RCDF validated; scoring anchors confirmed |
| Months 11-12 | RCDF documentation, inter-rater reliability testing | **MILESTONE: RCDF published; Year 1 report** |

### Year 2: Development and Comparative Evaluation

| Period | Activities | Milestones |
|--------|------------|------------|
| Months 1-4 | Scenario development and co-design | 40 scenarios finalised and recorded |
| Months 3-6 | AI pipeline development | Both pipelines operational and tested |
| Months 7-9 | Comparative experiment data collection | All scenarios processed; notes scored |
| Months 10-11 | Statistical analysis | Primary and secondary analyses complete |
| Month 12 | Write-up and conference presentation | **MILESTONE: Experimental findings published** |

### Year 3: Implementation Research and Integration

| Period | Activities | Milestones |
|--------|------------|------------|
| Months 1-4 | Interview and focus group recruitment and data collection | 20-25 interviews, 2-3 focus groups completed |
| Months 4-8 | Qualitative analysis | Thematic analysis complete; NASSS/NPT mapping |
| Months 8-10 | Mixed-methods integration | Joint display analysis; integrated findings |
| Months 10-12 | Implementation toolkit; thesis writing | **MILESTONE: PhD thesis submitted; toolkit published** |

---

## 5. Patient and Public Involvement and Engagement (PPIE)

Consistent with NIHR standards (NIHR, 2021; UK Standards for Public Involvement, 2019), PPIE is embedded throughout the research cycle, moving beyond consultation to co-production.

### 5.1 Pre-Project Development

This research was shaped by preliminary discussions with:
- Patients who have experienced nursing care and reflected on what 'good' documentation should capture
- Carers who have navigated healthcare systems and noted gaps in how their perspectives were recorded
- Nurses who have expressed frustration with documentation capturing 'what I did' but not 'who I am as a nurse'

These conversations identified the core tension between efficiency and visibility that this research addresses.

### 5.2 Project Governance

**PPIE Advisory Group**:
- Two patient/carer advisors serve as full members of the project steering group
- Equal voice in strategic decisions, methodology refinement, and dissemination priorities
- Compensated at NIHR INVOLVE rates (£25/hour plus expenses)
- Supported through accessible meeting formats and materials

**Steering Group Composition**:
- Supervisory team (academic oversight)
- Two patient/carer advisors (lived experience perspective)
- One clinical educator (simulation expertise)
- One digital nursing lead (implementation perspective)
- One informaticist (technical expertise)

### 5.3 PPIE Throughout Research Phases

**Phase 1: Framework Development**:
- 4-5 patient/carer representatives included in Delphi panel
- Public contributors review and validate that RCDF reflects patient priorities, not just professional/clinical constructs
- "What matters to me" perspective explicitly incorporated in indicator development

**Phase 2: Scenario Development**:
- PPIE group co-designs simulated scenarios ensuring they reflect authentic patient experiences
- Patient advisors review scenarios for: realistic patient voice, meaningful relational opportunities, diversity of experiences represented
- Advisors provide feedback on AI-generated notes from patient perspective: "Would I recognise myself in this note?"

**Phase 3: Interpretation and Dissemination**:
- Lay advisors participate in interpreting qualitative findings
- Co-production of accessible summaries for patient audiences
- Patient-authored commentary for key publications

### 5.4 Support and Resources

- Payment per NIHR INVOLVE guidance (£25/hour plus expenses)
- All materials available in accessible formats (plain language, large print as needed)
- Meeting times accommodating diverse schedules
- Training offered on research methods for interested advisors
- Recognition through acknowledgement and co-authorship where appropriate

---

## 6. Inclusion, Equality and Diversity (EDI)

The project adheres to NIHR (2025) Inclusive Research Funding guidance, recognising that AI systems can perpetuate or amplify existing biases if developed without explicit equity consideration.

### 6.1 Workforce Diversity in Participation

Recruitment for the Delphi panel and interview phases will purposefully sample for diversity in:
- **Ethnicity**: Ensuring representation of nurses from diverse ethnic backgrounds, recognising the UK nursing workforce's diversity
- **Gender**: Including male nurses and non-binary practitioners
- **Disability**: Accessible participation options for nurses with disabilities
- **Neurodiversity**: Flexible participation formats accommodating different communication preferences
- **Career stage**: From newly registered nurses to experienced practitioners
- **Specialty**: Urban and rural, NHS and independent sector

### 6.2 AI Bias Considerations

**Corpus Screening**:
- The training corpus for RAG will be systematically screened for exclusionary language
- Analysis of whose voices are represented in person-centred scholarship (historically predominantly White, Western perspectives)
- Intentional inclusion of scholarship addressing cultural humility, anti-racist practice, and diverse therapeutic relationships

**Scenario Diversity**:
- Simulated scenarios will explicitly represent:
  - Patients from diverse ethnic and cultural backgrounds
  - LGBTQ+ patients and considerations
  - Patients with disabilities and communication differences
  - Patients experiencing socioeconomic disadvantage
  - Older and younger adults
  - Different family structures and dynamics

**Testing for Differential Performance**:
- Secondary analysis will examine whether PCN-I performance varies by patient demographic characteristics in scenarios
- Identification of any populations for whom AI documentation performs differently

### 6.3 Accessibility of Outputs

- RCDF designed for accessibility to diverse nursing workforce
- Implementation guidelines available in multiple formats
- Plain language summaries for all publications

---

## 7. Ethics and Governance

### 7.1 Ethical Approvals

- **University Ethics**: Approval sought from University Ethics Committee prior to Delphi study commencement
- **NHS HRA Approval**: Health Research Authority approval obtained for recruitment of NHS staff (Phase 3)
- **Trust-Level Approvals**: Site-specific agreements for NHS recruitment sites

### 7.2 Clinical Safety Considerations

The study operates within a simulation environment (Phase 2), mitigating direct patient risk. Nevertheless, safety is paramount:

- All AI outputs evaluated against NHS Digital Clinical Safety Standards:
  - DCB0129: Clinical Risk Management in Health IT Manufacture
  - DCB0160: Clinical Risk Management in Health IT Deployment
- Hazard identification and clinical risk assessment documented
- Safety metrics included in Phase 2 outcomes (factual accuracy, omission analysis)
- Recommendations explicitly address safety governance for real-world deployment

### 7.3 Data Protection

- **No Real Patient Data**: The AI models trained and tested use simulated data only
- **Participant Data**: Delphi responses, interview recordings, and transcripts stored securely per GDPR requirements
- **Anonymisation**: All Phase 3 transcripts anonymised; quotes reviewed to prevent identification
- **Data management plan**: Pre-registered with university research data service

### 7.4 Responsible AI Considerations

- Transparency: Full documentation of AI pipeline architecture and prompting strategies
- Reproducibility: Code and prompts published (open source where possible)
- Governance: Engagement with institutional AI ethics review processes
- Human oversight: Position that AI documentation requires human review, not replacement

---

## 8. Dissemination and Impact

### 8.1 Research Outputs

**Primary Outputs**:
1. **Relational Care Documentation Framework (RCDF)**: A validated, reliable tool for auditing nursing notes' person-centred content
2. **PCN-I Pipeline Documentation**: Open-source or reproducible methodology for person-centred AI documentation
3. **Implementation Toolkit**: Evidence-based guidance for NHS Trusts deploying ambient AI in nursing

**Academic Dissemination**:
- Peer-reviewed publications in:
  - Nursing informatics journals (e.g., *Journal of the American Medical Informatics Association*, *Journal of Nursing Scholarship*)
  - Practice development journals (e.g., *International Practice Development Journal*, *International Journal of Nursing Studies*)
  - Digital health journals (e.g., *npj Digital Medicine*, *JMIR*)
- Conference presentations: RCN Congress, AMIA Nursing Informatics, EPFIC (European Practice Development Network)
- Pre-print sharing and open access publication where possible

### 8.2 Knowledge Mobilisation Strategy

**For NHS Decision-Makers**:
- Briefings for NHS England Digital Transformation portfolio
- Presentations at NHS Confederation digital health events
- Engagement with Integrated Care Systems deploying voice technology

**For Technology Developers**:
- Industry engagement sharing findings and RCDF
- Developer-focused guidance on incorporating person-centred evaluation
- Contributions to AI governance and standards development

**For Clinical Communities**:
- Resources for nursing informatics leads
- Education materials for pre-registration and post-registration nursing curricula
- Practice development resources for organisations implementing AI documentation

**For Patients and Public**:
- Plain language summaries distributed through patient advocacy organisations
- Involvement of PPIE group in dissemination activities
- Accessible materials explaining AI documentation and patient rights

### 8.3 Trajectory to Patient Benefit

**Immediate Impact** (during/post-PhD):
- Tools and frameworks available for use by NHS organisations and researchers
- Evidence base informing procurement decisions
- Contribution to emerging NHS AI governance standards

**Short-term** (1-3 years post-PhD):
- Pilot implementations of PCN-I approach in NHS Trusts
- RCDF used as audit tool in practice settings
- Further research validating and extending findings

**Medium-term** (3-5 years):
- Integration of person-centred criteria into NHS procurement standards for voice technology
- Professional body guidance on AI documentation incorporating findings
- Nursing education curricula addressing AI-human documentation collaboration

**Long-term** (5+ years):
- Transformed documentation landscape where AI supports rather than erodes nursing's relational essence
- Nursing's "invisible work" made visible in digital health records
- Reduced documentation burden WITH maintained care quality

This trajectory demonstrates how foundational research creates pathways to patient benefit through evidence-informed policy, practice, and technology development.

---

## 9. Indicative Resource Requirements

*Note: Specific figures would be confirmed based on institutional context and funding source.*

### 9.1 Staff Costs

| Item | Justification |
|------|---------------|
| PhD Stipend (3 years FTE or 4 years PTE) | Applicant salary/stipend |
| Supervisor Time | Academic oversight and mentorship |
| Technical Support | AI pipeline development expertise (if required) |

### 9.2 Research Costs

| Item | Justification |
|------|---------------|
| PPIE Payments | Delphi panel, advisory group, co-production activities (NIHR rates) |
| Transcription Services | Interview and focus group transcription |
| Software Licences | NVivo, statistical software, survey platform |
| API Costs | ASR and LLM usage for pipeline development and testing |
| Simulation Costs | Recording facilities, scenario actor time |

### 9.3 Dissemination Costs

| Item | Justification |
|------|---------------|
| Conference Attendance | 2-3 national/international conferences |
| Open Access Fees | Publication costs for open access mandates |
| Toolkit Production | Design and dissemination of implementation resources |

### 9.4 Other Costs

| Item | Justification |
|------|---------------|
| Consumables | Printing, stationery, participant materials |
| Travel | Data collection travel, stakeholder engagement |

---

## 10. References

Aiken, L. H., Sloane, D. M., Barnes, H., Cimiotti, J. P., Jarrín, O. F., & McHugh, M. D. (2023). Nurses' and patients' appraisals of hospital nurse staffing policies and patient safety: A cross-sectional study. *BMJ Quality & Safety*, 32(2), 86-93.

Allen, D. (2014). *The Invisible Work of Nurses: Hospitals, Organisation and Healthcare*. London: Routledge.

Allen, D. (2015). Inside 'the black box' of nursing work: Researching the invisible. *International Journal of Nursing Studies*, 52(12), 1835-1838.

Ball, J. E., Bruyneel, L., Aiken, L. H., Sermeus, W., Sloane, D. M., Rafferty, A. M., ... & Consortium, R. C. (2017). Post-operative mortality, missed care and nurse staffing in nine countries: A cross-sectional study. *International Journal of Nursing Studies*, 78, 10-15.

Baumann, L. A., Baker, J., & Elshaug, A. G. (2018). The impact of electronic health record systems on clinical documentation times: A systematic review. *Health Policy*, 122(8), 827-836.

Blair, W., & Smith, B. (2012). Nursing documentation: Frameworks and barriers. *Contemporary Nurse*, 41(2), 160-168.

Braun, V., & Clarke, V. (2019). Reflecting on reflexive thematic analysis. *Qualitative Research in Sport, Exercise and Health*, 11(4), 589-597.

Braun, V., & Clarke, V. (2021). Thematic analysis: A practical guide. London: SAGE.

Care Quality Commission. (2023). *Assessment framework for health and social care services*. London: CQC.

de Groot, K., Triemstra, M., Paans, W., & Francke, A. (2022). Nursing documentation and its relationship with perceived nursing workload: A mixed-methods study among community nurses. *BMC Nursing*, 21, 34.

Dewing, J., McCance, T., & McCormack, B. (2021). Person-centred care and nursing leadership: A critical synthesis. *Journal of Nursing Management*, 29(5), 1101-1107.

Duffield, C., Diers, D., Aisbett, C., & Roche, M. (2021). Chasing the ambulance: The emerging crisis in the preservation of nursing expertise and knowledge. *Journal of Clinical Nursing*, 30(1-2), 159-169.

Finley, G., Edwards, E., Robinson, A., Brenndoerfer, M., Sadoughi, N., Fone, J., Aber, M., & Stolcke, A. (2018). An automated medical scribe for documenting clinical encounters. *Proceedings of NAACL-HLT 2018*, 11-15.

Foundation of Nursing Studies. (n.d.). Resources and International Practice Development Journal (IPDJ) archive. Available at: fons.org

Greenhalgh, T., Wherton, J., Papoutsi, C., Lynch, J., Hughes, G., A'Court, C., ... & Shaw, S. (2017). Beyond adoption: A new framework for theorizing and evaluating nonadoption, abandonment, and challenges to the scale-up, spread, and sustainability of health and care technologies. *Journal of Medical Internet Research*, 19(11), e367.

Heartfield, M. (1996). Nursing documentation and nursing practice: A discourse analysis. *Journal of Advanced Nursing*, 24(1), 98-103.

Hong, Q. N., Pluye, P., Fàbregues, S., Bartlett, G., Boardman, F., Cargo, M., ... & Vedel, I. (2018). Mixed methods appraisal tool (MMAT), version 2018. *Registration of Copyright*, 1148552.

May, C., & Finch, T. (2009). Implementing, embedding, and integrating practices: An outline of normalization process theory. *Sociology*, 43(3), 535-554.

May, C. R., & Montori, V. M. (2014). Rethinking the patient: Using burden of treatment theory to understand the changing dynamics of illness. *BMC Health Services Research*, 14, 281.

McCormack, B., & McCance, T. (2017). *Person-Centred Practice in Nursing and Health Care: Theory and Practice* (2nd ed.). Chichester: Wiley-Blackwell.

McCormack, B., Manley, K., & Titchen, A. (Eds.). (2013). *Practice Development in Nursing and Healthcare* (2nd ed.). Chichester: Wiley-Blackwell.

NHS England. (2019). *The NHS Long Term Plan*. London: NHS England.

NHS England. (2021). *What Good Looks Like: A framework for digital health and social care*. London: NHS England.

NHS England Digital. (2018). *DCB0129: Clinical Risk Management: its Application in the Manufacture of Health IT Systems*. London: NHS England.

NHS England Digital. (2018). *DCB0160: Clinical Risk Management: its Application in the Deployment and Use of Health IT Systems*. London: NHS England.

NHS England Digital. (2025). *Digital clinical safety assurance* (Version 1.2). London: NHS England.

NIHR. (2021). *Briefing notes for researchers: Public involvement in NHS, health and social care research*. National Institute for Health and Care Research.

NIHR. (2024). *Payment guidance for researchers and professionals*. National Institute for Health and Care Research.

NIHR. (2025). *Guidance for applicants on working with people and communities*. National Institute for Health and Care Research.

NIHR. (2025). *Inclusive research funding application guidance*. National Institute for Health and Care Research.

Nursing and Midwifery Council. (2018). *The Code: Professional standards of practice and behaviour for nurses, midwives and nursing associates*. London: NMC.

Peters, M. D., Marnie, C., Tricco, A. C., Pollock, D., Munn, Z., Alexander, L., ... & Khalil, H. (2020). Updated methodological guidance for the conduct of scoping reviews. *JBI Evidence Synthesis*, 18(10), 2119-2126.

Royal College of Nursing. (2019). *Employment survey 2019*. London: RCN.

Staggers, N., & Blaz, J. W. (2013). Research on nursing handoffs for medical and surgical settings: An integrative review. *Journal of Advanced Nursing*, 69(2), 247-262.

UK Standards for Public Involvement. (2019). *UK Standards for Public Involvement in Research*.

Wendt, S. J., Dinh, C. T., Sutcliffe, M., Wright, M., Sandhu, P., Luery, J., & Celi, L. A. (2025). Deploying ambient clinical intelligence to improve care: Assessing the impact of Nuance DAX on documentation burden and burnout. *Future Healthcare Journal*, 12(3), 100450.