import boto3
import time
aws_con=boto3.session.Session(profile_name="root")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")
print("Starting Given Instance......")
ec2_con_cli.start_instances(InstanceIds=['i-0b574a8e0a0f4236c'])
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-0b574a8e0a0f4236c']) #40 checks after every 15 sec, otherwise raise exception
print("Now your ec2 instance is up and running")