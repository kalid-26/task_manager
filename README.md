# Django Task Manager

A production-style Django application with:

## Features

- User authentication (login/register)
- Task CRUD operations
- Profile with image upload
- Search & filtering

## Tech Stack

- Django
- Django REST Framework
- Bootstrap
- SQLite (dev)

## Setup

```bash
# Clone repository
git clone https://github.com/kalid-26/task_manager.git
cd task_manager

# Create virtual environment
python -m venv .venv

# Activate virtual environment 
# Windows
.venv\Scripts\activate

# Linux / Mac 
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver