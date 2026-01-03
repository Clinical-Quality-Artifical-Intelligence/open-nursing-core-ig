"""
Upload FONS Knowledge Base to Hugging Face Dataset
===================================================
This script uploads the large 61MB knowledge file to a HF Dataset,
so it can be loaded at runtime in the Space without hitting size limits.
"""

from datasets import Dataset
from huggingface_hub import HfApi
import json
import os

# Configuration
KNOWLEDGE_FILE = "fons_knowledge_google.jsonl"
DATASET_REPO = "NurseCitizenDeveloper/fons-knowledge-base"

def load_jsonl(filepath):
    """Load JSONL file into list of dicts."""
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except:
                continue
    return data

def main():
    print(f"📂 Loading {KNOWLEDGE_FILE}...")
    records = load_jsonl(KNOWLEDGE_FILE)
    print(f"✅ Loaded {len(records)} records")
    
    # Create HF Dataset
    dataset = Dataset.from_list(records)
    print(f"📊 Dataset: {dataset}")
    
    # Push to Hub
    print(f"⬆️ Uploading to {DATASET_REPO}...")
    dataset.push_to_hub(DATASET_REPO, private=False)
    print(f"✅ Upload complete! View at: https://huggingface.co/datasets/{DATASET_REPO}")

if __name__ == "__main__":
    main()
