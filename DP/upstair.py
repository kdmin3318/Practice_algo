import sys
input = sys.stdin.readline

n = int(input())
s = [0]+[int(input()) for _ in range(n)]

d = [[0 for _ in range(3)] for _ in range(n+1)]
d[1][1] = s[1]
d[1][2] = 0
d[2][1] = s[2]
d[2][2] = s[1]+s[2]
for i in range(3,n+1):
    d[i][1] = max(d[i-2][1], d[i-2][2]) + s[i]
    d[i][2] = d[i-1][1] + s[i]
print(max(d[n][1],d[n][2]))
