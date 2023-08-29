import boto3

aws_mag_con=boto3.session.Session(profile_name="root")
ec2_user=aws_mag_con.client(service_name="ec2",region_name="us-east-1")


# Listing all ec2 instences ids
ec2_secur_groups=ec2_user.describe_security_groups()
for sec_grp in ec2_secur_groups['SecurityGroups']:
    print(sec_grp["GroupId"])
