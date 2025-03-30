import requests

def test_api(question):
    url = "http://localhost:8000/query"
    payload = {"question": question}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Question:", question)
            print("Answer:", response.json()["answer"])
        else:
            print("Error:", response.text)
    except Exception as e:
        print("API request failed:", e)

if __name__ == "__main__":
    test_questions = [
        "Who are the employees in the IT department?",
        "What tasks are assigned to Ali Kamal?",
        "How many pending tasks are there?",
        "List all completed tasks",
        "Who was hired most recently?",
        "Which employees work in Marketing?"
    ]
    
    for question in test_questions:
        test_api(question)
        print("\n" + "="*50 + "\n")