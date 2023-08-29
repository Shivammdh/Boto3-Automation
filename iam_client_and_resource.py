import boto3

aws_mang=boto3.session.Session(profile_name="root")

# Iam console using resource object
iam_resor=aws_mang.resource("iam")

# listing all iam users
for iam_user in iam_resor.users.all():
    print(iam_user.name)

# for iam console using client object
iam_cons=aws_mang.client("iam")

# print iam client user
print(iam_cons.list_users())

