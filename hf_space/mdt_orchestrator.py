"""
MDT Orchestrator: Virtual Multi-Disciplinary Team for Nursing Care
===================================================================
Simplified version: No RAG, No Memory, Just pure MDT synthesis.
"""

from typing import Generator

class MDTOrchestrator:
    """
    Simplified MDT that produces a single concise output.
    """

    def __init__(self, generate_fn):
        self.generate_fn = generate_fn

    def run_discussion(self, patient_case: str) -> Generator[str, None, None]:
        """
        Runs a simplified MDT and yields a concise care plan.
        """
        yield "🏥 *Starting Virtual MDT Analysis...*\n\n"
        
        # ARCHITECTURE CHANGE: SEQUENTIAL AGENTS
        # Instead of one big prompt (which loops), we call each specialist individually.
        
        # 1. Tissue Viability Agent
        yield "### 🩹 Tissue Viability\n"
        prompt_tv = f"""Role: Tissue Viability Nurse.
Task: Assess skin risks (Waterlow), wounds, and device pressure for this patient: "{patient_case}"
Output: 3 bullet points. NO INTRO. NO OUTRO."""
        for chunk in self.generate_fn(prompt_tv, patient_case, max_tokens=100):
            yield chunk
        yield "\n\n"

        # 2. Relational Care Agent
        yield "### 💚 Relational Care\n"
        prompt_rel = f"""Role: Relational Care Lead.
Task: Identify emotional needs, preferences, and cultural dignity for this patient: "{patient_case}"
Output: 3 bullet points. NO INTRO. NO OUTRO."""
        for chunk in self.generate_fn(prompt_rel, patient_case, max_tokens=100):
            yield chunk
        yield "\n\n"

        # 3. Safety Agent
        yield "### 🛡️ Patient Safety\n"
        prompt_safe = f"""Role: Safety Auditor.
Task: Check for sepsis (NEWS2), falls risk, and allergies for this patient: "{patient_case}"
Output: 3 bullet points. NO INTRO. NO OUTRO."""
        for chunk in self.generate_fn(prompt_safe, patient_case, max_tokens=100):
            yield chunk
        yield "\n\n"

        # 4. Consensus Plan
        yield "### 📋 Consensus Plan\n"
        prompt_plan = f"""Role: MDT Chair.
Task: Create a numbered list of 3 actionable care steps for: "{patient_case}"
Output: Numbered list only. NO INTRO. NO OUTRO."""
        for chunk in self.generate_fn(prompt_plan, patient_case, max_tokens=100):
            yield chunk
        
        yield "\n\n---\n✅ **MDT Complete**"
