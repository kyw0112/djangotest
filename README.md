# Django Test Project

This repository contains a minimal Django project configured to use PostgreSQL and Redis.


## Prerequisites

- Python 3.12+
- [pip](https://pip.pypa.io/)
- [Docker](https://www.docker.com/) (for running PostgreSQL and Redis containers)

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd djangotest
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run PostgreSQL and Redis using Docker** (optional but recommended)

   ```bash
   docker run --name pg -e POSTGRES_DB=myproject -e POSTGRES_USER=myproject \
     -e POSTGRES_PASSWORD=myproject -p 5432:5432 -d postgres:16

   docker run --name redis -p 6379:6379 -d redis:7
   ```

5. **Configure environment variables**

   The project reads the following variables with defaults shown below:

   ```bash
   export POSTGRES_DB=myproject
   export POSTGRES_USER=myproject
   export POSTGRES_PASSWORD=myproject
   export POSTGRES_HOST=localhost
   export POSTGRES_PORT=5432
   export REDIS_URL=redis://127.0.0.1:6379/1
   export DJANGO_SECRET_KEY=change-me
   export DJANGO_DEBUG=True
   export DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   ```

6. **Run migrations and start the development server**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```


Windows users can run `setup_windows.ps1` to perform the above steps automatically.
Visit `http://127.0.0.1:8000/` to see the default Django page.
Swagger documentation is available at `http://127.0.0.1:8000/swagger/`.

## Requirements File

`requirements.txt` includes core dependencies:

- Django
- psycopg2-binary (PostgreSQL driver)
- django-redis
- djangorestframework
- drf-yasg (Swagger UI)

Install them with `pip install -r requirements.txt` as shown above.

## License

This project is provided as-is for demonstration purposes.
