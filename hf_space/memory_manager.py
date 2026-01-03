"""
Memory Manager: Persistent Person-Centred Patient Profiles
=========================================================
This module manages a persistent 'Memory Bank' of patient preferences,
nicknames, and cultural needs to ensure continuity of relational care.
"""

import json
import os
from typing import Dict, List, Optional

class MemoryManager:
    """
    Handles storage and retrieval of patient-specific memories.
    """
    
    def __init__(self, memory_file: str = "knowledge_base/patient_memory.json"):
        self.memory_file = memory_file
        self.memory = {}
        self.load_memory()

    def load_memory(self):
        """Loads memory from JSON file."""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    self.memory = json.load(f)
                print(f"🧠 Memory Hub: Loaded {len(self.memory)} patient profiles.")
            except Exception as e:
                print(f"⚠️ Memory Hub Error: Could not load {self.memory_file}: {e}")
                self.memory = {}
        else:
            self.memory = {}

    def save_memory(self):
        """Persists memory to JSON file."""
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump(self.memory, f, indent=4)
        except Exception as e:
            print(f"⚠️ Memory Hub Error: Could not save to {self.memory_file}: {e}")

    def upsert_patient(self, name: str, preferences: Dict[str, str]):
        """
        Adds or updates a patient profile.
        Example: upsert_patient("Mrs. Singh", {"preferred_name": "Dadi", "religion": "Sikh"})
        """
        if name not in self.memory:
            self.memory[name] = {"history": []}
        
        # Update preferences
        for key, value in preferences.items():
            self.memory[name][key] = value
        
        self.save_memory()

    def get_patient_context(self, query: str) -> Optional[str]:
        """
        Searches the memory for a name mentioned in the query.
        Returns a formatted string of preferences if found.
        """
        for name, profile in self.memory.items():
            # Basic fuzzy match: is the name in the clinical note?
            if name.lower() in query.lower() or profile.get("preferred_name", "").lower() in query.lower():
                context = f"PERSON-CENTRED MEMORY FOUND for {name}:\n"
                for key, val in profile.items():
                    if key != "history":
                        context += f"- {key.replace('_', ' ').title()}: {val}\n"
                return context
        return None

    def list_patients(self) -> List[str]:
        """Returns a list of all known names in memory."""
        return list(self.memory.keys())

if __name__ == "__main__":
    # Test
    mm = MemoryManager("test_memory.json")
    mm.upsert_patient("Mrs. Singh", {"preferred_name": "Dadi", "empathy_score": "5/5"})
    print(mm.get_patient_context("Patient is Mrs. Singh, she looks tired."))
