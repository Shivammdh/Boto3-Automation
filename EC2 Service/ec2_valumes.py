import boto3

aws_mang_con=boto3.session.Session(profile_name="root")
ec2_ser=aws_mang_con.client(service_name="ec2",region_name="us-east-1")
response=ec2_ser.describe_volumes()["Volumes"]

for each_item in response:
    print(f"The volume id is: {each_item['VolumeId']}\nThe Availability Zone is: {each_item['AvailabilityZone']}\nThe Create time is: {each_item['CreateTime'].strftime('%y-%m-%d')} ")
    # for each_item_info in each_item['Instances']:
    #     print(f'''The image id is: {each_item_info['ImageId']}\nThe instance id is:{each_item_info['InstanceId']}\nThe launch time is: {each_item_info['LaunchTime'].strftime("%y-%m-%d")}''')

    '''
    output:
   The volume id is: vol-0dcc80ef3a674e241
The Availability Zone is: us-east-1b
The Create time is: 22-10-14 

    '''