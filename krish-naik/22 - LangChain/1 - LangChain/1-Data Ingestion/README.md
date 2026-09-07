# 📥 1 - Data Ingestion

## Overview
This module covers **Document Loaders** in LangChain — the first step in the **RAG (Retrieval-Augmented Generation)** pipeline. You learn how to ingest text from various sources (plain text files, PDFs) into LangChain's `Document` object format, which is the standard data unit for all downstream processing.

---

## 📂 Files
| File | Description |
|------|-------------|
| `1-DataIngestion.ipynb` | Main notebook covering TextLoader and PyPDFLoader |
| `speech.txt` | Sample plain-text file used for TextLoader demo |
| `attention.pdf` | "Attention Is All You Need" paper — used for PyPDFLoader demo |

---

## 📦 Libraries Covered

### `langchain_community`
> Community-maintained integrations for LangChain document loaders.

#### `TextLoader`
- **Purpose**: Loads plain `.txt` files into LangChain `Document` objects.
- **Import**: `from langchain_community.document_loaders import TextLoader`

| Function | Purpose | Key Parameters |
|----------|---------|----------------|
| `TextLoader(file_path)` | Creates the loader object | `file_path` — path to the `.txt` file |
| `.load()` | Reads the file and returns a list of `Document` objects | — |

**Example:**
```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader('speech.txt')
documents = loader.load()
# Returns: [Document(metadata={'source': 'speech.txt'}, page_content='...')]
```

---

#### `PyPDFLoader`
- **Purpose**: Loads PDF files page-by-page into LangChain `Document` objects. Each page becomes a separate `Document`.
- **Import**: `from langchain_community.document_loaders import PyPDFLoader`

| Function | Purpose | Key Parameters |
|----------|---------|----------------|
| `PyPDFLoader(file_path)` | Creates the PDF loader | `file_path` — path to the `.pdf` file |
| `.load()` | Parses PDF and returns one `Document` per page | — |

**Example:**
```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('attention.pdf')
docs = loader.load()
# Returns: [Document(metadata={'source': 'attention.pdf', 'page': 0, 'total_pages': 15, ...}, page_content='...'), ...]
```

---

## 🔑 Key Concepts

### `Document` Object
Every loader returns a list of `Document` objects from `langchain_core.documents.base`.

| Field | Description |
|-------|-------------|
| `page_content` | The actual text content extracted from the file |
| `metadata` | Dictionary with source info: `source`, `page`, `total_pages`, author, etc. |

---

## 🗺️ Role in the RAG Pipeline

```
[Raw Files] → [Document Loaders] → [Documents] → [Splitters] → [Embeddings] → [Vector Store]
     ↑ This module covers this step
```

---

## 📚 Source Data Used
- **speech.txt** — A synthetic data engineer conference speech
- **attention.pdf** — "Attention Is All You Need" (Vaswani et al., 2017) — the original Transformer paper
