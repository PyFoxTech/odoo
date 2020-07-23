#!/bin/bash

PATH="/opt/odoo/odoo/venv/bin:$PATH";

python3 /opt/odoo/odoo/odoo-bin shell -c /etc/odoo-shell.conf -d odoo;
