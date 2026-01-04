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
        Runs a simplified MDT. NON-STREAMING to avoid Gradio issues.
        Collects all outputs, then yields the final formatted result.
        """
        yield "🏥 *Analyzing patient case... Please wait...*"
        
        # Helper to get final output from generator
        def get_response(prompt: str) -> str:
            result = ""
            for chunk in self.generate_fn(prompt, patient_case, max_tokens=100):
                result = chunk  # Each chunk is cumulative, so last one is complete
            return result.strip()
        
        # 1. Tissue Viability Agent
        prompt_tv = """Role: Tissue Viability Nurse.
Task: Assess skin risks (Waterlow), wounds, and device pressure for this patient.
Output: Exactly 3 bullet points starting with "- ". Be concise. NO intro, NO outro."""
        tv_output = get_response(prompt_tv)
        
        # 2. Relational Care Agent
        prompt_rel = """Role: Relational Care Lead.
Task: Identify emotional needs, preferences, and cultural dignity for this patient.
Output: Exactly 3 bullet points starting with "- ". Be concise. NO intro, NO outro."""
        rel_output = get_response(prompt_rel)
        
        # 3. Safety Agent
        prompt_safe = """Role: Safety Auditor.
Task: Check for sepsis risk (NEWS2), falls risk, and allergies for this patient.
Output: Exactly 3 bullet points starting with "- ". Be concise. NO intro, NO outro."""
        safe_output = get_response(prompt_safe)
        
        # 4. Consensus Plan
        prompt_plan = """Role: MDT Chair.
Task: Create 3 actionable care steps for this patient.
Output: Numbered list (1. 2. 3.) only. Be concise. NO intro, NO outro."""
        plan_output = get_response(prompt_plan)
        
        # Assemble final output
        final_output = f"""🏥 **Virtual MDT Summary**

### 🩹 Tissue Viability
{tv_output}

### 💚 Relational Care
{rel_output}

### 🛡️ Patient Safety
{safe_output}

### 📋 Consensus Plan
{plan_output}

---
✅ **MDT Complete**"""
        
        yield final_output


