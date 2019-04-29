# python3
import numpy as np

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    #a, b = map(int, input().split())
    a = np.uint8(input())
    b = np.uint8(input())
    print(sum_of_two_digits(a, b))
