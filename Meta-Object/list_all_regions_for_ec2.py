import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mag_con.resource(service_name="ec2")

'''
we have to create an resource object but we don't use describe_regions()
using resource group object so If I want to use describe_regions() using 
resources object then first switch to client object using meta concept.
'''
for each_item in ec2_con_re.meta.client.describe_regions()['Regions']:
	print(each_item['RegionName'])
