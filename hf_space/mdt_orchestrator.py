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
from rag_engine import RelationalRAG
from memory_manager import MemoryManager

# =============================================================================
# AGENT DEFINITIONS (System Prompts)
# =============================================================================

AGENT_PROMPTS = {
    "coordinator": """You are the Clinical Coordinator leading a Multi-Disciplinary Team (MDT) meeting.
Your role is to:
1. Synthesize contributions into a unified, "Super-Gold" standard Care Plan.
2. Provide a 'Executive Summary' (3 sentences max) at the start.
3. Use a structured ADPIE format for the details.
Keep the entire output concise and actionable.""",

    "tissue_viability": """You are a Tissue Viability Nurse Specialist.
Provide your input in exactly 2-3 concise bullet points focusing on:
1. Skin assessment completeness (especially for ALL skin tones).
2. Pressure ulcer risk factors.
CRITICAL: If dark skin (Fitzpatrick IV-VI), ensure PALPATION is documented.
BE EXTREMELY CONCISE.""",

    "relational_lead": """You are a Relational Care Facilitator.
Provide your input in exactly 2-3 concise bullet points focusing on:
1. Person-centred language (avoid jargon).
2. "What Matters to Me" evidence.
3. Empathy Index Score (1-5).
BE EXTREMELY CONCISE.""",

    "safety_auditor": """You are a Patient Safety Auditor.
Validate Phase 8 "Super-Gold" Safety Gates.
Output ONLY a table or list:
- [Gate Name]: [PASS/FAIL] - [1-sentence reason]
BE EXTREMELY CONCISE.""",
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
        self.rag = RelationalRAG("knowledge_base/fons_knowledge.jsonl")
        self.memory = MemoryManager("knowledge_base/patient_memory.json")
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
        
        # 0. Search for relevant evidence and memory first
        yield "🔍 *Checking Evidence Hub and Person-Centred Memory...*\n\n"
        search_results = self.rag.search(patient_case)
        evidence_context = self.rag.format_context(search_results)
        
        memory_context = self.memory.get_patient_context(patient_case)
        if memory_context:
            yield f"💡 *Memory Found:* {memory_context.splitlines()[0]}\n\n"
        else:
            memory_context = ""

        # 1. Get initial perspectives from each specialist
        yield "## 🏥 Virtual MDT Discussion\n\n"
        
        for agent_key, icon, display_name in self.agent_order:
            yield f"### {icon} {display_name}\n"
            
            system_prompt = AGENT_PROMPTS[agent_key]
            instruction = f"{system_prompt}\n\n{evidence_context}\n\n{memory_context}\n\nReview this patient case using the EVIDENCE and MEMORY provided above."
            
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
