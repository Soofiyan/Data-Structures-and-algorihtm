# Uses python3
import sys
import math

def lcm_naive(a, b):
    lcm = (a)/gcd_naive(a,b)*b
    return int(math.ceil(lcm))

def gcd_naive(a, b):
    if b>a:
        temp = a
        a = b
        b = temp
    current_gcd = 1
    while b != 0:
        temp = b
        b = a%b
        a = temp
        if(a==0):
            a = 1
    return a

a, b = map(int, input().split())
print(lcm_naive(a, b))

