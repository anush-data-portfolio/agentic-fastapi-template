
# fastapi-agentic-starter

This is a template for a Python-based web application using the FastAPI framework. It includes a simple user and login API with a JWT authentication flow and a SQLite database setup.

## Author

*   **Anush Krishna**
    *   GitHub: [anushkrishnav](https://github.com/anushkrishnav)
    *   Email: [anush.venkatakrishna@gmail.com](mailto:anush.venkatakrishna@gmail.com)

## Features

*   **FastAPI:** A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
*   **SQLAlchemy:** The Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
*   **Pydantic:** Data validation and settings management using Python type annotations.
*   **JWT Authentication:** A simple and secure authentication flow using JSON Web Tokens.
*   **OAuth2:** A simple and secure authentication flow using OAuth2 for Google and GitHub.
*   **SQLite:** A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
*   **Docker:** A set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.
*   **Makefile:** A file containing a set of directives used by a make build automation tool to generate a target/goal.

## Getting Started

### Prerequisites

*   Python 3.10+
*   Docker
*   Make

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/anushkrishnav/fastapi-agentic-starter.git
    cd fastapi-agentic-starter
    ```

2.  **Set up the environment:**

    *   Copy `.env.example` to `.env`
    *   Update the environment variables in `.env`, especially `SECRET_KEY`, `GEMINI_API_KEY`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GITHUB_CLIENT_ID`, and `GITHUB_CLIENT_SECRET`.

3.  **Build the Docker image:**

    ```bash
    make build
    ```

### Running the Application

```bash
make run
```

The application will be available at `http://localhost:8000`.

### Running Tests

```bash
make test
```

## API Endpoints

*   `POST /api/users/`: Create a new user.
*   `GET /api/users/me`: Get the current user's information.
*   `POST /api/login/token`: Get an access token.
*   `GET /api/oauth/login/google`: Redirect to Google for authentication.
*   `GET /api/oauth/auth/google`: Callback for Google authentication.
*   `GET /api/oauth/login/github`: Redirect to GitHub for authentication.
*   `GET /api/oauth/auth/github`: Callback for GitHub authentication.

## Project Structure

```
.
├── Dockerfile
├── Makefile
├── README.md
├── LICENSE
├── requirements.txt
├── src
│   ├── api
│   │   ├── __init__.py
│   │   ├── login.py
│   │   ├── oauth.py
│   │   └── users.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── config.py
│   │   ├── oauth.py
│   │   └── security.py
│   ├── crud
│   │   ├── __init__.py
│   │   └── user.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── session.py
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user.py
│   └── schemas
│       ├── __init__.py
│       ├── token.py
│       └── user.py
└── test
    ├── test_login.py
    └── test_users.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
