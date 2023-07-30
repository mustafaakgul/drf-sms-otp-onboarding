# Django DRF OTP Onboarding
Project for onboarding via sms


Running Application
 * docker-compose -f docker-compose.dev.yml up --build
 * docker exec -it <container_name> pytest user/tests/test_auth.py -k "verify_account" -rP -vv

# Running locally
Create a .env file by copying the .env.sample provided and run:
docker compose build && docker compose up
to start the container. As an alternative, run:
docker-compose -f docker-compose.dev.yml up --build
# Run tests
Run descriptive tests in the container using:
docker compose exec <docker_container_name> pytest -rP -vv
Access the docs on:
http://localhost:8000/api/v1/doc

# Tools and Services
Django & DRF : for building the APIs
Docker & Docker compose: Containerization
Celery: For running background task
Rabbit MQ: A message broker for celery
Flower dashboard: For monitoring celery background tasks
PostgreSQL: Relational DB
Twilio: SMS notifications

# By the end of this tutorial
Onboard a user on the system via phone number verification
Reset user password via OTP sent to user.
Authenticate a user using phone number and password

# Running In a Virtual Env
Create a virtual environment using:
mkvirtualenv <env_name>
Ensure you have installed virtualenv on your system and install dev dependencies using
pip install -r app/requirements/dev.txt
Navigate to app directory and run migrations using:
python manage.py makemigrations
python manage.py migrate
Run the server using:
python manage.py runserver
Access docs:
http://localhost:8000/api/v1/doc

http://localhost:8000/admin
http://localhost:15672/#/queues
https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1
http://127.0.0.1:8000/api/schema/
http://127.0.0.1:8000/api/v1/doc/#/auth/auth_change_password_create
http://127.0.0.1:8000/api/v1/redoc/#tag/auth/operation/auth_login_create

ADD LİCENSE