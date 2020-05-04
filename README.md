# HR Plus
HR Plus is a web application for HR purposes

## Env Files
* Inside the root directory copy `.env.example` file and name it `.env`. Then complete the data before running the project.
* Inside the panel directory copy `.env.example` file and name it `.env`. Then complete the data before running the project.

## Migrations
To run the migrations run `docker-compose run app python manage.py migrate`.

## Superuser
To create superuser run `docker-compose run app python manage.py createsuperuser`.

## Do This the First Time
Run the following command `docker-compose run app python manage.py collectstatic` once to publish static files.

## Translations
Run the following command `docker-compose run app python manage.py compilemessages -l fa_IR` for translations.

## Run the Project for Development
1. Run `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up`.
2. Run `docker-compose run panel npm install` to  install panel packages.
3. Then run `docker-compose run --service-ports panel npm run serve` for panel.

The panel is accessible through http://localhost:8080 and the apis are accessible through http://localhost:8888

## Run the Project for Production
1. Run `docker-compose -f docker-compose.yml -f docker-compose.prod.yml up`.
2. Run `docker-compose run panel npm install` to  install panel packages.
3. Then run `docker-compose run panel npm run build` to build the panel.

The panel is accessible through http://localhost:8888/panel/ and the APIs are accessible through http://localhost:8888
<br><br>
___Be careful as the production docker-compose file may not be optimized for production!___
