#!/bin/bash
apt-get update -y
apt-get install git -y
apt-get install python3 -y
cd /home/ubuntu/
TOKEN="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"
git clone https://TOKEN@github.com/AYSEOTKUN/my-aws-apstone-project
cd /home/ubuntu/my-aws-apstone-project
apt install python3-pip -y
apt-get install python3.7-dev libmysqlclient-dev -y
pip3 install -r requirements.txt
cd /home/ubuntu/my-aws-apstone-project/src
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:80