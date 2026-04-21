# Django Task Manager

A production-style Django application with:

## Features

- User authentication (login/register)
- Task CRUD operations
- Profile with image upload
- Search & filtering
- Pagination
- REST API (Django REST Framework)
- JWT Authentication

## Tech Stack

- Django
- Django REST Framework
- Bootstrap
- SQLite (dev)

## Setup

```bash
git clone https://github.com/kalid-26/task_manager.git

cd project

python -m venv .venv

.venv\Scripts\activate # or  source .venv/bin/activate 

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver