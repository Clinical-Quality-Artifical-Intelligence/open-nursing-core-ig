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
        CRITICAL: Gradio streaming requires yielding the FULL accumulated output each time.
        """
        full_output = "🏥 *Starting Virtual MDT Analysis...*\n\n"
        yield full_output
        
        # Helper to stream an agent and accumulate output
        def stream_agent(prompt: str, header: str) -> None:
            nonlocal full_output
            full_output += header
            yield full_output
            
            last_chunk = ""
            for chunk in self.generate_fn(prompt, patient_case, max_tokens=100):
                last_chunk = chunk
                yield full_output + chunk
            
            full_output += last_chunk + "\n\n"
        
        # 1. Tissue Viability Agent
        prompt_tv = f"""Role: Tissue Viability Nurse.
Task: Assess skin risks (Waterlow), wounds, and device pressure for this patient.
Output: 3 bullet points starting with "- ". NO INTRO. NO OUTRO."""
        for out in stream_agent(prompt_tv, "### 🩹 Tissue Viability\n"):
            yield out

        # 2. Relational Care Agent
        prompt_rel = f"""Role: Relational Care Lead.
Task: Identify emotional needs, preferences, and cultural dignity for this patient.
Output: 3 bullet points starting with "- ". NO INTRO. NO OUTRO."""
        for out in stream_agent(prompt_rel, "### 💚 Relational Care\n"):
            yield out

        # 3. Safety Agent
        prompt_safe = f"""Role: Safety Auditor.
Task: Check for sepsis (NEWS2), falls risk, and allergies for this patient.
Output: 3 bullet points starting with "- ". NO INTRO. NO OUTRO."""
        for out in stream_agent(prompt_safe, "### 🛡️ Patient Safety\n"):
            yield out

        # 4. Consensus Plan
        prompt_plan = f"""Role: MDT Chair.
Task: Create a numbered list of 3 actionable care steps for this patient.
Output: Numbered list (1. 2. 3.) only. NO INTRO. NO OUTRO."""
        for out in stream_agent(prompt_plan, "### 📋 Consensus Plan\n"):
            yield out
        
        full_output += "---\n✅ **MDT Complete**"
        yield full_output

