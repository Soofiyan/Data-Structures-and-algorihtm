# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    fn = (((5**0.5 + 1)/2)**n)/(5**0.5)
    return int((fn+0.5))

n = int(input())
print(calc_fib(n))

