#!/bin/bash

if [ "$#" -ne 1 ]
then
  echo "Usage: ./restore-db.sh /path/to/dump.sql"
  exit 1
fi

systemctl --user stop odoo.service;

dropdb odoo;
createdb odoo -O odoo13;

psql -d odoo < "$1";

systemctl --user start odoo.service;