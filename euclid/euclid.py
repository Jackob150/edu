################################################################################
# File:         euclid.py
# Author:       Jakub Ciesielski
# Date:         March 16, 2021
# Description:  Euclidean algorithm for finding GCD(a,b)
# Arguments:    [1] integer to calculate GCD
#               [2] integer to calculate GCD
################################################################################

################################################################################
# Imports
################################################################################
import sys

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

### Algorithm's loop - calculating remainders and substituting  ###
### Break condition - remainder = 0                             ###
r = 1
while r:
    r = a % b
    a = b
    b = r

### Peinting the answer - last non-zero remainder is now value of 'a' ###
print("GCD({},{}) = {}".format(sys.argv[1], sys.argv[2], a))