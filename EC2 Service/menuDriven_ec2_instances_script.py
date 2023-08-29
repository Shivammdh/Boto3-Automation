import sys

import boto3

aws_mang_con=boto3.session.Session(profile_name="root")
ec2_client=aws_mang_con.client(service_name="ec2",region_name="us-east-1")
ec2_resorce=aws_mang_con.resource(service_name="ec2",region_name="us-east-1")

while True:
    print("The script perform following actions:")
    print('''
    1.Start.
    2.Stop.
    3.Terminate.
    4.Exit
    ''')
    opt=int(input())
    if opt==1:
        instance_id=input("Please Enter your instance id: ")
        instance_obj = ec2_resorce.Instance(instance_id)
        instance_obj.start()
        print("String ec2 instance........ ")

    elif opt==2:
        instance_id = input("Please Enter your instance id: ")
        instance_obj = ec2_resorce.Instance(instance_id)
        instance_obj.stop()
        print("Stopping ec2 instance........ ")
    elif opt==3:
        instance_id = input("Please Enter your instance id: ")
        instance_obj = ec2_resorce.Instance(instance_id)
        instance_obj.terminate()
        print("Terminating ec2 instance........ ")
    elif opt==4:
        print("Thank you for using this script...")
        sys.exit()
    else:
        print("Your option is invalid please try once again...")
