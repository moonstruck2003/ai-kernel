# ✂️ 2 - Data Splitting

## Overview
This module covers **Text Splitters** in LangChain — the second step in the **RAG pipeline**. After loading raw documents, large texts must be broken into smaller, semantically meaningful chunks before being embedded and stored in a vector database. This module demonstrates 4 different splitting strategies.

---

## 📂 Files
| File | Description |
|------|-------------|
| `2-TextSplitter.ipynb` | PyPDFLoader + RecursiveCharacterTextSplitter demo |
| `3.3-RecuriveCharactertextsplitter.ipynb` | Deep dive into RecursiveCharacterTextSplitter |
| `3.4-CharacterTextsplitter.ipynb` | CharacterTextSplitter demo |
| `3.5-HTMLtextsplitter.ipynb` | HTMLHeaderTextSplitter demo |
| `3.6-RecursiveJsonSplitter.ipynb` | RecursiveJsonSplitter with live API data |
| `attention.pdf` | "Attention Is All You Need" paper — main test document |
| `speech.txt` | Sample speech text for loader demos |

---

## 📦 Libraries Covered

### `langchain_community`
> Community document loaders for ingesting data.

#### `PyPDFLoader`
- **Purpose**: Load PDF pages as `Document` objects before splitting.
- **Import**: `from langchain_community.document_loaders import PyPDFLoader`

#### `TextLoader`
- **Purpose**: Load plain text files as `Document` objects.
- **Import**: `from langchain_community.document_loaders import TextLoader`

---

### `langchain_text_splitters`
> Official library for splitting large text documents into chunks.

---

#### `RecursiveCharacterTextSplitter` ⭐ (Recommended)
- **Purpose**: The **recommended general-purpose splitter**. Tries to split on a hierarchy of separators (`\n\n`, `\n`, ` `, `""`) in order, until chunks are small enough. Keeps paragraphs, sentences, and words together as long as possible.
- **Import**: `from langchain_text_splitters import RecursiveCharacterTextSplitter`

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `chunk_size` | Max number of characters per chunk | `chunk_size=500` |
| `chunk_overlap` | Number of characters to overlap between consecutive chunks (for context continuity) | `chunk_overlap=50` |

| Method | Purpose | Parameters |
|--------|---------|------------|
| `split_documents(docs)` | Splits a list of `Document` objects | `docs` — list of `Document` |
| `split_text(text)` | Splits a raw string | `text` — raw string |
| `create_documents(texts)` | Creates `Document` objects from raw strings | `texts` — list of strings |

**Example:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
final_documents = text_splitter.split_documents(docs)
```

---

#### `CharacterTextSplitter`
- **Purpose**: Simpler splitter that splits on a **single specific character** (default: `\n\n`). Less context-aware than Recursive variant.
- **Import**: `from langchain_text_splitters import CharacterTextSplitter`

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `separator` | The character to split on | `separator="\n"` |
| `chunk_size` | Max characters per chunk | `chunk_size=200` |
| `chunk_overlap` | Overlap between chunks | `chunk_overlap=20` |

---

#### `HTMLHeaderTextSplitter`
- **Purpose**: Splits HTML content **semantically by header tags** (h1, h2, h3, etc.). Preserves document structure and adds header information as metadata.
- **Import**: `from langchain_text_splitters import HTMLHeaderTextSplitter`

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `headers_to_split_on` | List of `(tag, label)` tuples defining which headers to split at | `[("h1","Header 1"), ("h2","Header 2")]` |

| Method | Purpose |
|--------|---------|
| `split_text(html_string)` | Splits an HTML string by headers |
| `split_text_from_url(url)` | Fetches a web page and splits by headers |

**Example:**
```python
from langchain_text_splitters import HTMLHeaderTextSplitter

headers_to_split_on = [("h1", "Header 1"), ("h2", "Header 2")]
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on)
splits = html_splitter.split_text_from_url("https://plato.stanford.edu/entries/goedel/")
```

---

#### `RecursiveJsonSplitter`
- **Purpose**: Splits **JSON data** (nested dicts/lists) into smaller JSON chunks while preserving structure. Useful when working with API responses.
- **Import**: `from langchain_text_splitters import RecursiveJsonSplitter`

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `max_chunk_size` | Maximum size of each JSON chunk | `max_chunk_size=300` |

| Method | Purpose |
|--------|---------|
| `split_json(json_data)` | Splits JSON into a list of smaller JSON dicts |
| `create_documents(texts=[json_data])` | Creates `Document` objects from JSON |
| `split_text(json_data)` | Returns JSON chunks as list of strings |

**Example:**
```python
import requests
from langchain_text_splitters import RecursiveJsonSplitter

json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()
json_splitter = RecursiveJsonSplitter(max_chunk_size=300)
json_chunks = json_splitter.split_json(json_data)
```

---

## 🔑 Key Concepts

### Why Overlap Matters (`chunk_overlap`)
When splitting text, you add an overlap between adjacent chunks to ensure **context is not lost** at chunk boundaries. Without overlap, a sentence split across two chunks loses its meaning when embedded separately.

### Splitter Comparison

| Splitter | Best For | Split Strategy |
|----------|----------|---------------|
| `RecursiveCharacterTextSplitter` | General text (PDF, TXT) | Hierarchical separators (`\n\n` → `\n` → ` ` → `""`) |
| `CharacterTextSplitter` | Simple, uniform text | Single character separator |
| `HTMLHeaderTextSplitter` | Web pages, HTML docs | HTML semantic header tags |
| `RecursiveJsonSplitter` | API responses, JSON data | JSON structure traversal |

---

## 🗺️ Role in the RAG Pipeline

```
[Documents] → [Text Splitters] → [Chunks] → [Embeddings] → [Vector Store]
                   ↑ This module covers this step
```
