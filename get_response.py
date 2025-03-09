import requests

url = "http://127.0.0.1:5000/chat"

queries = [
    "What courses are available on Brainlox?",
    "What is the price of the AI course if available?",
    "What is the capital of USA?"
]

for query in queries:
    data = {"query": query}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Question:", query)
        print("Full Response:", response.json().get('response', 'No response.'))
        print("-" * 50)
    else:
        print("Error:", response.status_code, response.text)
