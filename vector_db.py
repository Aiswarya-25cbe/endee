import numpy as np
from utils import get_embedding


class VectorDB:
    def __init__(self):
        self.vectors = []
        self.texts = []

    def add(self, text):
        self.vectors.append(get_embedding(text))
        self.texts.append(text)

    def search(self, query, top_k=3):
        q_vec = get_embedding(query)

        results = []

        for i, vec in enumerate(self.vectors):
            score = self.cosine(q_vec, vec)
            results.append((score, self.texts[i]))

        results.sort(reverse=True, key=lambda x: x[0])

        return [text for _, text in results[:top_k]]

    def cosine(self, a, b):
        a = np.array(a)
        b = np.array(b)

        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
