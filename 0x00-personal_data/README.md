# alx-backend-user-data

## Table of Contents
1. [Description](#description)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Tasks](#tasks)
    1. [Task 0: Regex-ing](#task-0-regex-ing)
    2. [Task 1: Log Formatter](#task-1-log-formatter)
    3. [Task 2: Create Logger](#task-2-create-logger)
    4. [Task 3: Connect to Secure Database](#task-3-connect-to-secure-database)
    5. [Task 4: Read and Filter Data](#task-4-read-and-filter-data)
    6. [Task 5: Encrypting Passwords](#task-5-encrypting-passwords)
    7. [Task 6: Check Valid Password](#task-6-check-valid-password)

## Description
This project is aimed at handling personal data securely. It involves filtering sensitive information from logs, creating secure loggers, connecting to a secure database, and managing user passwords safely using encryption.

## Requirements
- Python 3.8+
- `re` module for regex operations
- `logging` module for creating loggers
- `mysql-connector-python` for connecting to MySQL databases
- `bcrypt` for hashing and validating passwords

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alx-backend-user-data.git
   cd alx-backend-user-data/0x00-personal_data
   ```

2. Install the required Python packages:
   ```bash
   pip install mysql-connector-python bcrypt
   ```

## Usage
Each task can be tested by running the provided `main.py` file in the respective directory.

## Tasks

### Task 0: Regex-ing
Write a function `filter_datum` to obfuscate sensitive fields in log messages.

**File:** `filtered_logger.py`

**Usage:**
```python
fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
```

**Expected Output:**
```
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
```

### Task 1: Log Formatter
Create a `RedactingFormatter` class to format log records, filtering out sensitive fields.

**File:** `filtered_logger.py`

**Usage:**
```python
import logging

message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))
```

**Expected Output:**
```
[HOLBERTON] my_logger INFO 2019-11-19 18:24:25,105: name=Bob; email=***; ssn=***; password=***;
```

### Task 2: Create Logger
Implement `get_logger` to create a logger with `RedactingFormatter` and define PII fields.

**File:** `filtered_logger.py`

**Usage:**
```python
import logging

get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS

print(get_logger.__annotations__.get('return'))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))
```

**Expected Output:**
```
<class 'logging.Logger'>
PII_FIELDS: 5
```

### Task 3: Connect to Secure Database
Implement `get_db` to connect to a secure MySQL database using environment variables for credentials.

**File:** `filtered_logger.py`

**Usage:**
```python
get_db = __import__('filtered_logger').get_db

db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()
```

**Expected Output:**
```
2
```

### Task 4: Read and Filter Data
Implement `main` to retrieve and display rows from the `users` table, filtering sensitive fields.

**File:** `filtered_logger.py`

**Usage:**
```bash
PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
```

**Expected Output:**
```
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,621: name=***; email=***; phone=***; ssn=***; password=***; ip=f724:c5d1:a14d:c4c5:bae2:9457:3769:1969; last_login=2019-11-14 06:16:19; user_agent=Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;
```

### Task 5: Encrypting Passwords
Implement `hash_password` to hash and salt user passwords using bcrypt.

**File:** `encrypt_password.py`

**Usage:**
```python
hash_password = __import__('encrypt_password').hash_password

password = "MyAmazingPassw0rd"
print(hash_password(password))
print(hash_password(password))
```

**Expected Output:**
```
b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
b'$2b$12$xSAw.bxfSTAlIBglPMXeL.SJnzme3Gm0E7eOEKOVV2OhqOakyUN5m'
```

### Task 6: Check Valid Password
Implement `is_valid` to validate if a provided password matches the hashed password.

**File:** `encrypt_password.py`

**Usage:**
```python
hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))
```

**Expected Output:**
```
b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
True
```
