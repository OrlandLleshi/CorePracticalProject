#!/bin/bash 

scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml Orland@flask:/home/docker-compose.yaml 

ssh -i ~/.ssh/ansible_id_rsa Orland@flask << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file docker-compose.yaml project 

EOF