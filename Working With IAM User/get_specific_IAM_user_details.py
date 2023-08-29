import boto3
import datetime
session=boto3.session.Session(profile_name="root")
iam_con_re=session.resource(service_name="iam")

#Get details of any iam user
# 1. Get details of shivammdh user
iam_user_ob=iam_con_re.User("shivammdh")
print(iam_user_ob.user_name,iam_user_ob.user_id,iam_user_ob.arn,iam_user_ob.create_date.strftime("%Y-%m-%d"))

# 2. Get Details of terraform users
iam_user_ob=iam_con_re.User("terraform")
print(iam_user_ob.user_name,iam_user_ob.user_id,iam_user_ob.arn,iam_user_ob.create_date.strftime("%Y-%m-%d"))
