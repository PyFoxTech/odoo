#### Steps for Deployment
You need to create a user called `rclone`

```bash
sudo useradd -m -d /home/rclone -s /bin/bash rclone
```

Source code odoo should be at `/opt/odoo/odoo`
```bash
sudo su odoo;
git clone git@github.com:PyFoxTech/odoo.git /opt/odoo/odoo;
```

##### Setup pyenv
```bash
sudo su odoo;

pyenv install 3.8.2;
pyenv global 3.8.2;

cd /opt/odoo/odoo;

python3.8 -m venv /opt/odoo/odoo/venv;

source /opt/odoo/odoo/venv/bin/activate;

pip install -r requirements.txt;
pip install -r requirements-3rd-party.txt;
pip install -r requirements-dev.txt;
pip install -r requirements-jnpl.txt;
```

<!-- ##### Enable `odoo.service`
```bash
sudo su odoo;
systemctl --user enable --now /opt/odoo/odoo/jnpl-deployment/systemd/odoo.service;
``` -->

##### Enable `odoo.conf` in supervisor
```bash
sudo ln -sf /opt/odoo/odoo/jnpl-deployment/supervisor/odoo.conf /etc/supervisor/conf.d/
```