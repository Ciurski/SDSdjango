web: python SDS/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT SDS/settings.py
release: python manage.py migrate --noinput
web: gunicorn SDS.wsgi
