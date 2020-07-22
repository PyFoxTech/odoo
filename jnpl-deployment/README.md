#### Steps for Deployment

##### Setup pyenv
```bash
pyenv install 3.8.2
pyenv global 3.8.2

cd /opt/odoo/odoo

python3.8 -m venv /opt/odoo/odoo/venv

source /opt/odoo/odoo/venv/bin/activate

pip install -r requirements.txt
pip install -r requirements-3rd-party.txt
pip install -r requirements-dev.txt
pip install -r requirements-jnpl.txt
```

##### Enable `odoo.service`
```bash
sudo systemctl enable --now /opt/odoo/odoo/jnpl-deployment/systemd/odoo.service
```
