from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql.base import SQLDatabaseChain  #
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


                                ####### Set your OpenAI API key #########
OPENAI_API_KEY = ""

def get_sqlalchemy_engine():
    """Creates an SQLAlchemy engine for LangChain integration."""
    return create_engine("mysql+mysqlconnector://root:PythonTasks%401234@localhost/company_db")


# Initialize LangChain SQL Database
engine = get_sqlalchemy_engine()
db = SQLDatabase(engine)
llm = ChatOpenAI(model_name="gpt-4-turbo", openai_api_key=OPENAI_API_KEY)
db_chain = SQLDatabaseChain.from_llm(llm, db)

def answer_question(question):
    """Uses LangChain SQLDatabaseChain to answer SQL-related questions."""
    try:
        response = db_chain.invoke(question)
        return response.get("result", "No answer found.")  # Extract only the result

    except Exception as e:
        return f"Error processing the query: {e}"

# Main execution
if __name__ == "__main__":
    question = input("Ask a question: ")
    ai_answer = answer_question(question)
    print(f"AI Answer: {ai_answer}")
