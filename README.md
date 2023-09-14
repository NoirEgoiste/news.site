Новостной сайт, в Docker контейнере с бд Postgres, 
Gunicorn и Nginx

После запуска контейнера с бд выполнить:
docker-compose exec web python manage.py flush --no-input
docker-compose exec web python manage.py migrate 