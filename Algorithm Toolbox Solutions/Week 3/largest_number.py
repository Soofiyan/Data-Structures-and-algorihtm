#Uses python3

import sys


def largest_number(a):
    # write your code here
    res = ""
    while len(a):
        first = a[0]
        for x in a[1:]:
            a1 = first*len(x)
            b1 = x*len(first)
            if first * len(x) < x * len(first): first = x
        a.remove(first)
        res += first
    return res


n = int(input())
a = input().split()
print(largest_number(a))
