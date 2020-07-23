#!/bin/bash

PATH="/opt/odoo/odoo/venv/bin:$PATH";

python3 /opt/odoo/odoo/odoo-bin -c /etc/odoo.conf --log-level=debug
