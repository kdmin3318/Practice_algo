import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*3 for _ in range(n)]
d[0][0] = cost[0][0]
d[0][1] = cost[0][1]
d[0][2] = cost[0][2]
for i in range(1,n):
    d[i][0] = min(d[i-1][1],d[i-1][2]) + cost[i][0]
    d[i][1] = min(d[i-1][0],d[i-1][2]) + cost[i][1]
    d[i][2] = min(d[i-1][0],d[i-1][1]) + cost[i][2]

print(min(d[n-1][0],d[n-1][1],d[n-1][2]))
