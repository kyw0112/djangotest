# setup_windows.ps1 - helper script to run project on Windows
# 1. create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. install dependencies
pip install -r requirements.txt

# 3. run PostgreSQL and Redis containers via docker
docker run --name pg -e POSTGRES_DB=myproject -e POSTGRES_USER=myproject -e POSTGRES_PASSWORD=myproject -p 5432:5432 -d postgres:16
docker run --name redis -p 6379:6379 -d redis:7

# 4. set environment variables
$env:POSTGRES_DB = 'myproject'
$env:POSTGRES_USER = 'myproject'
$env:POSTGRES_PASSWORD = 'myproject'
$env:POSTGRES_HOST = 'localhost'
$env:POSTGRES_PORT = '5432'
$env:REDIS_URL = 'redis://127.0.0.1:6379/1'
$env:DJANGO_SECRET_KEY = 'change-me'
$env:DJANGO_DEBUG = 'True'
$env:DJANGO_ALLOWED_HOSTS = 'localhost,127.0.0.1'

# 5. run migrations and start the development server
python manage.py migrate
python manage.py runserver
