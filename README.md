# vignan

This repository contains miscellaneous files and a simple script for backing up
an EC2 instance.

## EC2 Backup Script

`ec2_backup.py` creates an Amazon Machine Image (AMI) from a specified EC2
instance. The instance ID is read from the `EC2_INSTANCE_ID` environment
variable. The AWS region defaults to `us-east-1` but can be overridden with the
`AWS_REGION` environment variable.

Run the script directly or schedule it with cron (or a similar tool) to create a
backup once per day:

```bash
0 2 * * * /usr/bin/python3 /path/to/repo/ec2_backup.py >> /var/log/ec2_backup.log 2>&1
```

