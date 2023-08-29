import boto3

aws_mang=boto3.session.Session(profile_name="root")

# for iam console
s3_con=aws_mang.resource("s3")

# print all users
for each_user in s3_con.buckets.all():
    print(each_user.name)