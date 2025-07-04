#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Apply any outstanding database migrations
python manage.py migrate

# Convert static asset files
python manage.py collectstatic --no-input

# Migrate CSV data
python manage.py migratefromsheets

# Create superuser
if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input
fi