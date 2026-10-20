# 🚀 Source Code Analysis using Generative AI

Analyze any public GitHub repository using a local LLM powered by **Ollama**, **LangChain**, and **ChromaDB**.

The application clones a GitHub repository, indexes the source code, stores embeddings in ChromaDB, and allows you to ask questions about the codebase through a conversational interface.

---

## ✨ Features

- Analyze any public GitHub repository
- Generate embeddings using HuggingFace models
- Local vector database using ChromaDB
- Local LLM inference using Ollama
- No OpenAI API key required
- Ask questions about source code architecture, functions, classes, and implementation details

---

## 🏗️ Tech Stack

- Python
- Flask
- LangChain
- Ollama
- ChromaDB
- HuggingFace Embeddings
- GitPython

---

## 📋 Prerequisites

- Python 3.12+
- Ollama installed locally

### Install Ollama

Download and install:

https://ollama.com

Pull the Llama 3 model:

```bash
ollama pull llama3
```

Start the Ollama server:

```bash
ollama serve
```

---

## ⚙️ Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/officialveddev/Source-Code-Analysis-Generative-AI.git
```

```bash
cd Source-Code-Analysis-Generative-AI
```

---

### Step 2: Create a Virtual Environment

```bash
python3 -m venv myenv
```

Activate the environment:

```bash
source myenv/bin/activate
```

---

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

---

### Step 4: Start Ollama

Make sure Ollama is running:

```bash
ollama serve
```

Verify model availability:

```bash
ollama list
```

Expected:

```text
llama3
```

---

### Step 5: Run the Application

```bash
python app.py
```

---

## 🌐 Access the Application

Open your browser and navigate to:

```text
http://localhost:8080
```

---

## 📖 How to Use

### Index a Repository

Provide a public GitHub repository URL, for example:

```text
https://github.com/pallets/flask
```

The application will:

1. Clone the repository
2. Read Python source files
3. Generate embeddings
4. Store vectors in ChromaDB

### Ask Questions

Examples:

```text
Explain the project architecture.
```

```text
How is authentication implemented?
```

```text
Which files contain database logic?
```

```text
What does app.py do?
```

```text
Explain the API flow.
```

---

## 📂 Project Structure

```text
Source-Code-Analysis-Generative-AI/
│
├── app.py
├── store_index.py
├── requirements.txt
├── README.md
│
├── db/
│
├── repo/
│
├── src/
│   ├── helper.py
│   └── prompt.py
│
├── static/
├── templates/
│
└── myenv/
```

---

## 📌 Notes

- This project uses a local LLM through Ollama.
- No OpenAI API key is required.
- ChromaDB is used as the vector database.
- Embeddings are generated using the HuggingFace model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

---

## 🧹 Clear Repository Data

Type:

```text
clear
```

to remove indexed repository data and start over.

---

## 🤝 Contributing

Feel free to fork the repository, raise issues, and submit pull requests.

---

## 📜 License

This project is intended for learning and educational purposes.