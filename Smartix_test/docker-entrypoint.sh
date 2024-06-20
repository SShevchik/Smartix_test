#!/usr/bin/env bash

sleep 30

python3 ./manage.py migrate

python3 ./manage.py runserver 0:8000