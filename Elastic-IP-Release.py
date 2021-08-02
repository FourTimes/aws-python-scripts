import boto3

sess = boto3.Session(
  aws_access_key_id="MYAWSACCESSKEYID",
  aws_secret_access_key="MYSECRETACCESSKEY",
  region_name="us-east-1",
)


client = sess.resource('ec2')
addresses_dict = client.describe_addresses()
for eip_dict in addresses_dict['Addresses']:
    if "NetworkInterfaceId" not in eip_dict:
        print(eip_dict['PublicIp'])
        # client.release_address(AllocationId=eip_dict['AllocationId'])
