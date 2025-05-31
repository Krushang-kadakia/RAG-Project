from flask import Flask, request, render_template, jsonify
import os

from utils.pdf_reader import read_pdf
from utils.text_chunker import chunk_text
from utils.embedder import load_model, embed_text
from utils.qdrant_handler import store_embeddings, retrieve_relevant_chunks, retrieve_all_chunks_from_storage
from utils.relevance_checker import is_query_relevant
from utils.mistral_query import query_mistral
from utils.response_formatter import clean_response, format_response

import nltk
nltk.download('punkt')

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = load_model()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_pdf():
    files = request.files.getlist("files")
    
    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        text = read_pdf(file_path)
        chunks = chunk_text(text)
        embeddings = embed_text(model, chunks)
        store_embeddings(embeddings, chunks)

    return render_template("index.html", message="PDFs uploaded and processed successfully!")

@app.route("/ask", methods=["POST"])
def ask_question():
    user_query = request.form["query"]

    all_chunks = retrieve_all_chunks_from_storage()

    if not all_chunks:
        return jsonify({"response": "⚠️ No documents uploaded yet. Please upload a PDF to begin."})

    if not is_query_relevant(user_query, model,all_chunks,):
        return jsonify({"response": "🤖 Your question seems unrelated to the uploaded documents."})

    relevant_chunks = retrieve_relevant_chunks(user_query, model)
    context = "\n".join(relevant_chunks)

    prompt = f"""
You are a helpful assistant. Use the provided context to answer the question.

=== CONTEXT START ===
{context}
=== CONTEXT END ===

Question: {user_query}
Answer:
"""
    raw = query_mistral(prompt)
    cleaned = clean_response(raw)
    formatted = format_response(cleaned)
    return jsonify({"response": formatted})

if __name__ == "__main__":
    app.run(debug=True)
