#!/bin/bash

PATH="/opt/odoo/odoo/venv/bin:$PATH";

python3 /opt/odoo/odoo/odoo-bin -c /etc/odoo.conf --dev xml --log-level=debug
