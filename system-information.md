
# System Information

## Project Overview

This project is a FastAPI-based web application that provides a starting point for building agentic applications. It includes a user authentication system with three options: email/password, Google OAuth2, and GitHub OAuth2. The application is containerized using Docker and managed with a Makefile.

## Project Structure

The project is organized into the following directories:

*   `src`: Contains the main source code for the application.
    *   `api`: Defines the API endpoints for the application.
    *   `core`: Implements the core logic of the application, including authentication, configuration, and security.
    *   `crud`: Provides functions for creating, reading, updating, and deleting data from the database.
    *   `db`: Manages the database connection and session.
    *   `models`: Defines the database models.
    *   `schemas`: Defines the data validation schemas.
*   `test`: Contains the tests for the application.

## Database Schema

The application uses a SQLite database with a single table: `user`.

### `user` table

| Column          | Type    | Constraints                |
| --------------- | ------- | -------------------------- |
| id              | Integer | Primary Key, Auto Increment |
| email           | String  | Unique, Not Null           |
| hashed_password | String  | Not Null                   |
| is_active       | Boolean | Default: True              |

**Relationships:**

There are no relationships between tables in the current schema.

## Authentication Flow

The application supports three authentication methods:

1.  **Email/Password:**
    *   The user provides their email and password.
    *   The application verifies the credentials and returns a JWT token.
2.  **Google OAuth2:**
    *   The user is redirected to Google for authentication.
    *   Google redirects the user back to the application with an authorization code.
    *   The application exchanges the authorization code for an access token and user information.
    *   The application creates or updates the user in the database and returns a JWT token.
3.  **GitHub OAuth2:**
    *   The user is redirected to GitHub for authentication.
    *   GitHub redirects the user back to the application with an authorization code.
    *   The application exchanges the authorization code for an access token and user information.
    *   The application creates or updates the user in the database and returns a JWT token.

## API Endpoints

The application exposes the following API endpoints:

*   `POST /api/users/`: Create a new user.
*   `GET /api/users/me`: Get the current user's information.
*   `POST /api/login/token`: Get an access token.
*   `GET /api/oauth/login/google`: Redirect to Google for authentication.
*   `GET /api/oauth/auth/google`: Callback for Google authentication.
*   `GET /api/oauth/login/github`: Redirect to GitHub for authentication.
*   `GET /api/oauth/auth/github`: Callback for GitHub authentication.

## System Information

*   **Framework:** FastAPI
*   **Database:** SQLite
*   **Authentication:** JWT, OAuth2
*   **Containerization:** Docker
*   **Build Tool:** Make
