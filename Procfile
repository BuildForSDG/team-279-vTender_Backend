web: python manage.py runserver --host 0.0.0.0 --port ${PORT}
release: python manage.py db migrate
release: python manage.py db upgrade


web: gunicorn manage:app
worker: python -u manage.py run_worker
