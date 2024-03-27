#!/bin/bash
echo "****************************************"
echo " Setting up BDD Environment"
echo "****************************************"

echo "Making Python 3.8 the default..."
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1

echo "Checking the Python version..."
python --version

echo "Configuring the developer environment..."
echo "# BDD Lab Additions" >> ~/.bashrc
echo 'export PS1="\[\e]0;\u:\W\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ "' >> ~/.bashrc
echo "export PATH=$HOME/local/bin:$PATH" >> ~/.bashrc

echo "Installing Selenium and Chrome for BDD"
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y sqlite3 python3-selenium

echo "Starting the Postgres Docker container..."
make app

echo "Checking the Postgres Docker container..."
docker ps

echo "****************************************"
echo " BDD/TDD Environment Setup Complete"
echo "****************************************"
echo ""
