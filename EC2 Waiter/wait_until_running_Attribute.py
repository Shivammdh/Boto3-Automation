import boto3
import time
aws_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")
my_inst_ob=ec2_con_re.Instance("i-0b574a8e0a0f4236c")
print("Starting Given Instance......")
my_inst_ob.start()
my_inst_ob.wait_until_running() ##Resource waiter waits for 200sec(40 checks after every 5 sec) after that it will through an exception
print("Now Instance is up and running..")