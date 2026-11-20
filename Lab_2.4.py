import random 
length = int(input("enter the length of OTP: "))
if length == 4 or length == 6:
    otp = ""
for i in range(length):
    otp += str(random.randint(0,9))
print(otp)