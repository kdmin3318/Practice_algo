import sys
input = sys.stdin.readline
from collections import deque

ans = 0

def solve(k,n,s,w):
    global ans
    if k==n:
        cnt = 0
        for i in range(n):
            if s[i]<=0: cnt += 1
        ans = max(ans, cnt)
        return
    
    if s[k]<=0:
        solve(k+1,n,s,w)
        return

    canHit = False
    for i in range(n):
        if i!=k and s[i]>0:
            canHit = True
            s[k] -= w[i]
            s[i] -= w[k]
            solve(k+1,n,s,w)
            s[k] += w[i]
            s[i] += w[k]

    if not canHit:
        cnt = 0
        for i in range(n):
            if s[i]<=0: cnt+=1
        ans = max(ans,cnt)

def main():
    global ans
    ans = 0
    n = int(input())
    s = [0]*n
    w = [0]*n
    for i in range(n):
        s[i],w[i] = map(int, input().split())
    solve(0,n,s,w)
    print(ans)

if __name__ =="__main__":
    main()
