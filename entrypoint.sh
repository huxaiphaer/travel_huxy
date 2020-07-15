#Run migrations
flask db init
flask db migrate
flask db upgrade

# Run Celery worker
celery -A app.tasks.weather_tasks.celery worker -l info &

# Run Celery beat
celery -A app.tasks.weather_tasks.celery beat -l info &

python run.py celerybeat --pidfile= --schedule=/var/travel_huxy/celerybeat-schedule