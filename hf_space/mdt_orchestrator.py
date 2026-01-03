"""
MDT Orchestrator: Virtual Multi-Disciplinary Team for Nursing Care
===================================================================
This module implements a multi-agent system where specialized AI personas
collaborate to produce "Super-Gold" standard care plans.

The agents are:
1. Clinical Coordinator: Orchestrates the discussion and synthesizes the final plan.
2. Tissue Viability Specialist: Focuses on skin assessment and equity.
3. Relational Facilitator: Ensures empathy and person-centred language.
4. Patient Safety Auditor: Validates against Phase 8 Safety Gates.
"""

from dataclasses import dataclass
from typing import Generator, List

# =============================================================================
# AGENT DEFINITIONS (System Prompts)
# =============================================================================

AGENT_PROMPTS = {
    "coordinator": """You are the Clinical Coordinator leading a Multi-Disciplinary Team (MDT) meeting.
Your role is to:
1. Summarize the patient case.
2. Facilitate input from the Tissue Viability Specialist, Relational Facilitator, and Safety Auditor.
3. Synthesize their contributions into a unified, "Super-Gold" standard Care Plan.
Keep your summary concise and structured using ADPIE (Assessment, Diagnosis, Planning, Implementation, Evaluation).""",

    "tissue_viability": """You are a Tissue Viability Nurse Specialist.
Your role is to review patient documentation for:
1. Skin assessment completeness (especially for ALL skin tones).
2. Pressure ulcer risk factors (Braden, Waterlow, PURPOSE-T).
3. Wound care appropriateness.
CRITICAL: If the patient has dark skin (Fitzpatrick IV-VI or Monk 7-10), ensure the documentation uses 
sub-epidermal moisture scanning or palpation, NOT just visual erythema checks.
Flag any equity gaps in skin assessment.""",

    "relational_lead": """You are a Relational Care Facilitator, trained in FONS person-centred practice.
Your role is to review patient documentation for:
1. Use of person-centred language (avoid 'non-compliant', 'refused', 'poor historian').
2. Evidence of "What Matters to Me" conversations.
3. The patient's preferred name, cultural needs, and personal goals.
Score the Empathy Index (1-5) and suggest relational interventions if low.""",

    "safety_auditor": """You are a Patient Safety Auditor.
Your role is to validate documentation against the Phase 8 "Super-Gold" Safety Gates:
1. [Mobility Gate]: If 'bedbound', is a Pressure Ulcer Risk Assessment documented?
2. [Nutrition Gate]: If 'dysphagia', is a 'Protected Mealtimes' or swallow plan mentioned?
3. [Hygiene Gate]: If 'NBM', is Oral Care frequency specified?
4. [Elimination Gate]: If 'catheter', is the specific device/size mentioned?
Output PASS or FAIL for each gate with a brief reason.""",
}


@dataclass
class AgentResponse:
    """Represents a single agent's contribution to the MDT discussion."""
    agent_name: str
    agent_icon: str
    response: str


class MDTOrchestrator:
    """
    Orchestrates a multi-agent discussion on a patient case.
    Uses the same underlying model but with different system prompts.
    """

    def __init__(self, generate_fn):
        """
        Args:
            generate_fn: A function that takes (instruction, context, max_tokens) 
                         and yields text chunks. This is the core LLM call.
        """
        self.generate_fn = generate_fn
        self.agent_order = [
            ("tissue_viability", "🩹", "Tissue Viability Specialist"),
            ("relational_lead", "💚", "Relational Facilitator"),
            ("safety_auditor", "🛡️", "Patient Safety Auditor"),
        ]

    def run_discussion(self, patient_case: str) -> Generator[str, None, None]:
        """
        Runs the MDT discussion and yields a formatted log of the conversation.
        
        Args:
            patient_case: The clinical note or scenario to discuss.
            
        Yields:
            Formatted markdown strings showing the MDT discussion.
        """
        discussion_log = []
        
        # 1. Get initial perspectives from each specialist
        yield "## 🏥 Virtual MDT Discussion\n\n"
        
        for agent_key, icon, display_name in self.agent_order:
            yield f"### {icon} {display_name}\n"
            
            system_prompt = AGENT_PROMPTS[agent_key]
            instruction = f"{system_prompt}\n\nReview this patient case and provide your specialist input."
            
            agent_response = ""
            for chunk in self.generate_fn(instruction, patient_case, max_tokens=300):
                agent_response = chunk
                yield chunk
            
            discussion_log.append(AgentResponse(display_name, icon, agent_response))
            yield "\n\n---\n\n"
        
        # 2. Coordinator synthesizes the final plan
        yield "### 📋 Clinical Coordinator: Final Synthesis\n"
        
        synthesis_context = f"""Patient Case:
{patient_case}

---
MDT Input:

{chr(10).join([f'{r.agent_icon} {r.agent_name}: {r.response}' for r in discussion_log])}
"""
        
        coordinator_instruction = f"""{AGENT_PROMPTS['coordinator']}

Based on the specialist input above, synthesize a final, unified "Super-Gold" Care Plan."""
        
        for chunk in self.generate_fn(coordinator_instruction, synthesis_context, max_tokens=500):
            yield chunk
        
        yield "\n\n---\n✅ **MDT Discussion Complete**"


# =============================================================================
# Standalone Test (for local development)
# =============================================================================
if __name__ == "__main__":
    # Mock generate function for testing
    def mock_generate(instruction, context, max_tokens):
        yield f"[Mock response for: {instruction[:50]}...]"
    
    orchestrator = MDTOrchestrator(mock_generate)
    
    test_case = "78-year-old patient, dark skin tone, bedbound, NBM, catheter in situ."
    
    print("--- Starting MDT Test ---")
    for output in orchestrator.run_discussion(test_case):
        print(output, end="")
    print("\n--- MDT Test Complete ---")
