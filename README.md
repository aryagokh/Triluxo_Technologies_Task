# Triluxo_Technologies_Task

## Brainlox Chatbot using LangChain, FAISS, and Groq API
This project is a custom chatbot built with Flask, LangChain, FAISS, and Groq API.
It scrapes course data from Brainlox, stores it in a vector database, and provides intelligent responses via a Flask RESTful API.

### 📌 Features
✅ Scrapes course data from Brainlox using LangChain WebBaseLoader.
✅ Generates embeddings using Hugging Face Sentence Transformers.
✅ Stores embeddings in FAISS, enabling fast similarity search.
✅ Builds a Flask RESTful API to handle user queries.
✅ Uses Groq API to generate intelligent chatbot responses.

### 🚀 Installation & Setup
#### 1. Clone the Repository

```python
git clone https://github.com/aryagokh/Triluxo_Technologies_Task.gitcd <your-project-folder>
cd .
```

#### 2. Create a venv via conda or python

#### 3.  Install Dependencies
```python
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables
Create a .env file and add your Groq API Key:
```python
GROQ_API_KEY=your_groq_api_key
```

### Running the Chatbot API
#### 1. Start the Flask Server
```python
python app.py
```
You should see:  Running on http://127.0.0.1:5000

#### 2. Test API Using Python - You can modify this to add your own questions.
```python
python get_response.py
```

### Thank You.
#### Feel free to drop queries here : arya.gokhale1@gmail.com


