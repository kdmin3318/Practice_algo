import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
d = deque()
d.append((1,0))
d.append((0,1))
for i in range(t):
    n = int(input())
    if n>=len(d):
        for i in range(len(d),n+1):
            count_0 = d[i-1][0] + d[i-2][0]
            count_1 = d[i-1][1] + d[i-2][1]
            d.append((count_0, count_1))
    print(d[n][0], d[n][1],sep=" ")
