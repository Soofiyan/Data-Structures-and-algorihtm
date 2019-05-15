# Uses python3
import sys

def get_change(m):
    #write your code here
    t = int(m/10)
    m = m%10
    f = int(m/5)
    m = m%5
    o = int(m)
    return(t+f+o)

m = int(input())
print(get_change(m))