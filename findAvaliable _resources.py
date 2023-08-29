import boto3

aws_mang_con=boto3.session.Session(profile_name="root")

print(aws_mang_con.get_available_resources())