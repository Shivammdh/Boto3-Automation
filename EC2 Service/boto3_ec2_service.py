import boto3

aws_mang_con=boto3.session.Session(profile_name="root")
ec2_ser=aws_mang_con.client(service_name="ec2",region_name="us-east-1")
response=ec2_ser.describe_instances()["Reservations"]

for each_item in response:
    for each_item_info in each_item['Instances']:
        print(f'''The image id is: {each_item_info['ImageId']}\nThe instance id is:{each_item_info['InstanceId']}\nThe launch time is: {each_item_info['LaunchTime'].strftime("%y-%m-%d")}''')

    '''
    output:
    The image id is: ami-0149b2da6ceec4bb0
The instance id is:i-0b574a8e0a0f4236c
The launch time is: 2022-10-14 06:39:05+00:00
    '''