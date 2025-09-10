#!/bin/bash

# Install dependencies
python -m pip install -r requirements.txt

# Reset and create database tables
python manage.py reset_db

# Collect static files
python manage.py collectstatic --noinput --clear