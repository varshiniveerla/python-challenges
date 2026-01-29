from operator import truediv

name =  input("What is your full name? ")
email = input("What is your email id? ")
num = input("What is your Mobile number? ")
age = int(input("What is your age? " ))
valid = True


if name.count(" ") < 1:
    valid = False
elif name.find(" ") == 0 :
    valid = False
elif name.find(" ") == len(name) - 1:
     valid = False


if email.find("@") == -1 or email.find(".") == -1 :
    valid = False
elif email.find("@") == 0 :
    valid = False

if len(num)!= 10 :
    valid = False
elif not num.isdigit() :
    valid = False
elif num.find("0") == 0 :
    valid = False

if age <18 or age > 60 :
    valid = False

if valid :
    print("User Profile is VALID")
else :
    print("User Profile is NOT VALID")










