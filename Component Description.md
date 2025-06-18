| Component                        | Description                                                                                                                            |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `app.py`                         | The Streamlit-based web UI for uploading Excel files and asking questions.                                                             |
| `data_ingestion.py`              | Reads all sheets from Excel and compiles them into a text blob.                                                                        |
| `rag_pipeline.py`                | Creates vector embeddings (with `HuggingFaceBgeEmbeddings`), stores them in FAISS, and integrates with OpenAI for answering questions. |
| `requirements.txt`               | Lists all Python dependencies.                                                                                                         |
| `.env`                           | Holds the OpenAI API key (not committed to Git).                                                                                       |
| `faiss_index/`                   | Stores the FAISS embedding index locally to prevent recomputation.                                                                     |
| `README.md` | Documentation and explanation of architecture and usage.                                                                               |
