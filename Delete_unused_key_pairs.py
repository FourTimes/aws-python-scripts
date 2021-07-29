#!/usr/bin/env python

import boto3
sess = boto3.Session(
  aws_access_key_id='MYAWSACCESSKEYID',
  aws_secret_access_key='MYSECRETACCESSKEY',
  region_name='us-east-1'
)

# Creating lists for all, used, and unused key pairs
all_key_pairs = []
all_used_key_pairs = []
all_unused_key_pairs = []


# List all key pairs in the account
ec2 = sess.client('ec2')
all_key_pairs = list(map(lambda i: i['KeyName'], ec2.describe_key_pairs()['KeyPairs']))

# Each EC2 reservation returns a group of instances. 
instance_groups = list(map(lambda i: i['Instances'], ec2.describe_instances()['Reservations']))

# Create a list of all used key pairs in the account based on the running instances
for group in instance_groups:
  for i in group: 
    if i['KeyName'] not in all_used_key_pairs:
      all_used_key_pairs.append(i['KeyName'])

# Now compare the two lists
for key in all_key_pairs:
  if key not in all_used_key_pairs:
    all_unused_key_pairs.append(key)

print('Keeping used key pairs: {}'.format(all_used_key_pairs))

# Delete all unused key pairs
print('Deleting unused key pairs:')
for key in all_unused_key_pairs: 
  print(key)
  ec2.delete_key_pair(KeyName=key)

