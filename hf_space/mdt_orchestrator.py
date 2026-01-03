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
        
        # Ultra-Strict Prompt to prevent looping
        instruction = """You are leading a Virtual MDT. Analyze this patient case and provide a SHORT summary.
        
OUTPUT FORMAT:
**Patient**: [Name/Age/Condition]

**Key Findings**:
* [Finding 1]
* [Finding 2]

**Actions**:
1. [Action 1]
2. [Action 2]

KEEP IT UNDER 100 WORDS. DO NOT REPEAT SECTIONS."""
        
        final_output = ""
        # Increased max_tokens slightly to allow natural finish, but reliance is on repetition_penalty
        for chunk in self.generate_fn(instruction, patient_case, max_tokens=300):
            final_output = chunk
            yield chunk
        
        yield "\n\n---\n✅ **MDT Complete**"
