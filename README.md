# Spy Cat Management Application

## Overview

The Spy Cat Management Application is a CRUD system designed for the Spy Cat Agency (SCA) to streamline their espionage operations. This application allows users to manage spy cats, the missions they undertake, and the targets assigned to each mission. The application utilizes Django REST Framework for building RESTful APIs and integrates with SQL-like databases for data management.

## Features

- Create, read, update, and delete (CRUD) operations for managing:
  - **Cats**: Register new spy cats and view their details.
  - **Missions**: Create and manage missions assigned to cats.
  - **Targets**: Automatically create targets when a mission is created, and manage their notes and completion status.

## Requirements

- Python 3.x
- Django
- Django REST Framework
- SQL-like database (e.g., SQLite, PostgreSQL)

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <https://github.com/valkorostyslav/spy_cat_agency>
   cd spy-cat-management
   
2. **Install dependencies:**
   pip install -r requirements.txt

3. **Run migrations:**
  python manage.py migrate

4.**Create a superuser (optional):**
  python manage.py createsuperuser

5. **Run the development server:**
  python manage.py runserver

6. **Access the API at http://127.0.0.1:8000/api/.**

## API Endpoints

### Cats
- **Create a Cat**: `POST /api/cats/`
- **List Cats**: `GET /api/cats/`
- **Retrieve a Cat**: `GET /api/cats/{id}/`
- **Update a Cat**: `PUT /api/cats/{id}/`
- **Delete a Cat**: `DELETE /api/cats/{id}/`

### Missions
- **Create a Mission**: `POST /api/missions/`
- **List Missions**: `GET /api/missions/`
- **Retrieve a Mission**: `GET /api/missions/{id}/`
- **Update a Mission**: `PUT /api/missions/{id}/`
- **Delete a Mission**: `DELETE /api/missions/{id}/`

### Targets
Targets are automatically created with missions and do not have dedicated API endpoints for individual management.





