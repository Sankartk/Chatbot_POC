import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:\\Users\\karth\\OneDrive\\Documents\\project_backend\\venv\\projectbackend-921dd-firebase-adminsdk-lvtvy-64ccb635fc.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://projectbackend-921dd-default-rtdb.firebaseio.com/'
})

def seed_employees_data():
    employees_ref = db.reference('employees')
    
    employees_ref.push({
        'name': "John Doe",
        'department': "HR",
        'position': "Manager"
    })
    employees_ref.push({
        'name': "Jane Smith",
        'department': "IT",
        'position': "Developer"
    })
    employees_ref.push({
        'name': "Bob Johnson",
        'department': "Marketing",
        'position': "Designer"
    })

if __name__ == "__main__":
    seed_employees_data()
    print("Employees data seeded to Firebase Realtime Database successfully.")
