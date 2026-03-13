# 🤖 AI Knowledge Assistant

**An Industry-Grade Retrieval Augmented Generation (RAG) System with Web Search Fallback**

---

# Overview

AI Knowledge Assistant is an intelligent question-answering system that combines **Large Language Models (LLMs)** with **Retrieval Augmented Generation (RAG)** and **real-time web search**.

The system allows users to:

• Upload PDF documents
• Ask natural language questions
• Retrieve knowledge from uploaded documents
• Fall back to web search when information is unavailable
• Generate concise or detailed responses using an LLM

This architecture mimics **modern production AI assistants used by companies such as OpenAI, Perplexity, and Google Gemini.**

---

# Key Features

### 1. Document Question Answering

Upload PDFs and ask questions about the content.

### 2. Retrieval Augmented Generation (RAG)

Relevant sections of the document are retrieved and provided to the LLM as context.

### 3. Web Search Fallback

If the answer is not found in the document database, the system automatically performs a web search.

### 4. LLM Powered Reasoning

The assistant uses Groq-hosted models for fast inference and high-quality responses.

### 5. Conversational Interface

Chat-based interface built using Streamlit.

### 6. Response Modes

Users can choose between:

• Concise
• Detailed

### 7. Session Memory

Chat history is stored during the session.

---

# System Architecture

The application follows a **modular architecture** inspired by production AI systems.

```
                ┌───────────────────────────┐
                │        User Interface      │
                │        (Streamlit)         │
                └─────────────┬─────────────┘
                              │
                              ▼
                   ┌────────────────────┐
                   │   Query Processing  │
                   └─────────┬──────────┘
                             │
               ┌─────────────┴─────────────┐
               │                           │
               ▼                           ▼
      ┌───────────────┐           ┌────────────────┐
      │   Vector DB    │           │  Web Search     │
      │   (FAISS)      │           │   (SerpAPI)     │
      └───────┬────────┘           └────────┬───────┘
              │                              │
              └──────────────┬───────────────┘
                             ▼
                    ┌─────────────────┐
                    │  Prompt Builder  │
                    └─────────┬───────┘
                              ▼
                     ┌────────────────┐
                     │   LLM (Groq)    │
                     └─────────┬──────┘
                               ▼
                        Generated Answer
```

---

# Retrieval Augmented Generation Workflow

```
User Question
      │
      ▼
Check Vector Database
      │
      ├── Found Relevant Docs
      │         │
      │         ▼
      │    Provide Context
      │
      └── No Relevant Docs
                │
                ▼
            Web Search
                │
                ▼
         Build Final Prompt
                │
                ▼
          LLM Generates Answer
```

---

# Project Structure

```
AI_UseCase/
│
├── app.py
│
├── models/
│   └── llm.py
│
├── utils/
│   ├── document_loader.py
│   ├── rag_utils.py
│   ├── web_search.py
│   └── prompt_utils.py
│
├── config/
│   └── config.py
│
├── temp.pdf
│
└── README.md
```

---

# Module Description

## app.py

Main application entry point.

Responsibilities:

• Streamlit UI
• Chat interaction
• PDF upload handling
• Query routing
• LLM response display

---

## models/llm.py

Handles LLM initialization.

Responsible for:

• Loading Groq models
• Configuring inference parameters

---

## utils/document_loader.py

Loads and parses PDF documents.

Uses:

```
PyPDFLoader
```

Extracted text is converted into LangChain documents.

---

## utils/rag_utils.py

Responsible for RAG operations.

Functions include:

• Text chunking
• Embedding generation
• FAISS vector database creation
• Similarity search

---

## utils/web_search.py

Handles external knowledge retrieval.

Uses:

```
SerpAPI
```

Returns search results used as fallback context.

---

## utils/prompt_utils.py

Builds structured prompts for the LLM.

Prompt includes:

• Retrieved context
• User query
• Response style (Concise/Detailed)

---

# Technology Stack

| Layer               | Technology            |
| ------------------- | --------------------- |
| Frontend            | Streamlit             |
| LLM                 | Groq                  |
| Embeddings          | Sentence Transformers |
| Vector Database     | FAISS                 |
| Retrieval Framework | LangChain             |
| Web Search          | SerpAPI               |
| Language            | Python                |

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai-knowledge-assistant.git
```

Navigate into the project:

```
cd ai-knowledge-assistant
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```
GROQ_API_KEY=your_groq_api_key
SERPAPI_API_KEY=your_serpapi_key
```

---

# Running the Application

Start the Streamlit server:

```
streamlit run app.py
```

Open the application:

```
http://localhost:8501
```

---

# Usage

### Step 1

Upload a PDF document.

### Step 2

Ask questions related to the document.

### Step 3

If the document does not contain the answer, the assistant retrieves information from the web.

---

# Example Queries

Document Questions:

```
Summarize the document
```

```
What is the main topic discussed?
```

General Questions:

```
Who is the CEO of NVIDIA?
```

```
What is the latest version of Python?
```

---

# Performance Considerations

• FAISS enables **fast semantic search** even with large document collections.
• Groq inference provides **low-latency LLM responses**.
• RAG reduces hallucination by grounding answers in documents.

---

# Security Considerations

• API keys stored in `.env`
• No document data is permanently stored
• Temporary files are overwritten

---

# Future Improvements

Potential enhancements:

• Multi-document knowledge base
• Source citation display
• Streaming responses
• Memory-based conversations
• Vector database persistence
• Authentication system

---

# Industry Applications

This architecture is commonly used in:

• Enterprise knowledge assistants
• Customer support automation
• Research assistants
• Legal document analysis
• Internal company documentation search

---

# Conclusion

AI Knowledge Assistant demonstrates a **modern AI application architecture combining LLMs, RAG, and real-time information retrieval**.

The modular design allows easy extension and integration with enterprise systems.

This project serves as a **foundation for building scalable AI knowledge systems.**

---

# Author

Manoj PM

manojpoojari1511@gmail.com

AI Engineer Candidate
