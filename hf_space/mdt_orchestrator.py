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
        
        # Ultra-Strict Prompt with Explicit Agent Headers
        instruction = """You are the Chair of a Virtual MDT. Review the patient case and provide a summary from three specialists.

USE THIS EXACT FORMAT:

### 🩹 Tissue Viability
* [Assess skin integrity, pressure risks (Waterlow), and device issues]

### 💚 Relational Care
* [Identify patient preferences, cultural needs, or emotional state]

### 🛡️ Patient Safety
* [Verify safety gates like NEWS2, falls risk, or allergies]

### 📋 Consensus Plan
1. [Action 1]
2. [Action 2]

KEEP IT UNDER 150 WORDS. DO NOT REPEAT TEXT."""
        
        final_output = ""
        # Using a slightly lower max_tokens to encourage brevity, reliance on prompt structure
        for chunk in self.generate_fn(instruction, patient_case, max_tokens=350):
            final_output = chunk
            yield chunk
        
        yield "\n\n---\n✅ **MDT Complete**"
