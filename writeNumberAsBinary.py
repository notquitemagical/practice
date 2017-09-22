# 1.1.9
# Write a code fragment that puts the binary representation of a positive integer n
# into a string s

import sys, math

finalBinary = 0

def check(a):
    if math.log(a,2) == math.floor(math.log(a,2)):
        return printBinary(a)
    else:
        return split(a)
    
def writeBinary(b):
    binary = int("1" + "0" * int(math.log(b,2)))
    return binary

def printBinary(c):
    global finalBinary
    finalBinary += writeBinary(c)
    return finalBinary

def split(d):
    expo = math.floor(math.log(d, 2))
    remnant = d - 2**expo
    powerOfTwo = d - remnant
    check(powerOfTwo)
    return check(remnant)

print check(float(sys.argv[1]))
