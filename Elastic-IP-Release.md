```py

import boto3

login = boto3.Session(
  aws_access_key_id="xxxxxxxxxxxx",
  aws_secret_access_key="xxxxxxxxxxxx",
  region_name="ap-south-1",
)


EC2 = login.client('ec2')

addresses_dict = EC2.describe_addresses()
for eip_dict in addresses_dict['Addresses']:
    if "NetworkInterfaceId" not in eip_dict:
        print(eip_dict['PublicIp'])
        EC2.release_address(AllocationId=eip_dict['AllocationId'])

        
```
