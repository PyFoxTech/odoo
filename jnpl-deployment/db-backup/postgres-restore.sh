#!/bin/bash

if [ "$#" -ne 1 ]
then
  echo "Usage: ./postgres-restore.sh <path-to-backup.sql.gz>"
  exit 1
fi

dropdb odoo;
createdb odoo -O odoo13;
gunzip < $1 | psql odoo;
