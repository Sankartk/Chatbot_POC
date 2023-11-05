
import firebase_admin
from firebase_admin import credentials, db

# Global variable to keep track of the initialized app
firebase_app = None

def get_firebase_app():
    global firebase_app
    if not firebase_app:
        # Provide the actual path to your Firebase admin SDK JSON file
        cred = credentials.Certificate("C:\\Users\\karth\\OneDrive\\Documents\\project_backend\\venv\\projectbackend-921dd-firebase-adminsdk-lvtvy-64ccb635fc.json")
        firebase_app = firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://projectbackend-921dd-default-rtdb.firebaseio.com/'
        })
    return firebase_app

def store_in_firebase(user_message, bot_response):
    get_firebase_app()  # Ensure Firebase is initialized
    ref = db.reference('chatlogs')
    new_log = ref.push({
        'user_message': user_message,
        'bot_response': bot_response
    })
    return new_log.key

def get_chat_logs():
    get_firebase_app()  # Ensure Firebase is initialized
    ref = db.reference('chatlogs')
    chat_logs = ref.get()
    for key, value in chat_logs.items():
        print(f"{key} => {value}")


