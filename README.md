# Chatbot POC

## Introduction

This project is a proof of concept for a chatbot application. It is composed of a frontend made with AngularJS, a backend API developed with FastAPI, and uses Firebase Realtime Database for data storage. The application allows users to send messages to a chatbot and receive responses, as well as view a list of employees by department.

## Project Structure

The project is divided into two main parts:

- `frontend`: Contains the AngularJS application files, including `index.html` for markup, `styles.css` for styling, and `app.js` for the AngularJS application logic.
- `backend`: Contains the FastAPI application files, with `main.py` as the entry point. It also includes `crud.py` for database operations and `firebaseint.py` for initializing the Firebase connection.

## Backend

The FastAPI backend serves as the server-side logic handling chat operations, including sending and receiving messages, and interacting with the Firebase Realtime Database.

- `crud.py`: Contains functions for creating chat logs, retrieving chat logs, and querying the database for specific messages or employees.
- `firebaseint.py`: Manages the Firebase admin SDK initialization and provides a function to store chat messages in the database.
- `seed.py`: A script to seed the Firebase database with initial employee data.
- `main.py`: Defines the FastAPI application, API endpoints, and integrates the CRUD operations for chat interactions.

## Frontend

The AngularJS frontend provides a user interface for interacting with the chatbot.

- `index.html`: The main HTML document that includes the chat interface and employee listing.
- `app.js`: Defines the AngularJS application logic, responsible for sending messages and retrieving chat logs and employee data from the backend.
- `styles.css`: Contains the CSS styles for the chat interface and employee listing.

## Setup & Installation

### Requirements

- Python 3.6+
- Node.js and npm (for AngularJS dependencies if they are not included)
- Firebase account and project

### Backend Setup

1. Clone the repository and navigate to the `backend` directory.
2. Install the required Python dependencies:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


Initialize Firebase by replacing the paths in firebaseint.py and seed.py with your Firebase credentials JSON file.
Run seed.py to seed the database with initial data:
python seed.py

Start the FastAPI server:
uvicorn main:app –reload

The API will now be accessible at http://localhost:8000.

Frontend Setup
Navigate to the frontend directory.
Open the index.html file in a web browser to access the user interface.
Usage
Interact with the chatbot through the frontend interface by sending messages and viewing responses. You can also list employees by department using the provided input and button.
