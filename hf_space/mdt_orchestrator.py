"""
MDT Orchestrator: Virtual Multi-Disciplinary Team for Nursing Care
===================================================================
Simplified version that produces a single concise care plan summary.
"""

from rag_engine import RelationalRAG
from memory_manager import MemoryManager

class MDTOrchestrator:
    """
    Simplified MDT that produces a single concise output, grounded in Evidence and Memory.
    """

    def __init__(self, generate_fn):
        self.generate_fn = generate_fn
        # Lazy load these to avoid circular import issues if possible, 
        # but standard init is fine if app.py handles dependencies well.
        self.rag = RelationalRAG() 
        self.memory = MemoryManager()

    def run_discussion(self, patient_case: str) -> Generator[str, None, None]:
        """
        Runs a simplified MDT and yields a concise care plan.
        """
        # 1. Retrieve Context
        yield "🔍 *Checking Evidence & Memory...*\n\n"
        
        # Search RAG
        search_results = self.rag.search(patient_case)
        evidence_context = self.rag.format_context(search_results)
        
        # Search Memory (Dadi's Mirror)
        memory_context = self.memory.get_patient_context(patient_case)
        mem_str = f"PATIENT MEMORY:\n{memory_context}" if memory_context else ""

        yield "🏥 *Synthesizing Virtual MDT Plan...*\n\n"
        
        # 2. Single-Shot Prompt with Context
        instruction = f"""You are leading a Virtual MDT. Analyze this patient case using the EVIDENCE and MEMORY provided.
        
{evidence_context}

{mem_str}

Provide a CONCISE care plan based on the above.

FORMAT YOUR RESPONSE EXACTLY LIKE THIS:
## MDT Summary

**Patient:** [1 sentence summary]

### Key Findings:
- 🩹 Skin/Tissue: [1 bullet point]
- 💚 Relational: [1 bullet point using Memory/Evidence]
- 🛡️ Safety: [PASS/FAIL for each gate]

### Recommended Actions:
1. [Action 1]
2. [Action 2]
3. [Action 3]

DO NOT REPEAT YOURSELF. BE EXTREMELY CONCISE. MAX 200 WORDS TOTAL."""
        
        final_output = ""
        for chunk in self.generate_fn(instruction, patient_case, max_tokens=200):
            final_output = chunk
            yield chunk
        
        yield "\n\n---\n✅ **MDT Complete**"
