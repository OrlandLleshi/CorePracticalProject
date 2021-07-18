#!/bin/bash

sudo apt-get update
sudo apt-get install python3-venv python3-pip -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

cd service1
python 3 -m pytest --cov=application
cd ..

cd character
python 3 -m pytest --cov=application
cd ..

cd background
python 3 -m pytest --cov=application
cd ..

cd endpoint
python 3 -m pytest --cov=application
cd ..
