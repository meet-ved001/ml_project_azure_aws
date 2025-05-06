#!/bin/bash

# Create a virtual environment
python -m venv venv
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Create deployment package
mkdir -p deploy
cp -r application.py requirements.txt Procfile .ebextensions deploy/
cp -r src deploy/
cp -r static deploy/
cp -r templates deploy/
cp -r artifacts deploy/

# Initialize EB (only needed first time)
# eb init -p python-3.8 student-performance-predictor

# Create environment and deploy
cd deploy
eb deploy student-performance-predictor-env 