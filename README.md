git clone https://github.com/BSSE23087/test


pip install -r requirements.txt


python manage.py makemigrations


python manage.py migrate


celery -A counter_project worker -l info


celery -A counter_project beat -l info

(remember to adjust the redis server in settings.py)
