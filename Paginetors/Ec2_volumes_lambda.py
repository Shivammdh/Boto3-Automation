from pprint import pprint

import boto3

aws_session=boto3.session.Session(profile_name="root")
ec2_cli=aws_session.client(service_name="ec2",region_name="us-east-1")
volume_ids=[]
f1={'Name':"tag:Prod",'Values':['backup',"Backup"]}
for each_vol in ec2_cli.describe_volumes(Filters=[f1])["Volumes"]:
    volume_ids.append(each_vol['VolumeId'])
print(volume_ids)