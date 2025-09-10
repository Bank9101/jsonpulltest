#!/bin/bash

# Install dependencies
python -m pip install -r requirements.txt

# Create migrations (if needed)
python manage.py makemigrations --noinput

# Apply migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput --clear

# Load OTOP data if needed
if [ -f "staticfiles_build/static/data/otop_data.json" ]; then
    echo "OTOP data file found"
else
    echo "Warning: OTOP data file not found at staticfiles_build/static/data/otop_data.json"
fi