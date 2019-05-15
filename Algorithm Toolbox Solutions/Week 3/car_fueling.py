# python3
import sys


def compute_min_refills(distance, tank, n, stops):
    # write your code here
    count = tank
    cp = 0
    stops.append(distance)
    stops.append(0)
    for i in range(n+1):
        if(stops[i] <= count and stops[i+1] <= count):
            count = count
        elif(stops[i] <= count and stops[i+1] > count):
            cp = cp + 1
            count = tank + stops[i]
            if(stops[i+1] > count):
                return -1
    return cp


d = int(input())
m = int(input())
n = int(input())
stops = list(map(int, input().split()))
print(compute_min_refills(d, m, n, stops))
