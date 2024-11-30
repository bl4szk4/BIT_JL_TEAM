include app/config/.env

BACKEND_CONTAINER = web
DB_CONTAINER = db
ENV_FILE := $(if $(filter production,$(ENV)),--env-file ./app/config/.env,)


FIXTURES = fixtures/users.json

build:
	if [ ! -f ./app/config/.env ]; then cp ./app/config/.env.template ./app/config/.env; fi
	docker-compose $(ENV_FILE) build

up:
	docker-compose $(ENV_FILE) up

create-static:
	docker-compose $(ENV_FILE) run --rm $(BACKEND_CONTAINER) python manage.py collectstatic


up-build:
	if [ ! -f ./app/config/.env ]; then cp ./app/config/.env.template ./app/config/.env; fi
	docker-compose $(ENV_FILE) build
	docker-compose $(ENV_FILE) run --rm $(BACKEND_CONTAINER) python manage.py makemigrations
	docker-compose $(ENV_FILE) run --rm $(BACKEND_CONTAINER) python manage.py migrate
	docker-compose $(ENV_FILE) run --rm $(BACKEND_CONTAINER) python manage.py compilemessages
	docker-compose $(ENV_FILE) up

showmigrations:
	docker-compose $(ENV_FILE) exec $(BACKEND_CONTAINER) bash -c "python3 ./manage.py showmigrations"

migrate:
	docker-compose $(ENV_FILE) exec $(BACKEND_CONTAINER) bash -c "python3 ./manage.py migrate"

migrations:
	docker-compose $(ENV_FILE) exec $(BACKEND_CONTAINER) bash -c "python3 ./manage.py makemigrations"
	make migrate

recreate-db:
	docker-compose $(ENV_FILE) stop $(BACKEND_CONTAINER)
	docker-compose $(ENV_FILE) exec $(DB_CONTAINER) bash -c "su - $(POSTGRES_USER) -c 'if psql -lqt | cut -d \| -f 1 | grep -qw $(POSTGRES_DB); then dropdb $(POSTGRES_DB); fi'"
	docker-compose $(ENV_FILE) exec $(DB_CONTAINER) bash -c "su - $(POSTGRES_USER) -c 'createdb $(POSTGRES_DB)'"
	docker-compose $(ENV_FILE) up -d $(BACKEND_CONTAINER)
	docker-compose $(ENV_FILE) exec $(BACKEND_CONTAINER) bash -c "python3 ./manage.py createcachetable"
	make migrations

recreate-db-without-makemigrations:
	docker-compose $(ENV_FILE) stop $(BACKEND_CONTAINER)
	docker-compose $(ENV_FILE) exec $(DB_CONTAINER) bash -c "su - $(POSTGRES_USER) -c 'if psql -lqt | cut -d \| -f 1 | grep -qw $(POSTGRES_DB); then dropdb $(POSTGRES_DB); fi'"
	docker-compose $(ENV_FILE) exec $(DB_CONTAINER) bash -c "su - $(POSTGRES_USER) -c 'createdb $(POSTGRES_DB)'"
	docker-compose $(ENV_FILE) up -d $(BACKEND_CONTAINER)
	docker-compose $(ENV_FILE) exec $(BACKEND_CONTAINER) bash -c "python3 ./manage.py createcachetable"
	make migrate

backend-bash:
	docker-compose $(ENV_FILE) exec $(BACKEND_CONTAINER) bash

django-shell:
	docker-compose $(ENV_FILE) exec $(BACKEND_CONTAINER) bash -c "python3 ./manage.py shell"

format:
	docker-compose $(ENV_FILE) exec $(BACKEND_CONTAINER) bash -c "isort . && black . --line-length 100"

superuser:
	docker-compose $(ENV_FILE) exec $(BACKEND_CONTAINER) bash -c "python3 ./manage.py createsuperuser"

load-fixtures:
	docker-compose $(ENV_FILE) exec $(BACKEND_CONTAINER) bash -c "python3 ./manage.py loaddata $(FIXTURES)"

test:
	docker-compose $(ENV_FILE) exec $(BACKEND_CONTAINER) bash -c "pytest $(location) -W ignore::DeprecationWarning"
