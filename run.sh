#!/bin/bash

# Activate anaconda environment
echo 'Activating conda environment...'
source /opt/conda/etc/profile.d/conda.sh && \
conda activate ops-api && \
# Create django project
cd /usr/project/met_forecast/src/ && \
django-admin startproject api && \
# Create app
cd /usr/project/met_forecast/src/api && \
python manage.py startapp app