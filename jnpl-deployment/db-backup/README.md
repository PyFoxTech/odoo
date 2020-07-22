#### Instructions
You need to create a user called `rclone`

```bash
sudo useradd -m -d /home/rclone -s /bin/bash rclone
```

We rely on `~/.pgpass` in `rclone` user's home directory (https://www.postgresql.org/docs/12/libpq-pgpass.html).

You should set correct permissions on the `~/.pgpass` file:
```bash
sudo su rclone
chmod 600 ~/.pgpass
```

You need to create a config file for `rclone` which should be at `~/.config/rclone/rclone.conf`, Look at `jnpl-deployment/db-backup/rclone/rclone.example.conf` for example.

Copy contents of `crontab.txt` and add them to `rclone` user's crontab using `crontab -e`:
```bash
sudo su rclone
crontab -e
```

#### AWS S3 Bucket and IAM policy
We have a S3 bucket called `jnpl-odoo-prod-postgres-backups` and an IAM user with same name.

We have `Block public access (bucket settings)` on for the S3 bucket

IAM user `jnpl-odoo-prod-postgres-backups` has only one policy which is below:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetAccessPoint",
                "s3:PutAccountPublicAccessBlock",
                "s3:GetAccountPublicAccessBlock",
                "s3:ListAllMyBuckets",
                "s3:ListAccessPoints",
                "s3:ListJobs",
                "s3:CreateJob",
                "s3:HeadBucket"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:*:835571947007:job/*",
                "arn:aws:s3:::jnpl-odoo-prod-postgres-backups/*",
                "arn:aws:s3:*:835571947007:accesspoint/*",
                "arn:aws:s3:::jnpl-odoo-prod-postgres-backups"
            ]
        }
    ]
}
```
