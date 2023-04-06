#!/bin/bash
echo "****************************************"
echo " Setting up BDD Environment"
echo "****************************************"

echo "Making Python 3.8 the default..."
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

echo "Checking the Python version..."
python3 --version

echo "Installing Selenium and Chrome for BDD"
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y sqlite3 chromium-driver python3-selenium

echo "Starting the Postgres Docker container..."
make app

echo "Checking the Postgres Docker container..."
docker ps

echo "****************************************"
echo " BDD/TDD Environment Setup Complete"
echo "****************************************"
echo ""
