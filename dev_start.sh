#!/bin/bash

sleep 60

python manage.py migrate

source load_all_fixtures.sh

python manage.py runserver 0.0.0.0:8000