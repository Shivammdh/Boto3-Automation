import boto3

aws_mag_con=boto3.session.Session(profile_name="root")
iam_user=aws_mag_con.resource(service_name="iam",region_name="us-east-1")
ec2_user=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")

print("="*50)
print("Listing all iam user using resources  object:")
print("="*50)
# Listing all iam user using resourse  object
for each_user in iam_user.users.all():
    print(each_user.name)
print("="*50)
print("Listing all ec2 instanses using resources object")
print("="*50)
#  Listing all ec2 instanses using resources object
for each_inst in ec2_user.instances.all():
    print(each_inst.id)

# listing out all security group using resources object:
print("="*50)
print("listing out all security group id using resources object:")
print("="*50)
for each_secure_id in ec2_user.security_groups.all():
    print(each_secure_id.id)