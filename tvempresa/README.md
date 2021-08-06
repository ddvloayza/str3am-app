# Dockerized Django
Sample project on how to dockerize your Django project in development and production environments.
Take it from https://github.com/nicholaskajoh/dockerized-django

## Requirements
- Docker
- Docker Compose

## Development
- Clone project
- Create *.env* and *.env.secret* from the example files in the root folder and edit as appropriate
- Run `docker-compose up`
- Visit localhost:8000

## Production
- Follow the first 2 steps outlined above
- Run `docker-compose -f docker-compose.prod.yml up --build -d`
- Run `docker-compose -f docker-compose.prod.yml run web python manage.py migrate`
- Run `docker-compose -f docker-compose.prod.yml run web python manage.py collectstatic --noinput`
- Visit website


## Common commands local
- create app
    ```
    docker-compose exec web /bin/sh -c "cd ./src/apps  && python ../manage.py startapp user"
    ```
- migrate
    ```
    docker-compose exec web /bin/sh -c "python src/manage.py migrate"
    ```
- create superuser
    ```
    docker-compose exec web /bin/sh -c "python src/manage.py createsuperuser"
    ```