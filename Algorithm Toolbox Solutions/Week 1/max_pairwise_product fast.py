# python3

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max_product1 = 0
    max_product2 = 0
    prev_max_product1 = 0
    temp = 0
    for first in range(n):
        max_product1 = max(max_product1,numbers[first])
        if(max_product1 > prev_max_product1):
            temp = first
            prev_max_product1 = max_product1
    max_product = 0
    for second in range(n):
        if(second != temp):
            max_product2 = max(max_product2,numbers[second])
    max_product = max_product1*max_product2
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
