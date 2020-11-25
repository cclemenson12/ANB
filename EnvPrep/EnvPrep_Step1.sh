#!/bin/bash

# Git repo location
repo_root="~/ANB_Repo" #replace with the root of your ANB Git repository

trap 'echo "# $BASH_COMMAND"' DEBUG
mkdir -p /opt/contacts_proj/
mkdir -p /opt/contacts_proj/venv && cd /opt/contacts_proj/venv
virtualenv -p python3 .
useradd -p --system --home-dir=/var/opt/contacts_proj --no-create-home --shell=/bin/bash DDjUser
mkdir -p /var/opt/contacts_proj
chown DDjUser /var/opt/contacts_proj
mkdir -p /var/log/contacts_proj
chown DDjUser /var/log/contacts_proj
mkdir -p /etc/opt/contacts_proj
mkdir -p /var/cache/contacts_proj/static
mkdir -p /var/opt/contacts_proj/media
chown DDjUser /var/opt/contacts_proj/media
chown DDjUser /var/cache/contacts_proj/static/

trap - DEBUG
