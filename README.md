# JWT authentication in FastApi

This repository showcases an example implementation of a RESTful API using FastAPI, a modern web framework for building APIs with Python.

## Features

- Retrieve a list of posts
- Retrieve a single post by ID
- Create a new post
- User signup and login functionality with JWT authentication

## Requirements

- Python 3.6+
- pip (Python package manager)

## Installation

To install the project, follow these steps:

```shell
git clone https://github.com/AnimBadger/fast-jwt.git

Navigate to the project directory:
cd fast-jwt

Create and activate a virtual environment (optional, but recommended):
python3 -m venv venv
source venv/bin/activate

Install the dependencies:
pip install -r requirements.txt
```

## Usage

```shell
Run the FastAPI application:
- uvicorn main:app --reload

This command starts the FastAPI application and enables auto-reload for development.

Access the API at http://localhost:8000 in your browser or use an API testing tool like Postman.
```

## Endpoints

- GET / - Retrieves a greeting message.
- GET /posts - Retrieves a list of all posts.
- GET /posts/{id} - Retrieves a single post by its ID.
- POST /posts - Creates a new post.
- POST /users/signup - Registers a new user.
- POST /users/login - Logs in an existing user.

## Documentation

- The API is self-documented using Swagger UI.
- Access the API documentation at http://localhost:8000/docs

## Contribution

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

