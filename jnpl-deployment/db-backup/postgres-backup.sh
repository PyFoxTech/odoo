#!/bin/bash

if [ "$#" -ne 1 ]
then
  echo "Usage: ./postgres-backup.sh HOURLY|DAILY|WEEKLY|MONTHLY"
  exit 1
fi

HOME=/home/rclone
prefix=$1
rclone_config_name="odoo_db_backup_s3"
bucket_name="jnpl-odoo-prod-postgres-backups"
db_name="odoo"

printf -v date '%(%Y/%m/%d)T' -1
printf -v timestamp '%(%Y-%m-%d-%H:%M:%S)T' -1

output_dir="$HOME/postgres-backup/$prefix/$date"
output_filepath="$output_dir/$db_name-backup-$timestamp.sql.gz"

rm -rf $HOME/postgres-backup
mkdir -p $output_dir

pg_dump odoo -U odoo13 -h localhost | gzip > "$output_filepath"

rclone --config $HOME/.config/rclone/rclone.conf copy $HOME/postgres-backup/ "$rclone_config_name:$bucket_name" --progress
