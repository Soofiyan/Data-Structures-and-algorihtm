# Uses python3
import sys

def get_optimal_value(capacity, weights, values, n):
    value = 0.
    # write your code here
    if(capacity == 0):
        return value
    ratio = []
    for i in range(n):
        ratio.insert(i,(values[i]/weights[i],i))
    ratio.sort(reverse=True)
    for i in range(n):
        min_weight = min(weights[ratio[i][1]],capacity)
        value += min_weight*ratio[i][0]
        #weights[i] -= min_weight
        capacity -= min_weight
        #print(min_weight)
    #print(ratio)
    return value

data = list(map(int, input().split()))
n, capacity = data[0:2]
values = []
weights = []
for i in range(n):
    temp = list(map(int, input().split()))
    values.append(temp[0])
    weights.append(temp[1])
opt_value = get_optimal_value(capacity, weights, values, n)
print("{:.10f}".format(opt_value))
