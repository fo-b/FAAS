import boto3
from operator import itemgetter
import json

# Region
region_name = 'eu-central-1'

# EC2-Client init
client = boto3.client('ec2')

response = client.describe_subnets()

# print Subnet information
print("Subnets:")
for subnet in response['Subnets']:
    print(f"Subnet ID: {subnet['SubnetId']}")
    print(f"VPC ID: {subnet['VpcId']}")
    print(f"Availability Zone: {subnet['AvailabilityZone']}")
    print(f"CIDR Block: {subnet['CidrBlock']}")
    print("\n")

key_pair_name = 'testkey'  # Replace with the name of your key pair

response = client.describe_key_pairs(KeyNames=[key_pair_name])
key_pair_info = response['KeyPairs'][0]  # Get the first (and only) result

# Print key pair details
print("Key Pair:")
print(f"Key Pair Name: {key_pair_info['KeyName']}")
print(f"Fingerprint: {key_pair_info['KeyFingerprint']}\n")

try:
    # Filter for AMIs with the name 'ubuntu-jammy-22.04'
    response = client.describe_images(
        Filters=[
            {
                'Name': 'name',
                'Values': ['ubuntu-jammy-22.04'],
            },
        ],
    )

    # Extract and print specific AMI information
    for ami in response['Images']:
        ami_info = {
            'Architecture': ami['Architecture'],
            'CreationDate': ami['CreationDate'],
            'ImageId': ami['ImageId'],
            'ImageLocation': ami['ImageLocation'],
            'ImageType': ami['ImageType'],
            'Public': ami['Public'],
            'KernelId': ami.get('KernelId', ''),
            'OwnerId': ami['OwnerId'],
            'Platform': ami.get('Platform', ''),
            'PlatformDetails': ami.get('PlatformDetails', ''),
            'UsageOperation': ami.get('UsageOperation', ''),
            'ProductCodes': ami.get('ProductCodes', []),
            'RamdiskId': ami.get('RamdiskId', ''),
            'State': ami['State'],
            'BlockDeviceMappings': ami['BlockDeviceMappings'],
            'Description': ami['Description'],
            'EnaSupport': ami['EnaSupport'],
            'Hypervisor': ami['Hypervisor'],
            'ImageOwnerAlias': ami['ImageOwnerAlias'],
            'Name': ami['Name'],
            'RootDeviceName': ami['RootDeviceName'],
            'RootDeviceType': ami['RootDeviceType'],
            'SriovNetSupport': ami.get('SriovNetSupport', ''),
            'StateReason': ami.get('StateReason', {}),
            'Tags': ami.get('Tags', []),
            'VirtualizationType': ami['VirtualizationType'],
            'BootMode': ami.get('BootMode', ''),
            'TpmSupport': ami.get('TpmSupport', ''),
            'DeprecationTime': ami.get('DeprecationTime', ''),
            'ImdsSupport': ami.get('ImdsSupport', ''),
        }

        print("AMI:")
        for key, value in ami_info.items():
            print(f"{key}: {value}")
        print("\n")

except Exception as e:
    print(f"An error occurred: {str(e)}")