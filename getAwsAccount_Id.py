import boto3

aws_mang_con_root=boto3.session.Session(profile_name="root")
sts_con=aws_mang_con_root.client(service_name="sts",region_name="us-east-1")

response=sts_con.get_caller_identity()
print(f"Aws account id is: {response['Account']}")