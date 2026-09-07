# 🔢 4 - Embeddings

## Overview
This module covers **Text Embeddings** in LangChain — the third step in the **RAG (Retrieval-Augmented Generation)** pipeline. Embeddings convert text into high-dimensional numerical vectors that capture semantic meaning, enabling similarity-based retrieval from a vector database.

Three embedding providers are covered:
1. **OpenAI Embeddings** (`text-embedding-3-large`)
2. **Ollama Embeddings** (local, offline models)
3. **HuggingFace Embeddings** (`all-MiniLM-L6-v2`, local)

---

## 📂 Files

| File | Description |
|------|-------------|
| `4.1-embedding.ipynb` | OpenAI embeddings + ChromaDB vector store + similarity search |
| `4.2-ollamaemnedding.ipynb` | Local Ollama embedding models |
| `4.3-huggingface.ipynb` | HuggingFace sentence transformer embeddings |
| `speech.txt` | Sample text file used for embedding & vector store demo |

---

## 📦 Libraries Covered

---

### 4.1 — `langchain_openai`
> LangChain's official OpenAI integration.

#### `OpenAIEmbeddings`
- **Purpose**: Converts text into dense vector embeddings using OpenAI's embedding API (requires `OPENAI_API_KEY`).
- **Import**: `from langchain_openai import OpenAIEmbeddings`

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `model` | Which OpenAI embedding model to use | `"text-embedding-3-large"` |
| `dimensions` | Output vector dimension (optional, for compression) | `dimensions=1024` |

| Method | Purpose | Parameters |
|--------|---------|------------|
| `embed_query(text)` | Embeds a **single string** (for query embedding during retrieval) | `text` — string to embed |
| `embed_documents(texts)` | Embeds a **list of strings** (for indexing documents) | `texts` — list of strings |

**Example:**
```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
# Full 3072-dim vector
query_result = embeddings.embed_query("This is a tutorial on OPENAI embedding")
len(query_result)  # 3072

# Compressed 1024-dim vector
embeddings_1024 = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)
query_result = embeddings_1024.embed_query("This is a tutorial on OPENAI embedding")
len(query_result)  # 1024
```

---

### 4.1 — `langchain_community.vectorstores` — `Chroma`
> Integration with ChromaDB vector store.

#### `Chroma`
- **Purpose**: Stores embedded document vectors and enables **semantic similarity search**. This is where the RAG retrieval magic happens!
- **Import**: `from langchain_community.vectorstores import Chroma`

| Method | Purpose | Key Parameters |
|--------|---------|----------------|
| `Chroma.from_documents(documents, embedding)` | Creates a Chroma DB from documents and an embedding model | `documents` — list of `Document`, `embedding` — embedding model instance |
| `.similarity_search(query)` | Retrieves the most semantically similar documents to a query string | `query` — the question/search text |

**Example:**
```python
from langchain_community.vectorstores import Chroma

db = Chroma.from_documents(final_documents, embeddings_1024)
results = db.similarity_search("It will be all the easier for us to conduct ourselves as belligerents")
print(results)
```

---

### 4.2 — `langchain_ollama`
> LangChain integration for local Ollama models.

#### `OllamaEmbeddings`
- **Purpose**: Generates text embeddings **locally** using Ollama — no API key required. Must use a dedicated embedding model (not a chat model).
- **Import**: `from langchain_ollama import OllamaEmbeddings`

> ⚠️ **Important**: Use a dedicated embedding model like `nomic-embed-text`, NOT a generative model like `gemma3`. Generative models return a `ResponseError: This server does not support embeddings`.

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `model` | The Ollama embedding model to use | `"nomic-embed-text"` |

| Method | Purpose | Parameters |
|--------|---------|------------|
| `embed_documents(texts)` | Embeds a list of documents | `texts` — list of strings |
| `embed_query(text)` | Embeds a single query string | `text` — string |

**Example:**
```python
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Embed multiple documents
r1 = embeddings.embed_documents([
    "Alif is the first character of the Arabic alphabet",
    "Baa is the second character of the Arabic alphabet"
])
len(r1[0])  # 768-dimensional vector

# Embed a single query
q = embeddings.embed_query("What is the second character of Arabic?")
```

---

### 4.3 — `langchain_huggingface`
> LangChain's HuggingFace integration for local embedding models.

#### `HuggingFaceEmbeddings`
- **Purpose**: Generates embeddings using **sentence-transformer models from HuggingFace** — fully local, no API key needed. Powered by the `sentence_transformers` library under the hood.
- **Import**: `from langchain_huggingface import HuggingFaceEmbeddings`
- **Requires**: `HF_TOKEN` environment variable (for downloading gated models)

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `model_name` | HuggingFace model name or path | `"all-MiniLM-L6-v2"` |

| Method | Purpose | Parameters |
|--------|---------|------------|
| `embed_query(text)` | Embeds a single query string | `text` — string to embed |
| `embed_documents(texts)` | Embeds a list of text strings | `texts` — list of strings |

**Example:**
```python
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
os.environ['HF_TOKEN'] = os.getenv("HF_TOKEN")

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

query_result = embeddings.embed_query("this is a test document")
len(query_result)  # 384

doc_result = embeddings.embed_documents(["this is a test document", "This is not a test document."])
```

---

### Supporting Libraries

#### `python-dotenv`
- **Purpose**: Loads API keys from `.env` file securely into environment variables.
- **Key function**: `load_dotenv()` — scans for `.env` file and loads all key-value pairs into `os.environ`.

#### `sentence_transformers`
- **Purpose**: Backend library used by `HuggingFaceEmbeddings` for running sentence transformer models locally.

---

## 🔑 Key Concepts

### What is an Embedding?
An embedding converts text into a **list of floating-point numbers** (a vector). Semantically similar texts produce vectors that are **close together** in vector space, enabling similarity search.

### `embed_query` vs `embed_documents`
| Method | Used For | Optimization |
|--------|----------|-------------|
| `embed_query` | A single search/question string | Optimized for query representation |
| `embed_documents` | Multiple documents to store/index | Optimized for document representation |

### Embedding Provider Comparison

| Provider | Requires API Key | Model Example | Dimensions | Local? |
|----------|-----------------|---------------|------------|--------|
| OpenAI | ✅ Yes | `text-embedding-3-large` | 3072 (or custom) | ❌ No |
| Ollama | ❌ No | `nomic-embed-text` | 768 | ✅ Yes |
| HuggingFace | Optional (HF_TOKEN) | `all-MiniLM-L6-v2` | 384 | ✅ Yes |

---

## 🗺️ Full RAG Pipeline (End-to-End in 4.1)

```python
# 1. Load
from langchain_community.document_loaders import TextLoader
loader = TextLoader('speech.txt')
docs = loader.load()

# 2. Split
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
final_documents = text_splitter.split_documents(docs)

# 3. Embed + Store
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)
db = Chroma.from_documents(final_documents, embeddings)

# 4. Retrieve
results = db.similarity_search("your question here")
```

---

## 🗺️ Role in the RAG Pipeline

```
[Chunks] → [Embedding Models] → [Vectors] → [ChromaDB] → [Similarity Search]
                ↑ This module covers this step
```
