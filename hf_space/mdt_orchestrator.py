"""
MDT Orchestrator: Virtual Multi-Disciplinary Team for Nursing Care
===================================================================
Simplified version that produces a single concise care plan summary.
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
        yield "🏥 *Running Virtual MDT Analysis...*\n\n"
        
        instruction = """You are leading a Virtual MDT. Analyze this patient case and provide a CONCISE care plan.

FORMAT YOUR RESPONSE EXACTLY LIKE THIS:
## MDT Summary

**Patient:** [1 sentence summary]

### Key Findings:
- 🩹 Skin/Tissue: [1 bullet point]
- 💚 Relational: [1 bullet point about person-centred care]
- 🛡️ Safety: [PASS/FAIL for each gate: Mobility, Nutrition, Hygiene, Elimination]

### Recommended Actions:
1. [Action 1]
2. [Action 2]
3. [Action 3]

DO NOT REPEAT YOURSELF. BE EXTREMELY CONCISE. MAX 150 WORDS TOTAL."""
        
        final_output = ""
        for chunk in self.generate_fn(instruction, patient_case, max_tokens=200):
            final_output = chunk
            yield chunk
        
        yield "\n\n---\n✅ **MDT Complete**"
