from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

def load_vectorstore(vectorstore_path, index_name):
    vectorstore = FAISS.load_local(folder_path=vectorstore_path, index_name=index_name, embeddings=OpenAIEmbeddings())
    return vectorstore