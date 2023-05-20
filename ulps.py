'''Module 2 - Programming Assignment: ulps'''
import sys
import math

base = sys.float_info.radix
eps = sys.float_info.epsilon
prec = sys.float_info.mant_dig
inf = math.inf
print(float('-inf') * float('inf'))  

def ulps(x,y):
    '''Takes two floating point parameters, x and y, and returns the number of ulps (floating-point intervals) between x and y'''

    '''Check the input parameters for special conditions.'''
    # The function will return infinity if the input parameters have the following properties:
    # Opposite in signs, or
    # Either one of them is zero, or
    # Either one of them is either positive infinity or negative infinity
    if x*y <= 0 or x*y == float('inf'):
        return float('inf')
    if x < 0: # If the input parameters are both negative
        # Convert them to be positive numbers by taking the absolute value.
        x, y = abs(x), abs(y)
    if x > y: # We want x to be the smaller value
        # Swap x and y so x is smaller
        x, y = y, x

    '''Find the exponents for both input parameters in the machine base (base).'''
    # Base = 2

    '''Examine the exp for both parameter:'''


    
