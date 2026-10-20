import os
import shutil

from git import Repo

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    Language,
)
from langchain_huggingface import HuggingFaceEmbeddings


def repo_ingestion(repo_url):

    if os.path.exists("repo"):
        shutil.rmtree("repo")

    Repo.clone_from(
        repo_url,
        "repo"
    )


def load_repo(repo_path):

    loader = DirectoryLoader(
        repo_path,
        glob="**/*.py",
        loader_cls=TextLoader,
        show_progress=True
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} documents")

    return documents


def text_splitter(documents):

    splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=2000,
        chunk_overlap=200
    )

    return splitter.split_documents(documents)


def load_embedding():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings