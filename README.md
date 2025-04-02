
# AI Database Query System


## 📌 Quick Start
```bash
# 1. Clone and setup
git clone https://github.com/yourusername/ai-db-query.git
cd ai-db-query
pip install -r requirements.txt

# 2. Configure environment
  OPENAI_API_KEY=  "your_openai_key_here"
  DB_URL="mysql+mysqlconnector://root:yourpassword@localhost/company_db" 

# 3. Run API server
python API.py



##🔧 Key Files

File Purpose

`API.py` : FastAPI server (port 8005)

`ai_model.py` : LangChain AI model

`TestApi.py` : Pre-built test cases

`database_setup.sql` : MySQL schema


🚀 Usage Examples 

## Via VS Code

# Test individual questions
python ai_model.py
Enter: "Who has pending tasks?"

# Run all test cases
python TestApi.py


# Pro Tip: For Postman testing, add these headers:
Content-Type: application/json  
Accept: application/json

### Via Postman

1.  Send  `POST`  request to: Copy: "http://localhost:8005/query"
    
2.  Request Body (JSON):  Copy: {"question": "List Marketing department tasks"}
    
3.  Expected Response:
    {
      "answer": "Marketing department tasks: Plan social media campaign (Completed), Design new email marketing strategy (In Progress)"
    }
