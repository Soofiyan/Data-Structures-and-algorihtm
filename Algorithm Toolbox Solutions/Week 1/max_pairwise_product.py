# python3


def max_pairwise_product(numbers,length):
    n = len(numbers)
    max_product = 0
    for first in range(length):
        for second in range(first + 1, length):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    length = len(input_numbers)
    print(max_pairwise_product(input_numbers,length))
