import boto3

aws_mng_con=boto3.session.Session(profile_name="root")
ec2_obj_re=aws_mng_con.resource(service_name="ec2",region_name="us-east-1")
ec2_obj_cli=aws_mng_con.client(service_name="ec2",region_name="us-east-1")

all_instance_id=[]
for each in ec2_obj_re.instances.all():
    all_instance_id.append(each.id)
waiter=ec2_obj_cli.get_waiter('instance_running')
print("Starting all instances...........")
ec2_obj_re.instances.start()
waiter.wait(InstanceIds=all_instance_id)
print("Now your ec2 instances is up and running")