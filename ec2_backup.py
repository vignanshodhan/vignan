#!/usr/bin/env python3
"""Simple EC2 backup script.

Creates an AMI of a specified EC2 instance. The instance ID is read from the
EC2_INSTANCE_ID environment variable. The AWS region defaults to ``us-east-1``
unless ``AWS_REGION`` is set.

This script can be scheduled with cron or a similar tool to run daily.
"""

import os
from datetime import datetime

import boto3


INSTANCE_ID = os.environ.get("EC2_INSTANCE_ID")
REGION = os.environ.get("AWS_REGION", "us-east-1")


def create_instance_backup(instance_id: str) -> None:
    """Create an AMI from the provided EC2 instance."""
    ec2 = boto3.client("ec2", region_name=REGION)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
    name = f"backup-{instance_id}-{timestamp}"
    response = ec2.create_image(InstanceId=instance_id, Name=name, NoReboot=True)
    image_id = response.get("ImageId")
    print(f"Created AMI {image_id} named {name}")


def main() -> None:
    instance_id = INSTANCE_ID
    if not instance_id:
        raise ValueError("EC2_INSTANCE_ID environment variable not set")
    create_instance_backup(instance_id)


if __name__ == "__main__":
    main()
