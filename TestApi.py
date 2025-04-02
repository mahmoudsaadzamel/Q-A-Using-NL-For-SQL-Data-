import requests

def test_api(question):
    url = "http://localhost:8005/query"
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
        "What tasks are assigned to Abeer Hany?",
        "What is the oldest pending task?",
        "Which employees work in Operations?",
        "Which employees were hired before 2023?"
    ]
    
    for question in test_questions:
        test_api(question)
        print("\n" + "="*50 + "\n")