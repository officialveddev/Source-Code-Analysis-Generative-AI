import os
import shutil
import subprocess

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM

from src.helper import (
    repo_ingestion,
    load_embedding
)

app = Flask(__name__)

embeddings = load_embedding()

llm = OllamaLLM(
    model="llama3"
)

persist_directory = "./db"


def get_vector_db():

    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chatbot", methods=["POST"])
def chatbot():

    repo_url = request.form["question"]

    repo_ingestion(repo_url)

    subprocess.run(
        ["python", "store_index.py"],
        check=True
    )

    return jsonify(
        {
            "response": "Repository indexed successfully"
        }
    )


@app.route("/get", methods=["POST"])
def chat():

    user_input = request.form["msg"]

    if user_input.lower() == "clear":

        shutil.rmtree(
            "repo",
            ignore_errors=True
        )

        shutil.rmtree(
            "db",
            ignore_errors=True
        )

        return "Repository cleared"

    vectordb = get_vector_db()

    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    docs = retriever.invoke(user_input)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an expert software engineer.

Use the repository code below to answer.

Repository Context:
{context}

Question:
{user_input}

Answer:
"""

    response = llm.invoke(prompt)

    return str(response)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
