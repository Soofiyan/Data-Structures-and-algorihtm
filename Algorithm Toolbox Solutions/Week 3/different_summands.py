# Uses python3
import sys

def optimal_summands(a):
    #write your code here
    res = int(a)
    rem = []
    temp = 0
    i = 1
    sum = 0
    if (res == 1):
        rem.append(1)
        return rem
    if (res == 2):
        rem.append(2)
        return rem
    else:
        rem.append(1)
        res = res - 1
        sum = 1
    while i != a:
        i += 1
        if (i <= a - sum):
            rem.append(i)
            temp = temp + 1
            sum = sum + rem[temp]
            res = res - i
        if (i >= (a - sum)):
            value = rem.pop(temp)
            rem.append(i)
            res = res + value - i
            sum = sum + i - value
        if (res == 0):
            break
    return rem


n = int(input())
summands = optimal_summands(n)
print(len(summands))
for x in summands:
    print(x, end=' ')
