from langchain.retrievers import ParentDocumentRetriever
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.storage import InMemoryStore


parent_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=20, separator='\n')

child_splitter = CharacterTextSplitter(chunk_size=400, chunk_overlap=20, separator='\n')


vectorstore = Chroma(
    collection_name="split_parents", embedding_function=watsonx_embedding
)

store = InMemoryStore()


retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)

retriever.add_documents(document)
