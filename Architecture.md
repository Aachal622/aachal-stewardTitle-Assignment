![img.png](img.png)

          ┌────────────┐
          │  Excel UI  │◄───── Upload Excel & Input Query
          └────┬───────┘
               │
               ▼
       ┌──────────────────┐
       │ Data Ingestion   │◄── Excel content read into string
       └──────────────────┘
               │
               ▼
     ┌────────────────────────┐
     │ FAISS Vector Store     │◄── Create or load embedding index
     └────────────────────────┘
               │
               ▼
     ┌────────────────────────┐
     │ Retrieval QA (LangChain)│◄── Relevant chunks fetched
     └────────────────────────┘
               │
               ▼
          ┌─────────────┐
          │ OpenAI LLM  │◄── Prompt with context + question
          └─────────────┘
               │
               ▼
         ┌────────────┐
         │  Answer UI │◄── Show result in Streamlit
         └────────────┘

