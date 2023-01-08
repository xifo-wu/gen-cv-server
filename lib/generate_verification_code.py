import math
import random


def generate_verification_code(length=4):
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""

   # length of password can be changed
   # by changing value in range
    for _i in range(length):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP
