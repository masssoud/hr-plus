# HR Plus
HR Plus is a web application for HR purposes

## Env Files
* Inside the root directory copy `.env.example` file and name it `.env`. Then complete the data before running the project.
* Inside the panel directory copy `.env.example` file and name it `.env`. Then complete the data before running the project.

##  Superuser
To create superuser run `docker-compose run app python manage.py createsuperuser`.

## Run the Project for Development
Run `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up`
<br><br>
The panel is accessible through http://localhost:8080 and the apis are accessible through http://localhost:8888

## Run the Project for Production
Run `docker-compose -f docker-compose.yml -f docker-compose.prod.yml up`
<br><br>
The panel is accessible through http://localhost:8888/panel/ and the apis are accessible through http://localhost:8888
<br><br>
___Be careful as the production docker-compose file may not be optimized for production!___
