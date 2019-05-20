#!/bin/bash


# Run Django migrations
echo "==> Django setup, executing: migrate"
python ./src/manage.py migrate

# Start the server
echo "==> Starting ..."
python ./src/manage.py runserver 0.0.0.0:8000