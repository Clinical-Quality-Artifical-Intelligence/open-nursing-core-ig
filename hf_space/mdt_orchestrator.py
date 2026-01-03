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
        
        # Simple, direct instruction without external dependencies
        instruction = """You are leading a Virtual MDT. Analyze this patient case and provide a CONCISE care plan.

FORMAT YOUR RESPONSE EXACTLY LIKE THIS:
## MDT Discussion Summary

**Patient:** [1 sentence summary]

### Key Specialist Findings:
- 🩹 Tissue Viability: [1 bullet point]
- 💚 Relational Care: [1 bullet point]
- 🛡️ Patient Safety: [PASS/FAIL for safety gates]

### Recommended Care Actions:
1. [Action 1]
2. [Action 2]
3. [Action 3]

DO NOT REPEAT YOURSELF. BE EXTREMELY CONCISE. MAX 200 WORDS TOTAL."""
        
        final_output = ""
        for chunk in self.generate_fn(instruction, patient_case, max_tokens=250):
            final_output = chunk
            yield chunk
        
        yield "\n\n---\n✅ **MDT Complete**"
