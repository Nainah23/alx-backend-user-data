---

# User Authentication Service

This project implements a simple user authentication service using Python, SQLAlchemy, and Flask. The service provides functionalities to manage users, including registration, login, and session management.

## Features

- **User Model**: Defines a SQLAlchemy model named `User` for the `users` table with fields such as `id`, `email`, `hashed_password`, `session_id`, and `reset_token`.
- **Database Management**: Provides methods to add, find, and update users in the database using SQLAlchemy.
- **Password Hashing**: Securely hashes user passwords using bcrypt.
- **User Registration**: Allows new users to register with an email and password.
- **Credentials Validation**: Validates user login credentials.
- **Session Management**: Generates and manages user sessions using UUIDs.
- **Flask API**: Provides RESTful endpoints for user registration and login.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/alx-backend-user-data.git
   cd alx-backend-user-data/0x03-user_authentication_service
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python3 app.py
   ```

## Usage

### User Registration

- **Endpoint**: `POST /users`
- **Description**: Registers a new user.
- **Form Data**:
  - `email`: User's email address.
  - `password`: User's password.
- **Response**:
  - **Success**: `{"email": "<registered email>", "message": "user created"}`
  - **Failure**: `{"message": "email already registered"}`, HTTP 400

### User Login

- **Endpoint**: `POST /sessions`
- **Description**: Logs in a user.
- **Form Data**:
  - `email`: User's email address.
  - `password`: User's password.
- **Response**:
  - **Success**: `{"email": "<user email>", "message": "logged in"}` and a session ID is set in a cookie.
  - **Failure**: HTTP 401 Unauthorized

## Project Structure

- `user.py`: Contains the `User` model.
- `db.py`: Handles database operations, including adding, finding, and updating users.
- `auth.py`: Manages authentication tasks like password hashing, user registration, and session creation.
- `app.py`: Sets up the Flask app and defines API routes.

## Testing

To run the provided test cases, execute the following command:
```bash
python3 -m unittest discover tests
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Authors

- [Ian Wainaina Kamau](https://github.com/Nainah23)

---
