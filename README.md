````markdown
# RAG Project

This project implements a Retrieval-Augmented Generation (RAG) system using:

- `llama.cpp` for LLM inference  
- `Qdrant` for vector database  
- Custom text processing and embedding pipelines

---

## Setup Guide

### 1. Clone the repository

```bash
git clone https://github.com/Krushang-kadakia/RAG-Project.git
cd RAG-Project
````

### 2. Create and activate a Python virtual environment

**Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required Python packages

Make sure `requirements.txt` exists with all dependencies listed.

```bash
pip install -r requirements.txt
```

### 4. Initialize the Qdrant vector database

> **Note:** The `qdrant_database` folder is not included in the repo as it contains large files.
> You need to generate the database locally by running the ingestion script.

Run the script that:

* Processes your documents (e.g., PDFs)
* Extracts text chunks
* Creates embeddings
* Uploads vectors to Qdrant database

Example (replace with your actual script):

```bash
python scripts/ingest.py
```

### 5. Run the application

Start your Flask or other server application:

```bash
python app.py
```

---

## Important Notes

* **Do not commit large binary files** like virtual environments, Qdrant database files, or model weights. They are ignored via `.gitignore`.
* If you want to manage large model files, consider using [Git LFS](https://git-lfs.github.com/).
* Keep your virtual environment isolated from the project repo.
* Document any custom scripts you write for ingestion, preprocessing, or deployment.

---

## Troubleshooting

* If you face issues with missing packages, run `pip install -r requirements.txt` again.
* To reset Qdrant database, delete the local `qdrant_database` folder and rerun the ingestion script.
* Make sure your Python version is compatible (e.g., Python 3.8+).

---
