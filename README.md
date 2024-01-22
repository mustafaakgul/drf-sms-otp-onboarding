# Django DRF OTP Onboarding
Project for onboarding via sms

## Running with Docker
* docker-compose -f docker-compose.dev.yml up --build
* docker exec -it <container_name> pytest user/tests/test_auth.py -k "verify_account" -rP -vv

## Running locally
* Create a .env file by copying the .env.sample provided and run: cp .env.sample .env
* Docker: docker compose build && docker compose up OR
* Classical:
* python3.12 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver

## Run tests
* Run descriptive tests in the container using:
* docker compose exec <docker_container_name> pytest -rP -vv
* Access the docs on: http://localhost:8000/api/v1/doc
* http://localhost:8000/admin
* http://localhost:15672/#/queues
* https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1
* http://127.0.0.1:8000/api/schema/
* http://127.0.0.1:8000/api/v1/doc/#/auth/auth_change_password_create
* http://127.0.0.1:8000/api/v1/redoc/#tag/auth/operation/auth_login_create

## Tools and Services
Django & DRF : for building the APIs
Docker & Docker compose: Containerization
Celery: For running background task
Rabbit MQ: A message broker for celery
Flower dashboard: For monitoring celery background tasks
PostgreSQL: Relational DB
Twilio: SMS notifications

## By the end of this tutorial
Onboard a user on the system via phone number verification
Reset user password via OTP sent to user.
Authenticate a user using phone number and password
