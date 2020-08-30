#!/bin/bash

if [ "$#" -ne 1 ]
then
  echo "Usage: ./restore-db.sh /path/to/dump.sql"
  exit 1
fi

sudo supervisorctl stop odoo13;
pkill -F /tmp/odoo-13.pid;

dropdb odoo;
createdb odoo -O odoo13;

psql -d odoo < "$1";

sudo supervisorctl start odoo13;
