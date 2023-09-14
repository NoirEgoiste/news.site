Новостной сайт, в Docker контейнере с бд Postgres, 
Gunicorn и Nginx

#### PROD
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear 

#### DEV
docker-compose up -d --build
