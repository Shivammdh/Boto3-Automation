import boto3

'''
 when we had create default session for our aws then this time we don't need
to create any aws management object for this time

aws_mang=boto3.session.Session(profile_name="root")
'''
# for iam console
iam_cons=boto3.resource("iam")

# print all users
for each_user in iam_cons.users.all():
    print(each_user.name)