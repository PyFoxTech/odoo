### How to run the script
##### Prerequisites
During development, you should create a spearate config file for odoo, e.g. `/etc/odoo-shell.conf`, which would get used for odoo shell and scripts. In this you can remove Sentry related config to avoid spamming your mailbox with error notifications during development.

##### Install `odoo` to virtualenv as Python package for easy import in scripts
```
cd /opt/odoo/odoo
source /opt/odoo/odoo/venv/bin/activate
python setup.py develop
```

##### Run the script
```bash
cd /opt/odoo/odoo
source /opt/odoo/odoo/venv/bin/activate
python3.8 jnpl-scripts/fix_product_prices.py -c /etc/odoo-shell.conf -d odoo
```
