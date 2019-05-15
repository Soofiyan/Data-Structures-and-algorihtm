# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments, n):
    points = []
    #write your code here
    sorted_segments = sorted(segments, key=lambda x:x[0][1])
    while sorted_segments:
        segment = sorted_segments.pop(0)
        point = segment[0][1]
        points.append(point)
        for s in sorted_segments[:]:
            if (s[0][0] <= point <= s[0][1]):
                sorted_segments.remove(s)

    return points


n = int(input())
segments = []
for i in range(n):
    data = list(map(int, input().split()))
    segments.append(list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2]))))
points = optimal_points(segments, n)
print(len(points))
for p in points:
    print(p, end=' ')
'''
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    # Sort segments by the right endpoint.
    sorted_segments = sorted(segments, key=lambda x: x.end)

    points = []
    while sorted_segments:
        # Place the first point to the right endpoint of the first segment.
        # Remove the segment, since it's considered as covered one.
        segment = sorted_segments.pop(0)
        point = segment.end
        points.append(point)

        # Check whether the point hit the other segments.
        for s in sorted_segments[:]:
            if s.start <= point <= s.end:
                sorted_segments.remove(s)

    return points


n, *data = map(int, input().split())
segments = list(
    map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
points = optimal_points(segments)
print(len(points))
for p in points:
    print(p, end=" ")
'''