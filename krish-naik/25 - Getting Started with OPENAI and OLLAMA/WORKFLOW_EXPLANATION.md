# End-to-End RAG Application Workflow & Explanation
> **Notebook Reference:** [`1.1.2-Simpleapp.ipynb`](file:///c:/Users/PC/Desktop/ai-kernel/krish-naik/25%20-%20Getting%20Started%20with%20OPENAI%20and%20OLLAMA/1.1.2-Simpleapp.ipynb)  
> **Tech Stack:** LangChain, FAISS Vector DB, Ollama Embeddings (`embeddinggemma:300m`), Groq LLM (`qwen/qwen3.8-27b`)

---

## 1. Executive Summary

This application implements a **Retrieval-Augmented Generation (RAG)** pipeline using LangChain. The core purpose of RAG is to enrich Large Language Models (LLMs) with custom, external context (e.g., website data, proprietary documents) so that LLMs can answer domain-specific questions accurately without hallucinating.

The pipeline ingests web content, splits it into chunks, stores vector embeddings in a FAISS vector database, retrieves relevant text based on a user's question, and uses a **Document Chain** and **Retrieval Chain** to generate an context-grounded answer.

---

## 2. End-to-End Visual Workflow Architecture

```mermaid
flowchart TD
    subgraph Data_Ingestion_and_Indexing["1. Data Ingestion & Indexing Pipeline"]
        A["Web Page URL\n(nsac.basis.org.bd)"] -->|WebBaseLoader| B["Raw LangChain Document"]
        B -->|RecursiveCharacterTextSplitter\n(chunk_size=1000, overlap=200)| C["Document Chunks"]
        C -->|OllamaEmbeddings\n(embeddinggemma:300m)| D["Vector Embeddings"]
        D -->|Index Chunks| E[("FAISS Vector Store DB")]
    end

    subgraph Query_Processing_and_RAG["2. RAG Execution Pipeline"]
        F["User Input Question\n('What are 2026 Challenges?')"] -->|Invoke| G["Retrieval Chain\n(create_retrieval_chain)"]
        
        subgraph Retrieval_Stage["Retrieval Sub-system"]
            G -->|1. Query| H["VectorStoreRetriever\n(vectorstoredb.as_retriever)"]
            H -->|2. Similarity Search| E
            E -->|3. Return Top Chunks| I["Retrieved Context Documents"]
        end
        
        subgraph Document_Processing_Stage["Document Chain Sub-system"]
            I -->|4. Pass Context Docs| J["Document Chain\n(create_stuff_documents_chain)"]
            F -->|Pass Question| J
            J -->|5. Inject into Prompt Template| K["ChatPromptTemplate\n({context} + {input})"]
            K -->|6. Formatted Prompt| L["Groq LLM\n(qwen/qwen3.8-27b)"]
            L -->|7. Generate Response| M["StrOutputParser"]
        end

        M -->|8. Final Output| N["Response Payload\n{'input', 'context', 'answer'}"]
    end

    style Data_Ingestion_and_Indexing fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#fff
    style Query_Processing_and_RAG fill:#0f172a,stroke:#10b981,stroke-width:2px,color:#fff
    style Retrieval_Stage fill:#334155,stroke:#f59e0b,color:#fff
    style Document_Processing_Stage fill:#1e293b,stroke:#8b5cf6,color:#fff
```

---

## 3. Detailed Step-by-Step Breakdown

### Step 1: Environment & Tracing Setup
- **dotenv**: Loads API keys (`GROQ_API_KEY`, `LANGCHAIN_API_KEY`) from `.env`.
- **LangChain Tracing**: Configures `LANGCHAIN_TRACING_V2="true"` for full visibility into prompt variables, retrieved documents, and token usage via LangSmith.

### Step 2: Data Ingestion (`WebBaseLoader`)
- **Action**: Uses `WebBaseLoader` to scrape text content from a target URL (`https://nsac.basis.org.bd/about-nasa`).
- **Output**: A list of `Document` objects containing raw text in `page_content` and metadata (URL source, page title, description).

### Step 3: Text Chunking (`RecursiveCharacterTextSplitter`)
- **Action**: Large web documents exceed LLM context windows and reduce retrieval precision. The text is split into chunks of `1000` characters with an overlap of `200` characters.
- **Why Overlap?**: Overlap ensures important semantic context is not severed at chunk boundaries.

### Step 4: Vector Embeddings & Storage (`OllamaEmbeddings` + `FAISS`)
- **Embedding Model**: `OllamaEmbeddings(model="embeddinggemma:300m")` converts text chunks into high-dimensional numerical vectors.
- **Vector Database**: `FAISS.from_documents(documents, embeddings)` indexes vector representations for ultra-fast cosine similarity / distance searching.

---

## 4. Focus Deep Dive: Document Chain vs. Retrieval Chain

The core logic of LangChain RAG relies on two distinct chain abstractions working in harmony:

```
                  +-------------------------------------------------------------+
                  |                       Retrieval Chain                       |
                  |                                                             |
User Question --->|  +-------------------+        +--------------------------+  |---> Final Answer
                  |  |  Vector Store     |=======>|      Document Chain      |  |     + Context
                  |  |  Retriever        | Context| (Combine Docs + Prompt   |  |
                  |  +-------------------+ Docs   |        + LLM)            |  |
                  |                               +--------------------------+  |
                  +-------------------------------------------------------------+
```

### A. The Document Chain (`create_stuff_documents_chain`)

#### **Role & Functionality**
The **Document Chain** is responsible for taking a list of documents, formatting them into a single string (a process known as "stuffing"), inserting them into a prompt template's `{context}` variable, and passing the complete prompt to the LLM.

#### **Mechanism ("Stuffing")**
1. Receives a list of `Document` objects: `[Document(page_content="..."), Document(page_content="...")]`.
2. Concatenates all `page_content` blocks separated by newlines.
3. Injects the combined text string into `{context}` inside `ChatPromptTemplate`.
4. Sends the formatted prompt to `ChatGroq(model="qwen/qwen3.8-27b")`.

#### **Code snippet from notebook:**
```python
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# 1. Define Prompt Template with {context} slot
prompt = ChatPromptTemplate.from_template("""
Answer the following question based on the provided context:
<context>
{context}
</context>
""")

# 2. Create the Document Chain
document_chain = create_stuff_documents_chain(llm, prompt)

# 3. Direct invocation example (passing manual context docs)
response = document_chain.invoke({
    "input": "What are 2026 Challenges?",
    "context": [Document(page_content="Choose from 14 challenges for you and your team...")]
})
```

---

### B. The Retrieval Chain (`create_retrieval_chain`)

#### **Role & Functionality**
While the Document Chain knows how to format context and talk to the LLM, **it cannot search for documents itself**. 

The **Retrieval Chain** wraps around the **Retriever** and the **Document Chain** to automate the retrieval step:
1. It takes the user's raw question string from `"input"`.
2. It calls `retriever.get_relevant_documents(input)` on the FAISS vector database.
3. It automatically forwards the retrieved list of `Document` objects into the `document_chain` under the `"context"` parameter.
4. It compiles the final output payload containing `"input"`, `"context"` (the retrieved sources), and `"answer"` (the LLM's answer).

#### **Code snippet from notebook:**
```python
from langchain_classic.chains import create_retrieval_chain

# 1. Convert FAISS vector database into a retriever interface
retriever = vectorstoredb.as_retriever()

# 2. Combine Retriever and Document Chain into Retrieval Chain
retriever_chain = create_retrieval_chain(retriever, document_chain)

# 3. Execution - only pass user input!
response = retriever_chain.invoke({"input": "What are 2026 Challenges?"})

# Output access:
print("Answer:", response["answer"])
print("Retrieved Sources:", response["context"])
```

---

## 5. Pipeline Data Transformation Matrix

| Stage | Input Data | Component Used | Output Data |
| :--- | :--- | :--- | :--- |
| **Ingestion** | Web URL (`https://...`) | `WebBaseLoader` | Raw `[Document]` object |
| **Splitting** | Raw `[Document]` | `RecursiveCharacterTextSplitter` | `[Document]` chunks (size: 1000) |
| **Embedding** | Text strings | `OllamaEmbeddings` | Dense Float Vectors |
| **Indexing** | Vectors + Documents | `FAISS.from_documents()` | `FAISS` VectorStore Index |
| **Retrieval** | User Question (`str`) | `VectorStoreRetriever` | Top $k$ relevant `[Document]` chunks |
| **Doc Stuffing** | `[Document]` + Prompt | `create_stuff_documents_chain` | Populated Prompt (`{context}`) |
| **Generation** | Formatted Prompt | `ChatGroq(qwen/qwen3.8-27b)` | Generated Answer Text |

---

## 6. Key Takeaways & Best Practices

1. **Separation of Concerns**:
   - `create_stuff_documents_chain`: Handles **document formatting & LLM generation**.
   - `create_retrieval_chain`: Handles **search retrieval & chaining with retriever**.
2. **LangChain 1.x Compatibility**:
   - Imported from `langchain_classic.chains.combine_documents` and `langchain_classic.chains` when `langchain-classic` is installed.
3. **Observability**:
   - Every execution is automatically logged to LangSmith (via `LANGCHAIN_TRACING_V2`), allowing inspection of raw prompt context vs final generated answer.
