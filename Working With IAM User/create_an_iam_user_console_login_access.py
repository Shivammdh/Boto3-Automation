import string

import boto3
from random import choice
import sys


def get_iam_client_object():
    session = boto3.session.Session(profile_name="root")
    iam_client = session.client(service_name="iam", region_name="us-east-1")
    return iam_client


# def get_random_password():
#     len_of_password = 8
#     valid_chars_for_password = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#     return "".join(choice(valid_chars_for_password) for each_char in range(len_of_password))
#
def get_randome_password():
    small = string.ascii_lowercase
    capt = string.ascii_uppercase
    digit = string.digits
    special = "#$%&()*+<=>?@[]^_{}~"
    passwordstr = small + capt + digit + special
    password_length = 8

    while True:
        cnt = 0
        l, u, d, p = 0, 0, 0, 0
        genpass = "".join(choice(passwordstr) for i in range(password_length))
        if genpass[0] in capt:

            for i in genpass:

                # counting lowercase alphabets
                if (i in small):
                    l += 1

                    # counting uppercase alphabets
                if (i in capt):
                    u += 1

                    # counting digits
                if (i in digit):
                    d += 1

                    # counting the mentioned special characters
                if (i in special):
                    p += 1
            if (l >= 1 and u >= 1 and p == 2 and d >= 1 and l + p + u + d == password_length):
                return genpass

        else:
            continue


def main():
    iam_client = get_iam_client_object()
    Iam_user_name = "shivammdh0105@gmail.com"
    # passwrd=get_random_password()
    PolicyArn = "arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_client.create_user(UserName=Iam_user_name)
    except Exception as e:
        if e.response['Error']['Code'] == "EntityAlreadyExists":
            print("Already Iam User with {} is exist".format(Iam_user_name))
            sys.exit(0)
        else:
            print("Please verify the following error and retry")
            print(e)
            sys.exit(0)
    response = iam_client.create_access_key(UserName=Iam_user_name)
    print("IAM User Name={}".format(Iam_user_name))
    print("AccessKeyId={}\nSecretAccessKey={}".format(response['AccessKey']['AccessKeyId'],
                                                response['AccessKey']['SecretAccessKey']))
    # iam_client.create_login_profile(UserName=Iam_user_name,Password=passwrd,PasswordResetRequired=False)
    iam_client.attach_user_policy(UserName=Iam_user_name, PolicyArn=PolicyArn)
    # print "IAM User Name={} and Password={}".format(Iam_user_name,passwrd)
    return None


if __name__ == "__main__":
    main()