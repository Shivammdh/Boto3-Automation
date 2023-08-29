import boto3

aws_mang_con=boto3.session.Session(profile_name="root")
iam_cons=aws_mang_con.client("iam")

# listing all iam user name using client object
for user in iam_cons.list_users()["Users"]:
    print(user['UserName'])