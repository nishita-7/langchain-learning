# LangChain Learning Journey 🦜⛓️

A hands-on exploration of the LangChain framework — from basic chat model integrations to chains, runnables, and document loaders. Work in progress.

## What's Covered

| # | Topic | What I Built |
|---|-------|-------------|
| 1 | **Chat Models** | Integrations with OpenAI, Anthropic, Gemini, Groq, and HuggingFace (API + local) |
| 2 | **Embedding Models** | OpenAI and HuggingFace embeddings; document similarity search |
| 3 | **LLMs** | Basic LLM demo with the legacy LLM interface |
| 4 | **Prompts** | PromptTemplates, ChatPromptTemplates, MessagePlaceholders, a chatbot with history, and a Streamlit prompt UI |
| 5 | **Structured Outputs** | Pydantic, TypedDict, and JSON Schema approaches to structured generation |
| 6 | **Output Parsers** | StrOutputParser, JsonOutputParser, PydanticOutputParser, StructuredOutputParser |
| 7 | **Chains** | Simple, sequential, parallel, and conditional chains using LCEL |
| 8 | **Runnables** | RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch |
| 9 | **Document Loaders** | Text, PDF, CSV, web, and directory loaders |
| 10 | **Text Splitters** | Character text splitter, Recursive splitting, document structure based, semantic splitting |
| 10 | **Vector Stores** | chroma, FAISS |

## Stack

- **LangChain** (core + integrations)
- **LLM providers**: OpenAI, Anthropic, Google Gemini, Groq, HuggingFace
- **Python 3.10+**

## Setup

```bash
git clone https://github.com/nishita-7/langchain-learning
cd LangChain
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your API keys:

```
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GOOGLE_API_KEY=...
GROQ_API_KEY=...
HUGGINGFACEHUB_API_TOKEN=...
```

## How to Run

Each folder is self-contained. Navigate into any topic and run the script directly:

```bash
python "7. Chains/parallel_chain.py"
```

## Status

Actively learning — new folders will be added as I progress through more LangChain concepts.

---

*Learning in public. Feedback welcome.*