# 🦜🔗 22 - LangChain

## Overview
This workspace covers the **LangChain** framework for building **LLM-powered applications**, with a strong focus on the **RAG (Retrieval-Augmented Generation)** pipeline. The course is structured as a series of hands-on Jupyter notebooks organized by topic.

---

## 📂 Folder Structure

```
22 - LangChain/
├── README.md                    ← You are here
├── requirement.txt              ← All project dependencies
├── .env                         ← API keys (OPENAI_API_KEY, HF_TOKEN)
├── .gitignore                   ← Ignores venv/ and .env
├── venv/                        ← Project virtual environment
│
├── 1 - LangChain/               ← Core pipeline: Ingestion + Splitting
│   ├── README.md
│   ├── GettingStarted.ipynb
│   ├── 1-Data Ingestion/
│   │   └── 1-DataIngestion.ipynb
│   └── 2-Data Splitting/
│       ├── 2-TextSplitter.ipynb
│       ├── 3.3-RecuriveCharactertextsplitter.ipynb
│       ├── 3.4-CharacterTextsplitter.ipynb
│       ├── 3.5-HTMLtextsplitter.ipynb
│       └── 3.6-RecursiveJsonSplitter.ipynb
│
└── 4-Embeddings/                ← Embedding models + Vector Store
    ├── README.md
    ├── 4.1-embedding.ipynb
    ├── 4.2-ollamaemnedding.ipynb
    └── 4.3-huggingface.ipynb
```

---

## 🗺️ RAG Pipeline — What You've Covered

```
Step 1          Step 2              Step 3              Step 4
[Raw Files] → [Document Loaders] → [Text Splitters] → [Embeddings] → [Vector Store] → [Retrieval]
               TextLoader            RecursiveChar      OpenAI          ChromaDB        similarity_search
               PyPDFLoader           CharacterText      Ollama
                                     HTMLHeader         HuggingFace
                                     RecursiveJson
```

---

## 📦 All Libraries Used

| Library | Version | Purpose |
|---------|---------|---------|
| `langchain` | latest | Core framework |
| `langchain-community` | latest | Document loaders, vector store integrations |
| `langchain-text-splitters` | latest | Text splitting utilities |
| `langchain-openai` | latest | OpenAI embeddings & LLMs |
| `langchain-ollama` | latest | Local Ollama embeddings & LLMs |
| `langchain-huggingface` | latest | HuggingFace embeddings |
| `langchain-core` | latest | Base Document types and interfaces |
| `ollama` | latest | Local Ollama model runtime client |
| `chromadb` | latest | In-memory + persistent vector database |
| `sentence_transformers` | latest | HuggingFace sentence embedding backend |
| `python-dotenv` | latest | Load API keys from `.env` file |
| `pypdf` | latest | PDF parsing for PyPDFLoader |
| `bs4` | latest | HTML parsing (BeautifulSoup) |
| `arxiv` | <2.0.0 | Arxiv paper loader |
| `pymupdf` | latest | Alternative PDF parser |
| `ipykernel` | latest | Jupyter kernel support |

---

## 📖 Module-by-Module Summary

### [1 - LangChain](./1%20-%20LangChain/README.md)
Covers the foundational first two stages of the RAG pipeline.

| Sub-module | Topic | Key Classes |
|------------|-------|-------------|
| [1-Data Ingestion](./1%20-%20LangChain/1-Data%20Ingestion/README.md) | Loading files into Document objects | `TextLoader`, `PyPDFLoader` |
| [2-Data Splitting](./1%20-%20LangChain/2-Data%20Splitting/README.md) | Chunking documents for embedding | `RecursiveCharacterTextSplitter`, `CharacterTextSplitter`, `HTMLHeaderTextSplitter`, `RecursiveJsonSplitter` |

---

### [4-Embeddings](./4-Embeddings/README.md)
Covers converting text chunks into semantic vectors and storing them in a vector database.

| Notebook | Embedding Provider | Vector Store | Key Concepts |
|----------|--------------------|--------------|--------------|
| `4.1-embedding.ipynb` | OpenAI | ChromaDB | `embed_query`, `embed_documents`, `similarity_search`, custom `dimensions` |
| `4.2-ollamaemnedding.ipynb` | Ollama (local) | — | `nomic-embed-text`, local inference |
| `4.3-huggingface.ipynb` | HuggingFace (local) | — | `all-MiniLM-L6-v2`, `HF_TOKEN`, `sentence_transformers` |

---

## ⚙️ Setup & Environment

### Virtual Environment
This project uses a **Conda prefix-based environment** at:
```
22 - LangChain/venv/
```

**Activate in PowerShell:**
```powershell
.\venv\Scripts\activate
```

**Activate in Git Bash:**
```bash
source venv/Scripts/activate
```

### Install Dependencies
```bash
# Recommended (always targets the correct environment)
.\venv\python.exe -m pip install -r requirement.txt
```

### Environment Variables (`.env`)
```env
OPENAI_API_KEY=your_openai_key_here
HF_TOKEN=your_huggingface_token_here
```

---

## 🔑 Key Concept: Why RAG?

RAG (Retrieval-Augmented Generation) overcomes LLM limitations:
- LLMs have a **knowledge cutoff** — they don't know recent events.
- LLMs can **hallucinate** facts.
- RAG **grounds** the LLM with real, retrieved documents before answering.

**Flow**: User Question → Embed Question → Search Vector DB → Retrieve Top Chunks → Feed to LLM → Answer
