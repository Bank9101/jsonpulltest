#!/bin/bash

# Install dependencies
python3.13 -m pip install -r requirements.txt

# Reset and create database tables
python3.13 manage.py reset_db

# Collect static files
python3.13 manage.py collectstatic --noinput --clear