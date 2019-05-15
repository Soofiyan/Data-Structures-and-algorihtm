# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if (n <= 1):
        return n
    fn = (((5**0.5 + 1)/2)**n)/(5**0.5)
    fn = int(fn+0.5)
    ans = fn%m
    print(fn)
    ans = int(ans+0.5)
    return ans


n, m = map(int, input().split())
print(get_fibonacci_huge_naive(n, m))
