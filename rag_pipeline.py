import os
import pickle
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings

load_dotenv()

class RAGPipeline:
    def __init__(self, content, index_path="faiss_index"):
        self.index_path = index_path
        self.embeddings = HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        if os.path.exists(f"{index_path}.faiss"):
            self.vectorstore = FAISS.load_local(index_path, self.embeddings)
        else:
            self.docs = [Document(page_content=content)]
            self.vectorstore = FAISS.from_documents(self.docs, self.embeddings)
            self.vectorstore.save_local(index_path)

        openai_api_key = os.getenv("OPENAI_API_KEY")
        openai_api_base = os.getenv("OPENAI_API_BASE")
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=OpenAI(temperature=0, openai_api_key=openai_api_key,openai_api_base=openai_api_base),
            retriever=self.vectorstore.as_retriever()
        )

    def ask(self, query):
        return self.qa_chain.run(query)
