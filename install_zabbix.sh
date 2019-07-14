#!/bin/bash

# Change these settings
MYSQL_ROOT_PASSWORD="changeme123A*"
ZABBIX_DB_USER_PASSWORD="changeMeAgain123*"
SERVER_IP="10.28.8.70"


# Deploy a mysql container for zabbix to use.
docker run -d \
  --name="zabbix-mysql-database" \
  --restart=always \
  -p 3306:3306 \
  -e MYSQL_DATABASE=zabbix \
  -e MYSQL_USER=zabbix \
  -e MYSQL_PASSWORD=$ZABBIX_DB_USER_PASSWORD \
  -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD \
  -v $HOME/volumes/mysql:/var/lib/mysql \
  mysql:5.7

# Deploy the zabbix-server application container
docker run -d \
  --name zabbix-server \
  --restart=always \
  -e DB_SERVER_HOST=$SERVER_IP \
  -e MYSQL_USER="zabbix" \
  -e MYSQL_PASSWORD=$ZABBIX_DB_USER_PASSWORD \
  -v $HOME/volumes/zabbix/alertscripts:/usr/lib/zabbix/alertscripts \
  -v $HOME/volumes/zabbix/externalscripts:/usr/lib/zabbix/externalscripts \
  -v $HOME/volumes/zabbix/modules:/var/lib/zabbix/modules \
  -v $HOME/volumes/zabbix/enc:/var/lib/zabbix/enc \
  -v $HOME/volumes/zabbix/ssh_keys:/var/lib/zabbix/ssh_keys \
  -v $HOME/volumes/zabbix/ssl/certs:/var/lib/zabbix/ssl/certs \
  -v $HOME/volumes/zabbix/ssl/keys:/var/lib/zabbix/ssl/keys \
  -v $HOME/volumes/zabbix/ssl_ca:/var/lib/zabbix/ssl/ssl_ca \
  -v $HOME/volumes/zabbix/snmptraps:/var/lib/zabbix/snmptraps \
  -v $HOME/volumes/zabbix/mibs:/var/lib/zabbix/mibs \
  -p 10050:10050 \
  -p 10051:10051 \
  zabbix/zabbix-server-mysql:ubuntu-3.4-latest

# Deploy the webserver frontend.
docker run -d \
  --name zabbix-web-nginx \
  --restart=always \
  -e DB_SERVER_HOST="$SERVER_IP" \
  -e MYSQL_USER="zabbix" \
  -e MYSQL_PASSWORD=$ZABBIX_DB_USER_PASSWORD \
  -e ZBX_SERVER_HOST=$SERVER_IP \
  -e PHP_TZ="UTC" \
  -p 80:80 \
  -p443:443 \
  zabbix/zabbix-web-nginx-mysql:ubuntu-3.4-latest
