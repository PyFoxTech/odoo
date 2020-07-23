#!/bin/bash
cd /opt/odoo/odoo;

git pull origin JNPL-13.0:JNPL-13.0;

PATH="/opt/odoo/odoo/venv/bin:$PATH";

pip install -r requirements.txt;
pip install -r requirements-3rd-party.txt;
pip install -r requirements-dev.txt;
pip install -r requirements-jnpl.txt;

pkill -F /tmp/odoo-13.pid
