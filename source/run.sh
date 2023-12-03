#!/bin/sh
cd /app/
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
#for fixture in auth.json dump.json; do
#  python manage.py loaddata fixtures/$$fixture
#done
python manage.py runserver 0.0.0.0:8000