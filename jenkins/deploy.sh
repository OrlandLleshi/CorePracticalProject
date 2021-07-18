#!/bin/bash 

scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@flask:/home/Orland/CorePracticalProject/CorePracticalProject/docker-compose.yaml 

ssh -i ~/.ssh/ansible_id_rsa jenkins@flask << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file docker-compose.yaml project 

EOF