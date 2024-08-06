# Simple Basic API

This project implements a basic API with user authentication using Flask. The storage of users is handled via serialization/deserialization in files.

## Setup and Start Server

1. **Download and Install Dependencies:**
    ```bash
    pip3 install -r requirements.txt
    ```

2. **Start the Server:**
    ```bash
    API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
    ```

3. **Use the API:**
    ```bash
    curl "http://0.0.0.0:5000/api/v1/status" -vvv
    ```

    Example Response:
    ```json
    {"status": "OK"}
    ```

## Repository

- **GitHub repository:** `alx-backend-user-data`
- **Directory:** `0x01-Basic_authentication`

## Tasks

### 0. Simple-basic-API

Set up a simple API with one model: User. Storage of users is done via a serialization/deserialization in files.

### 1. Error Handler: Unauthorized

Add an error handler for HTTP status code 401 (Unauthorized).

- **Edit `api/v1/app.py`:**
    - Add an error handler for status code 401 that responds with:
      ```json
      {"error": "Unauthorized"}
      ```
    - Status code: 401
    - Use `jsonify` from Flask

- **Add Endpoint in `api/v1/views/index.py`:**
    - Route: `GET /api/v1/unauthorized`
    - Raise a 401 error using `abort`

### 2. Error Handler: Forbidden

Add an error handler for HTTP status code 403 (Forbidden).

- **Edit `api/v1/app.py`:**
    - Add an error handler for status code 403 that responds with:
      ```json
      {"error": "Forbidden"}
      ```
    - Status code: 403
    - Use `jsonify` from Flask

- **Add Endpoint in `api/v1/views/index.py`:**
    - Route: `GET /api/v1/forbidden`
    - Raise a 403 error using `abort`

### 3. Auth Class

Create a class to manage API authentication.

- **Create Folder:** `api/v1/auth`
- **Create Files:**
    - `api/v1/auth/__init__.py`
    - `api/v1/auth/auth.py`
- **Class `Auth`:**
    - Method `require_auth(self, path: str, excluded_paths: List[str]) -> bool`: returns `False`
    - Method `authorization_header(self, request=None) -> str`: returns `None`
    - Method `current_user(self, request=None) -> TypeVar('User')`: returns `None`

### 4. Define Which Routes Don't Need Authentication

Update the `require_auth` method in `Auth`.

- **Method `require_auth(self, path: str, excluded_paths: List[str]) -> bool`:**
    - Returns `True` if `path` is `None`
    - Returns `True` if `excluded_paths` is `None` or empty
    - Returns `False` if `path` is in `excluded_paths`
    - Slash tolerant: `path=/api/v1/status` and `path=/api/v1/status/` should return `False` if `excluded_paths` contains `/api/v1/status/`

### 5. Request Validation

Secure the API by validating all requests.

- **Update Method `authorization_header(self, request=None) -> str` in `api/v1/auth/auth.py`:**
    - Returns `None` if `request` is `None`
    - Returns `None` if `request` doesn’t contain the header key `Authorization`
    - Otherwise, returns the value of the header request `Authorization`

- **Update `api/v1/app.py`:**
    - Create a variable `auth` initialized to `None` after the CORS definition
    - Based on the environment variable `AUTH_TYPE`, load and assign the right instance of authentication to `auth`
    - Use Flask's `before_request` method to filter each request.

### 6. Basic Auth

Create a class `BasicAuth` that inherits from `Auth`.

- **Update `api/v1/app.py`:**
    - Use `BasicAuth` class instead of `Auth` depending on the value of the environment variable `AUTH_TYPE`.
    - If `AUTH_TYPE` is equal to `basic_auth`, create an instance of `BasicAuth` and assign it to the variable `auth`.

### 7. Basic - Base64 Part

Add the method `extract_base64_authorization_header` in the class `BasicAuth`.

- **Method `extract_base64_authorization_header(self, authorization_header: str) -> str`:**
    - Returns `None` if `authorization_header` is `None`
    - Returns `None` if `authorization_header` is not a string
    - Returns `None` if `authorization_header` doesn’t start by `Basic` (with a space at the end)
    - Otherwise, returns the value after `Basic` (after the space)

### 8. Basic - Base64 Decode

Add the method `decode_base64_authorization_header` in the class `BasicAuth`.

- **Method `decode_base64_authorization_header(self, base64_authorization_header: str) -> str`:**
    - Returns `None` if `base64_authorization_header` is `None`
    - Returns `None` if `base64_authorization_header` is not a string
    - Returns `None` if `base64_authorization_header` is not a valid Base64
    - Otherwise, returns the decoded value as UTF8 string

### 9. Basic - User Credentials

Add the method `extract_user_credentials` in the class `BasicAuth`.

- **Method `extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str)`:**
    - Returns `None, None` if `decoded_base64_authorization_header` is `None`
    - Returns `None, None` if `decoded_base64_authorization_header` is not a string
    - Returns `None, None` if `decoded_base64_authorization_header` doesn’t contain `:`
    - Otherwise, returns the user email and the user password separated by `:`

### 10. Basic - User Object

Add the method `user_object_from_credentials` in the class `BasicAuth`.

- **Method `user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User')`:**
    - Returns `None` if `user_email` is `None` or not a string
    - Returns `None` if `user_pwd` is `None` or not a string
    - Returns `None` if the database doesn’t contain any `User` instance with email equal to `user_email`
    - Returns `None` if `user_pwd` is not the password of the `User` instance found
    - Otherwise, returns the `User` instance
