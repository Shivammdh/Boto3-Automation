import boto3
import time
aws_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")

# Start ec2 instance using resources object
my_inst_ob=ec2_con_re.Instance("i-0b574a8e0a0f4236c")
print("Starting given instance....")
my_inst_ob.start()

# Wait for running ec2 using client object
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-0b574a8e0a0f4236c'])
print("Now your ec2 instace is up and running")