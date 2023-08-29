from pprint import pprint

import boto3

aws_mag_con=boto3.session.Session(profile_name="root")
iam_user=aws_mag_con.client(service_name="iam",region_name="us-east-1")
ec2_user=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
s3_user=aws_mag_con.client(service_name="s3",region_name="us-east-1")

# Listing all iam user using client object
response=iam_user.list_users()
users=response["Users"]
for user in users:
    print(user["UserName"])


# Listing all ec2 instences ids
ec2_instences=ec2_user.describe_instances()
for resev in ec2_instences['Reservations']:
    for instanc in resev['Instances']:
        print(instanc["InstanceId"])
