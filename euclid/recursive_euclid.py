################################################################################
# File:         recursive_euclid.py
# Author:       Jakub Ciesielski
# Date:         March 16, 2021
# Description:  Euclidean algorithm for finding GCD(a,b) (recursive approach)
# Arguments:    [1] integer to calculate GCD
#               [2] integer to calculate GCD
################################################################################

################################################################################
# Imports
################################################################################
import sys

################################################################################
# Local functions
################################################################################

### Recursive euclid function ###
# param[in]:    a - integer to check greatest common divisor with b
# param[in]:    b - integer to check greatest common divisor with a
# returns:      integer equal to greatest common divisor for a and b
###
def euclid(a, b):
    if not a % b:
        return b
    
    return euclid(b, a % b)

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

### Peinting the answer - last non-zero remainder is now value of 'a' ###
print("GCD({},{}) = {}".format(a, b, euclid(a,b)))