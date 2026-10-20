from src.helper import (
    load_repo,
    text_splitter,
    load_embedding
)

from langchain_community.vectorstores import Chroma

documents = load_repo("repo")

if len(documents) == 0:
    raise Exception(
        "No python files found under repo folder"
    )

text_chunks = text_splitter(documents)

if len(text_chunks) == 0:
    raise Exception(
        "No chunks generated"
    )

print(f"Created {len(text_chunks)} chunks")

embeddings = load_embedding()

vectordb = Chroma.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    persist_directory="./db"
)

print("Vector Database Created Successfully")