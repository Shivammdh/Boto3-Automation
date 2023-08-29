import boto3

session=boto3.session.Session(profile_name="root")
iam_con=session.resource(service_name="iam",region_name="us-east-1")

for each_user in iam_con.users.all():
    print(each_user.name)