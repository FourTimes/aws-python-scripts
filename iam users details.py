#!/usr/bin/env python3
import datetime
import sys
import boto3

# Age should be 90 days old
age = 90

login = boto3.Session(
  aws_access_key_id="xxxxxxxxx",
  aws_secret_access_key="xxxxx",
  region_name="ap-south-1",
)
iam = login.client('iam')

users = iam.list_users()
for user in users['Users']:
    for key,values in user.items():
        if key == 'PasswordLastUsed':
            print("UserName: {0}\nCreateDate: {1}\nPasswordUsed: {2}\n"
            .format(user['UserName'], user['CreateDate'], user['PasswordLastUsed'].strip()))
