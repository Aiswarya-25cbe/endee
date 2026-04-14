import os
from vector_db import VectorDB
from utils import chunk_text
from anthropic import Anthropic


class RAGPipeline:
    def __init__(self):
        self.db = VectorDB()
        self._load_data()

        api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=api_key) if api_key else None

    def _load_data(self):
        with open("data/agriculture_data.txt", "r", encoding="utf-8") as f:
            data = f.read()

        chunks = chunk_text(data)

        for c in chunks:
            self.db.add(c)

    def retrieve(self, query):
        return self.db.search(query)

    def generate(self, query, context):
        if not self.client:
            return None

        prompt = f"""
You are an agriculture expert AI assistant.

Use ONLY the context below:

Context:
{chr(10).join(context)}

Question:
{query}

Give simple farming advice:
"""

        response = self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def run(self, query):
        context = self.retrieve(query)
        answer = self.generate(query, context)

        return {
            "context": context,
            "answer": answer
        }
