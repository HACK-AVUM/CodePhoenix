#!/bin/bash

# Start SonarQube
$SONARQUBE_HOME/bin/linux-x86-64/sonar.sh start

# Wait for SonarQube to start (optional, you might need to tweak the sleep time)
sleep 30

# Start the Python application
python3 src/main.py