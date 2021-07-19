#!/bin/bash

sudo apt update 
sudo apt install software-properties-common -y
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
cd ansible 
ansible-playbook -i inventory.yaml playbook.yaml
cd ..