"""
Relational RAG Engine: Evidence-Based Retrieval for Nursing Care
================================================================
This module uses FAISS and Sentence Transformers to provide semantic search
over nursing literature, grounding AI responses in evidence.
"""

import json
import os
from typing import List, Dict
import numpy as np

# We'll import these inside the class to allow the Space to start up 
# while dependencies are still installing if needed.
# import faiss
# from sentence_transformers import SentenceTransformer

class RelationalRAG:
    """
    Handles indexing and retrieval of nursing knowledge.
    """
    
    def __init__(self, knowledge_file: str, index_path: str = "faiss_index"):
        self.knowledge_file = knowledge_file
        self.index_path = index_path
        self.model_name = "sentence-transformers/all-MiniLM-L6-v2"
        self.model = None
        self.index = None
        self.documents = []
        
        # Load local data if it exists
        if os.path.exists(knowledge_file):
            self._load_documents()

    def _load_documents(self):
        """Loads JSONL knowledge file."""
        self.documents = []
        with open(self.knowledge_file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    self.documents.append(json.loads(line))
                except:
                    continue
        print(f"✅ Loaded {len(self.documents)} documents from {self.knowledge_file}")

    def _initialize_assets(self):
        """Lazy load heavy ML assets."""
        if self.model is None:
            from sentence_transformers import SentenceTransformer
            print(f"🔄 Loading embedding model: {self.model_name}")
            self.model = SentenceTransformer(self.model_name)
        
        if self.index is None:
            import faiss
            if os.path.exists(self.index_path):
                print(f"📂 Loading existing FAISS index from {self.index_path}")
                self.index = faiss.read_index(self.index_path)
            else:
                self._build_index()

    def _build_index(self):
        """Builds a new FAISS index from documents."""
        import faiss
        print("🧠 Building new knowledge index (this may take a minute)...")
        
        # Extract text content for embedding
        texts = [doc.get("content", doc.get("text", "")) for doc in self.documents]
        
        # Generate embeddings
        embeddings = self.model.encode(texts, show_progress_bar=True)
        
        # Initialize and populate index
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings).astype("float32"))
        
        # Save for future use
        # faiss.write_index(self.index, self.index_path)
        print("✅ Index built successfully!")

    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """Performs semantic search."""
        self._initialize_assets()
        
        # Embed query
        query_embedding = self.model.encode([query]).astype("float32")
        
        # Search index
        distances, indices = self.index.search(query_embedding, top_k)
        
        results = []
        for i in range(len(indices[0])):
            idx = indices[0][i]
            if idx < len(self.documents):
                doc = self.documents[idx]
                results.append({
                    "content": doc.get("content", doc.get("text", "")),
                    "source": doc.get("source", "Nursing Handbook"),
                    "relevance": float(1 / (1 + distances[0][i])) # Pseudo-probability
                })
        
        return results

    def format_context(self, results: List[Dict]) -> str:
        """Formats search results for LLM context injection."""
        context_str = "RELATIONAL EVIDENCE FOUND:\n"
        for i, res in enumerate(results):
            context_str += f"[{i+1}] Source: {res['source']}\nExcerpt: {res['content']}\n\n"
        return context_str

if __name__ == "__main__":
    # Test script
    rag = RelationalRAG("fons_knowledge.jsonl")
    test_query = "How to support a patient with dementia using relational care?"
    results = rag.search(test_query)
    print(rag.format_context(results))
