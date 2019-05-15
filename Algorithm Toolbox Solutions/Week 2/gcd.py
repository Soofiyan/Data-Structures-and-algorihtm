# Uses python3
import sys

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
print(gcd_naive(a, b))
