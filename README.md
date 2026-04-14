# 🌾 AI Smart Farming Assistant

### RAG-Based Crop Advisory System

---

## 📌 Overview

This project is an **AI-powered farming assistant** that provides simple and useful agricultural advice using a **Retrieval-Augmented Generation (RAG)** approach.

Instead of giving general answers, the system first **retrieves relevant farming information** and then generates a response based on that context.

This helps in giving **more accurate and meaningful suggestions** for farming-related queries.

---

## 🎯 Objective

To build a practical AI system that can:

* Understand farming-related questions
* Retrieve relevant agricultural data
* Provide clear and simple advice
* Demonstrate RAG-based architecture

---

## 🧠 Key Concepts

* Vector Embeddings (Sentence Transformers)
* Semantic Search
* Cosine Similarity
* Retrieval-Augmented Generation (RAG)
* Context-based response generation

---

## ⚙️ Tech Stack

* Python
* Sentence Transformers (`all-MiniLM-L6-v2`)
* NumPy
* Anthropic (Claude API)
* python-dotenv
* Streamlit (optional)

---

## 🏗️ System Architecture

* Load agriculture dataset
* Split data into small chunks
* Convert text into vector embeddings
* Store embeddings in memory
* Convert user query into embedding
* Find similar data using cosine similarity
* Send context to AI model
* Generate final answer

---

## 🔥 Features

* 🌱 Smart farming assistant
* 🔍 Semantic search (understands meaning, not just keywords)
* 🤖 AI-generated responses
* 📊 Context-based results
* ⚡ Simple and lightweight system

---

## 🧪 Example Queries

* "How to control pests?"
* "Best soil for tomato?"
* "How to improve soil fertility?"
* "Which fertilizer is good for crops?"

---

## 📊 Sample Output

**Retrieved Context:**

* Aphids are pests → use neem oil
* Soil fertility improves with compost

**AI Answer:**
Use neem oil to control pests like aphids. Add compost or organic manure to improve soil fertility.

---

## 🚀 How to Run

### 1️⃣ Clone Repository

```
git clone <your-repo-link>
cd ai-smart-farming-assistant
```

### 2️⃣ Install Requirements

```
pip install -r requirements.txt
```

### 3️⃣ Setup Environment

Create `.env` file:

```
ANTHROPIC_API_KEY=your_api_key_here
```

### 4️⃣ Run

```
python rag_pipeline.py
```

---

## 📂 Dataset

Contains basic agriculture knowledge such as:

* Crop diseases
* Soil nutrients
* Fertilizer usage
* Irrigation methods
* Pest control

---

## ⚠️ Note

This project uses a **local in-memory vector database** instead of external tools.

But it still follows the same steps used in real-world systems:

* Embedding
* Storage
* Retrieval
* AI generation

---

## 📈 Future Improvements

* Add Streamlit UI
* Support more crop data
* Add multiple languages
* Use real vector databases (FAISS, Pinecone)
* Build mobile app

---

## 🏁 Conclusion

This project shows how AI can help in **smart farming** by providing useful suggestions based on data.

It demonstrates:

* RAG pipeline
* Semantic search
* Real-world AI application

---

## 👨‍💻 Author

AI Project – Smart Farming Assistant 🌾

---

⭐ Give a star if you like this project!
