from firebase_admin import db
from pydantic import BaseModel

# Defining data model as Pydantic BaseModel
class ChatLog(BaseModel):
    user_message: str
    bot_response: str

# Function to create a new chat log entry in Firebase
def create_chat_log(user_message: str, bot_response: str):
    ref = db.reference('chatlogs')
    new_log = ref.push({
        'user_message': user_message,
        'bot_response': bot_response
    })
    return new_log.key  # Return the unique key for the new log entry

# Function to retrieve chat logs from Firebase
def get_chat_logs(skip: int = 0, limit: int = 10):
    ref = db.reference('chatlogs')
    chat_logs = ref.order_by_key().limit_to_first(skip + limit).get()
    chat_logs_list = [{k: v} for k, v in chat_logs.items()][skip:] if chat_logs else []
    return chat_logs_list

# Function to query chat logs that contain a specific message text
def query_chat_logs(message_text):
    ref = db.reference('chatlogs')
    query = ref.order_by_child('user_message').equal_to(message_text).get()
    return [{key: val} for key, val in query.items()] if query else []

# Function to query employees by department
def query_employees_by_department(department: str):
    ref = db.reference('employees')
    query = ref.order_by_child('department').equal_to(department).get()
    return [{key: val} for key, val in query.items()] if query else []
