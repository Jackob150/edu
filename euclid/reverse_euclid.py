################################################################################
# File:         reverse_euclid.py
# Author:       Jakub Ciesielski
# Date:         March 16, 2021
# Description:  Reverse euclidean algorithm for finding inverse elements
#               in Phi(n).
# Arguments:    [1] integer - element to inverse
#               [2] integer - modulus of Phi group
# Notes:        Part of the code containing recursive function based on:
#               geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
#               Only for educational purposes.
################################################################################

################################################################################
# Imports
################################################################################
import sys

################################################################################
# Local functions
################################################################################

### Reverse euclid algorithm                                                 ###
### Source: geeksforgeeks.org/euclidean-algorithms-basic-and-extended/       ###
# param[in]:    a - integer coefficient in the diofantic equation ax + by = gcd
# param[in]:    b - integer coefficient in the diofantic equation ax + by = gcd
# returns:      gcd - integer equal to greatest common divisor for a and b
#               x - integer - solution of the diofantic equation
#               y - integer - solution of the diofantic equation
###
def rev_euclid(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = rev_euclid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

################################################################################
# Main script
################################################################################

### Check for correct number of arguments provided by the user ###
if not len(sys.argv) == 3:
    print("Call the script with 2 args: python euclid.py a b")
    exit()

### Casting arguments to integers ###
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except:
    print("Something wrong with the arguments")
    exit()


if not a < b:
    print("Incorrect arguments")
    exit()

### Calculating and printing the answer
gcd, ans, _ = rev_euclid(a, b)
if gcd == 1:
    if ans < 0:
        ans += b
    print("Inverse element for {} in Phi({}) is {}".format(a, b, ans))
else:
    print("Numbers are not coprime")