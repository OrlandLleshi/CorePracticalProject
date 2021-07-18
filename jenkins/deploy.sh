#!/bin/bash 

scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@flask:/home/jenkins/docker-compose.yaml 

ssh -i ~/.ssh/ansible jenkins@flask << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file docker-compose.yaml project 

EOF