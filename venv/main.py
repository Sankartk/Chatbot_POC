from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import crud
from firebaseint import get_firebase_app

# Initialize Firebase as soon as possible
get_firebase_app()

class Message(BaseModel):
    user_message: str

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/chatlogs")
def get_chat_logs(skip: int = 0, limit: int = 10):
    chatlogs = crud.get_chat_logs(skip=skip, limit=limit)
    return chatlogs

@app.post("/chat/")
def post_chat(message: Message):
    bot_response = f"Bot: I received your message '{message.user_message}'"
    log_key = crud.create_chat_log(message.user_message, bot_response)
    return {"response": bot_response, "log_key": log_key}

@app.get("/query_chatlogs/")
def query_chat_logs(message_text: str):
    results = crud.query_chat_logs(message_text)
    return results

@app.get("/employees/")
def get_employees_by_department(department: str):
    try:
        employees = crud.query_employees_by_department(department)
        return employees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
