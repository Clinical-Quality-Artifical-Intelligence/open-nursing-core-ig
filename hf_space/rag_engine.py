"""
Relational RAG Engine: Evidence-Based Retrieval for Nursing Care
================================================================
Loads knowledge from a Hugging Face Dataset for efficient large-scale retrieval.
"""

import os
from typing import List, Dict
import numpy as np

class RelationalRAG:
    """
    Handles indexing and retrieval of nursing knowledge from HF Dataset.
    """
    
    def __init__(self, dataset_repo: str = "NurseCitizenDeveloper/fons-knowledge-base"):
        self.dataset_repo = dataset_repo
        self.model_name = "sentence-transformers/all-MiniLM-L6-v2"
        self.model = None
        self.index = None
        self.documents = []
        self.initialized = False

    def _initialize_assets(self):
        """Lazy load heavy ML assets and dataset."""
        if self.initialized:
            return
            
        try:
            from sentence_transformers import SentenceTransformer
            from datasets import load_dataset
            import faiss
            
            print(f"🔄 Loading embedding model: {self.model_name}")
            self.model = SentenceTransformer(self.model_name)
            
            print(f"📂 Loading dataset from: {self.dataset_repo}")
            dataset = load_dataset(self.dataset_repo, split="train")
            
            # Extract content from dataset
            self.documents = []
            for row in dataset:
                # Handle different possible column names
                content = row.get("content") or row.get("text") or str(row)
                self.documents.append({
                    "content": content,
                    "source": row.get("source", "FONS Knowledge Base")
                })
            
            print(f"✅ Loaded {len(self.documents)} documents")
            
            # Build index
            if self.documents:
                print("🧠 Building search index...")
                texts = [doc["content"] for doc in self.documents]
                embeddings = self.model.encode(texts[:1000], show_progress_bar=True)  # Limit for speed
                
                dimension = embeddings.shape[1]
                self.index = faiss.IndexFlatL2(dimension)
                self.index.add(np.array(embeddings).astype("float32"))
                print("✅ Index built successfully!")
            
            self.initialized = True
            
        except Exception as e:
            print(f"⚠️ RAG initialization failed: {e}")
            self.initialized = True  # Don't retry on failure

    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """Performs semantic search."""
        self._initialize_assets()
        
        if not self.index or not self.documents:
            return [{"content": "Knowledge base not available.", "source": "System", "relevance": 0}]
        
        query_embedding = self.model.encode([query]).astype("float32")
        distances, indices = self.index.search(query_embedding, top_k)
        
        results = []
        for i in range(len(indices[0])):
            idx = indices[0][i]
            if idx < len(self.documents):
                doc = self.documents[idx]
                results.append({
                    "content": doc["content"][:500],  # Truncate for context window
                    "source": doc["source"],
                    "relevance": float(1 / (1 + distances[0][i]))
                })
        
        return results

    def format_context(self, results: List[Dict]) -> str:
        """Formats search results for LLM context injection."""
        if not results:
            return ""
        context_str = "RELATIONAL EVIDENCE FOUND:\n"
        for i, res in enumerate(results):
            context_str += f"[{i+1}] {res['content']}\n\n"
        return context_str
