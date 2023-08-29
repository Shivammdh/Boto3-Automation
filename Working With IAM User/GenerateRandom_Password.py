from random import choice
import string
small=string.ascii_lowercase
capt=string.ascii_uppercase
digit=string.digits
special="#$%&()*+<=>?@[]^_{}~"
passwordstr=small+capt+digit+special
password_length=8

while True:
    cnt=0
    l,u,d,p=0,0,0,0
    genpass="".join(choice(passwordstr) for i in range(password_length))
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
            print(genpass)
            break
    else:
        continue

