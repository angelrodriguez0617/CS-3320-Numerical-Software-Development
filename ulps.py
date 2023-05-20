'''Module 2 - Programming Assignment: ulps'''
import sys
import math

base = sys.float_info.radix
eps = sys.float_info.epsilon
prec = sys.float_info.mant_dig
inf = math.inf
# print(f'base: {base}\neps: {eps}\nprec: {prec}\ninf: {inf}') 

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
    exp_x = 0
    exp_y = 0
    while x >= base:
        x /= base
        exp_x += 1
    while y >= base:
        y /= base
        exp_y += 1
    # print(f'exp_x: {exp_x}')
    # print(f'exp_x: {exp_y}')

    '''Examine the exp for both parameter:'''
    if exp_x == exp_y: # If they are the same
        spacing = eps*(base**exp_x)
        intervals = (y - x) / spacing
    elif (abs(exp_x - exp_y) == 1): # If they differ by one
        if exp_y - exp_x != 1:
            print('SUM TING WONG, Y EXPONENT SHOULD BE GREATER THAN X EXPONENT')
        x_spacing = eps*(base**exp_x)
        x_intervals = (base**(exp_x+1) - x) / x_spacing
        y_spacing = eps*(base**exp_y)
        y_intervals = (y - base**(exp_y)) / y_spacing
        intervals = x_intervals + y_intervals
    else: # If they differ by more than one
        x_spacing = eps*(base**exp_x)
        x_intervals = (base**(exp_x+1) - x) / x_spacing
        y_spacing = eps*(base**exp_y)
        y_intervals = (y - base**(exp_y)) / y_spacing
        intervals = x_intervals + y_intervals
        exp_current = exp_x + 1
        while exp_current != exp_y:
            intervals += ((base**(exp_current+1)) - (base**(exp_current))) / (eps*(base**exp_current))
            exp_current += 1
    return intervals

print(ulps(-1.0, -1.0000000000000003)) # 1
print(ulps(1.0, 1.0000000000000003)) # 1
print(ulps(1.0, 1.0000000000000004)) # 2
print(ulps(1.0, 1.0000000000000005)) # 2
print(ulps(1.0, 1.0000000000000006)) # 3
print(ulps(0.9999999999999999, 1.0)) # 1
print(ulps(0.4999999999999995, 2.0)) # 9007199254741001
print(ulps(0.5000000000000005, 2.0)) # 9007199254740987
print(ulps(0.5, 2.0)) # 9007199254740992
print(ulps(1.0, 2.0)) # 4503599627370496
print(2.0**52) #  4503599627370496.0
print(ulps(-1.0, 1.0)) # inf
print(ulps(-1.0, 0.0)) # inf
print(ulps(0.0, 1.0)) # inf
print(ulps(5.0, math.inf)) # inf
print(ulps(15.0, 100.0)) # 12103423998558208

    
