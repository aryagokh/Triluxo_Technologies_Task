import os
import requests
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from dotenv import load_dotenv
from src.vector_store import load_faiss, store_embeddings
from src.scraper import scrape_web
import logging

logging.basicConfig(filename="chatbot.log", level=logging.INFO, format="%(asctime)s - %(message)s")
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')

app = Flask(__name__)
api = Api(app)

documents = scrape_web('https://brainlox.com/courses/category/technical')
if documents:
    store_embeddings(documents=documents)
else:
    print("Falied to scrape docs.")

vector_db = load_faiss()

class Chatbot(Resource):
    def post(self):
        data = request.json
        query = data.get("query")

        retriever = vector_db.as_retriever()
        docs = retriever.get_relevant_documents(query)
        context = " ".join([doc.page_content for doc in docs])

        print("User Query:", query)
        print("Retrieved Context:", context)

        if not context:
            return jsonify({"response": "No relevant information found."})

        groq_api_key = os.getenv("GROQ_API_KEY")
        headers = {"Authorization": f"Bearer {groq_api_key}", "Content-Type": "application/json"}
        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "You are an AI assistant that answers based on the given context. If not found any context, simply tell didn't find any"},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
            ]
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)
        answer = response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response.").strip()
        
        logging.info(f"User: {query}")
        logging.info(f"AI Response: {answer}")
        
        return jsonify({"response": answer})

api.add_resource(Chatbot, "/chat")

if __name__ == "__main__":
    app.run(debug=True)
