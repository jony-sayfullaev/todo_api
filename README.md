# Todo API

This is a RESTful API built using Django and Django Rest Framework for creating and managing todo lists.

## Requirements
- Python 3.x
- Django 3.x
- Django Rest Framework
- Virtual Environment

## Installation
1. Clone the repository:
- git clone https://github.com/<your-github-username>/todo_api.git

2. Navigate into the project directory:
- cd todo_api
 
4. Activate the virtual environment:
- source env/bin/activate


5. Install the dependencies:
- pip install -r requirements.txt

6. Migrate the database:
- python manage.py migrate

7. Create a superuser:
- python manage.py createsuperuser

8. Run the server:
- python manage.py runserver



The API will be available at `http://localhost:8000/`.

## Endpoints

### /auth/token/
- `POST`: Get a token for authentication. Required parameters: `username` and `password`.

### /api/todos/
- `GET`: Get a list of all todos.
- `POST`: Create a new todo. Required parameters: `title`.

### /api/todos/{id}/
- `GET`: Get a single todo by id.
- `PUT`: Update a single todo by id. Required parameters: `title`.
- `DELETE`: Delete a single todo by id.

## Authentication

This API uses token-based authentication. To get a token, make a POST request to `/auth/token/` with your username and password. The response will include a token that you can use for subsequent requests by setting the `Authorization` header with the value `Token {token}`.





