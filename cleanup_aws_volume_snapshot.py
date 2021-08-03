#!/usr/bin/env python3

import datetime
import sys
import boto3

# Age should be 90 days old
age = 90

login = boto3.Session(
  aws_access_key_id="xxxxx",
  aws_secret_access_key="xxxxxx",
  region_name="ap-south-1",
)

def days_old(date):
    date_obj = date.replace(tzinfo=None)
    diff = datetime.datetime.now() - date_obj
    return diff.days

ec2 = login.client('ec2')
amis = ec2.describe_snapshots(OwnerIds=[
        'self'
        ])

for ami in amis['Snapshots']:
    create_date = ami['StartTime']
    snapshot_id = ami['SnapshotId']
    day_old = days_old(create_date)
    if day_old > age:
        try:
            print("deleting -> " + snapshot_id + " as image is " + str(day_old)  + " old.")
            # delete the snapshot
            # ec2.delete_snapshot(SnapshotId=snapshot_id)
        except:
            print("can't delete " + snapshot_id)
