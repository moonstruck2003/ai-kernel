# 🧠 1 - LangChain Module

## Overview
This is the **parent folder** for all core LangChain concepts. It covers the first two foundational stages of the **RAG (Retrieval-Augmented Generation)** pipeline:
1. **Data Ingestion** — Loading documents from various sources
2. **Data Splitting** — Breaking documents into chunks for embedding

---

## 📂 Structure

```
1 - LangChain/
├── GettingStarted.ipynb         # Introduction to LangChain and LangServe
├── 1-Data Ingestion/            # Document loading from text and PDF
│   ├── README.md
│   ├── 1-DataIngestion.ipynb
│   ├── speech.txt
│   └── attention.pdf
└── 2-Data Splitting/            # Text splitting strategies
    ├── README.md
    ├── 2-TextSplitter.ipynb
    ├── 3.3-RecuriveCharactertextsplitter.ipynb
    ├── 3.4-CharacterTextsplitter.ipynb
    ├── 3.5-HTMLtextsplitter.ipynb
    ├── 3.6-RecursiveJsonSplitter.ipynb
    ├── speech.txt
    └── attention.pdf
```

---

## 📋 Module Summaries

### 📘 GettingStarted.ipynb
An introductory notebook covering the basics of:
- Setting up **LangChain**
- Setting up **LangServe** (LangChain's API serving framework)

---

### 📁 1-Data Ingestion
Covers LangChain **Document Loaders** — the entry point of the RAG pipeline.

| Loader | Source Format | Key Method |
|--------|---------------|------------|
| `TextLoader` | `.txt` files | `.load()` |
| `PyPDFLoader` | `.pdf` files | `.load()` (page-by-page) |

→ **See**: [1-Data Ingestion/README.md](./1-Data%20Ingestion/README.md)

---

### 📁 2-Data Splitting
Covers LangChain **Text Splitters** — chunking documents for embedding.

| Splitter | Best For |
|----------|----------|
| `RecursiveCharacterTextSplitter` | General text (⭐ Recommended) |
| `CharacterTextSplitter` | Simple text with consistent formatting |
| `HTMLHeaderTextSplitter` | Web pages and HTML documents |
| `RecursiveJsonSplitter` | JSON API responses |

→ **See**: [2-Data Splitting/README.md](./2-Data%20Splitting/README.md)

---

## 🗺️ RAG Pipeline Position

```
[Raw Files]
    ↓
[1-Data Ingestion] → TextLoader / PyPDFLoader → Documents
    ↓
[2-Data Splitting] → RecursiveCharacterTextSplitter / etc. → Chunks
    ↓
[4-Embeddings] → OpenAI / Ollama / HuggingFace → Vectors
    ↓
[Vector Store] → ChromaDB / FAISS → Similarity Search
```

---

## 📦 Libraries Used

| Library | Purpose |
|---------|---------|
| `langchain_community` | Document loaders (TextLoader, PyPDFLoader) |
| `langchain_text_splitters` | Text splitting utilities |
| `langchain_core` | Core Document object types |
| `pypdf` | PDF parsing backend for PyPDFLoader |
