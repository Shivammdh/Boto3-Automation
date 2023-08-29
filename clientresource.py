import boto3

aws_mang=boto3.session.Session(profile_name="root")

# for iam console
iam_cons=aws_mang.client("iam")

