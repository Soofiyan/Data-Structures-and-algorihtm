# Uses python3
import math
def calc_fib(n):
        previous = 0
        current  = 1

        for _ in range(n - 1):
                previous, current = current%10, (previous + current)%10
        return current

        
n = int(input())
print(calc_fib(n))
