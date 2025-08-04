import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))
d = [0]+[0]*n
sum=0
for i in range(n):
    sum += num[i]
    d[i+1] = sum
for i in range(m):
    i,j = map(int,input().split())
    print(d[j]-d[i-1])
