```py


#!/usr/bin/env python

# usage: Finding and deleting unattached EBS volumes

import boto3

sess = boto3.Session(
  aws_access_key_id="MYAWSACCESSKEYID",
  aws_secret_access_key="MYSECRETACCESSKEY",
  region_name="us-east-1",
)

ec2 = sess.resource('ec2')
volumes = ec2.volumes.all()

to_terminate=[]
for volume in volumes:
    print('Evaluating volume {0}'.format(volume.id))
    print('The number of attachments for this volume is {0}'.format(len(volume.attachments)))

    # Here's where you might add other business logic for deletion criteria
    if len(volume.attachments) == 0:
        to_terminate.append(volume)

if len(to_terminate) == 0:
    print ("No volumes to terminate! Exiting.")
    exit()

for volume in to_terminate:
    print('Deleting volume {0}'.format(volume.id))
    volume.delete()


```
