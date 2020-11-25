#!/bin/bash

# Git repo location
repo_root="/root/ANB_Repo/ANB" #replace with the root of your ANB Git repository

trap 'echo "# $BASH_COMMAND"' DEBUG
#Install base requirements
apt-get install python3-pip python3-virtualenv python3-setuptools python3-dev build-essential python3 nginx-light gunicorn

mkdir -p /opt/contacts_proj/
mkdir -p /opt/contacts_proj/venv && cd /opt/contacts_proj/venv
mkdir /opt/contacts_proj/venv/scripts
virtualenv -p python3 .
useradd -p --system --home-dir=/var/opt/contacts_proj --no-create-home --shell=/bin/bash DDjUser
mkdir -p /var/opt/contacts_proj
mkdir -p /var/log/contacts_proj
chown DDjUser /var/log/contacts_proj
mkdir -p /etc/opt/contacts_proj
mkdir -p /var/cache/contacts_proj/static
mkdir -p /var/opt/contacts_proj/media
chown DDjUser /var/opt/contacts_proj/media
chown DDjUser /var/cache/contacts_proj/static/

#Place config files
cp -r ""$repo_root/conf/contacts_proj /etc/opt/
cp ""$repo_root/conf/nginx/* /etc/nginx/sites-available/
cp ""$repo_root/conf/gunicorn/* /etc/systemd/system/
chgrp DDjUser /etc/opt/contacts_proj
chmod u=rwx,g=rx,o= /etc/opt/contacts_proj

#Place script files
cp ""$repo_root/scripts/* /opt/contacts_proj/venv/scripts

#Place webapp files
cp -r ""$repo_root/webapp/contacts_proj /var/opt/
chown DDjUser /var/opt/contacts_proj


cd /opt/contacts_proj/venv
source bin/activate


trap - DEBUG
