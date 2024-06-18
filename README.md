FastAPI User Management System

This project is a user management system built using FastAPI and MongoDB. It includes APIs for user registration, login, linking an ID, joining data from multiple collections, and deleting users 

along with their associated data.



Project Structure

main.py: The main entry point for the FastAPI application.

database.py: Handles MongoDB connection setup.

models.py: Defines Pydantic models for data validation.

routes/: Contains route handlers for various functionalities.

user.py: Handles user registration.

auth.py: Handles user login.

link.py: Handles linking an ID to a user's account.

join.py: Handles joining data from multiple collections.

delete.py: Handles deleting a user and associated data.

utils/: Contains utility functions.

security.py: Handles password hashing and verification.

requirements.txt: Lists all required Python packages.

Requirements

Python 3.7+

MongoDB

Installation

Clone the repository:


git clone https://github.com/yourusername/my_fastapi_project.git

cd my_fastapi_project

Create and activate a virtual environment:



python -m venv env

source env/bin/activate (On Windows use env\Scripts\activate)

Install the required packages:


pip install -r requirements.txt

Configuration

Ensure your MongoDB instance is running and update the MongoDB connection string in database.py if needed.


Running the Application

Start the FastAPI application using uvicorn:

uvicorn main:app --reload

The application will be available at http://127.0.0.1:8000.

API Endpoints

Registration: /user/register (POST)

Login: /auth/login (POST)

Link ID: /link (POST)

Join Data: /join (GET)

Delete User: /delete/{user_id} (DELETE)



Contact
For any questions or issues, please contact tharungurana788@gmail.com.
