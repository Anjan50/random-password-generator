# random-password-generator
small project

#!/usr/bin/python3

import random

chars = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890^?!?$%&/()=?`'+#*'~';:_,.-<>|"
password = ""

print("Use Char list = %s \n" % chars)

length = int(input("[*] Input Password Length: "))
while len(password) != length:
    password = password + random.choice(chars)
    if len(password) == length:
        print("Password: %s" % password)
