# Project Management API

## Overview
This is a **Project Management API** built using Django REST Framework (DRF) with MySQL as the database. It allows authenticated users to manage **Clients** and **Projects**, assign users to projects, and retrieve assigned projects.

## Features
- **User Authentication** (JWT-based)
- **CRUD Operations for Clients**
- **CRUD Operations for Projects**
- **Assign Users to Projects**
- **Retrieve Assigned Projects for a User**

## Technologies Used
- **Django REST Framework**
- **MySQL Database**
- **JWT Authentication**
- **Postman** (for testing API endpoints)

---
## Installation & Setup

### 1. Clone the Repository
```sh
    git clone https://github.com/your-username/project-management-api.git
    cd project-management-api
```

### 2. Install Dependencies
Ensure you have **Python** and **pip** installed, then install dependencies:
```sh
    pip install -r requirements.txt
```

### 3. Configure MySQL Database
Update your **settings.py** with your MySQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Apply Migrations
```sh
    python manage.py makemigrations
    python manage.py migrate
```

### 5. Create Superuser
```sh
    python manage.py createsuperuser
```

### 6. Run the Server
```sh
    python manage.py runserver
```

---
## API Endpoints & Testing with Postman

### Authentication
#### 1. Generate JWT Token
**Endpoint:** `POST /api/login/`
**Body:**
```json
{
    "username": "admin",
    "password": "adminpassword"
}
```
**Response:**
```json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

#### 2. Refresh JWT Token
**Endpoint:** `POST /api/token/refresh/`
**Body:**
```json
{
    "refresh": "<refresh_token>"
}
```
**Response:**
```json
{
    "access": "<new_access_token>"
}
```

---
### Client Management
#### 1. List All Clients
**Endpoint:** `GET /api/clients/`
**Headers:** `Authorization: Bearer <access_token>`

**Response:**
```json
[
    {
        "id": 1,
        "client_name": "Nimap",
        "created_at": "2025-02-03T11:03:55Z",
        "created_by": "Rohit"
    },
    {
        "id": 2,
        "client_name": "Infotech",
        "created_at": "2025-02-03T11:03:55Z",
        "created_by": "Rohit"
    }
]
```

#### 2. Create a New Client
**Endpoint:** `POST /api/clients/register/`
**Body:**
```json
{
    "client_name": "Company A"
}
```
**Response:**
```json
{
    "id": 3,
    "client_name": "Company A",
    "created_at": "2025-02-03T11:03:55Z",
    "created_by": "Rohit"
}
```

#### 3. Retrieve Client Info
**Endpoint:** `GET /api/clients/:id/`

#### 4. Update a Client
**Endpoint:** `PUT /api/clients/:id/`
**Body:**
```json
{
    "client_name": "Updated Company A"
}
```

#### 5. Delete a Client
**Endpoint:** `DELETE /api/clients/:id/`

---
### Project Management
#### 1. Create a New Project
**Endpoint:** `POST /api/projects/add/`
**Body:**
```json
{
    "project_name": "Project A",
    "client_id": 1,
    "users": [1]
}
```

#### 2. Get All Projects Assigned to Logged-in User
**Endpoint:** `GET /api/user/projects/`

**Response:**
```json
[
    {
        "id": 1,
        "project_name": "Project A",
        "client_name": "Client A",
        "created_at": "2025-02-03T11:03:55Z",
        "created_by": "Ganesh"
    }
]
```

---
## Running Tests
To run tests, execute:
```sh
    python manage.py test
```

---
## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m "Add feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---
## License
This project is open-source and available under the **MIT License**.

