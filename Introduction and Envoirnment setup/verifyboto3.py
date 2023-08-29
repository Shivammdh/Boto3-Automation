import boto3

aws_mang=boto3.session.Session(profile_name="root")

# for iam console
iam_cons=aws_mang.resource("iam")

# print all users
for each_user in iam_cons.users.all():
    print(each_user.name)