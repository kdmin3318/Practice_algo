import sys
input = sys.stdin.readline
from collections import deque

def main():
    n,l = map(int, input().split())
    a = list(map(int, input().split()))
    dq = deque()
    
    for i in range(len(a)):
        if dq and i-dq[0]>=l:
            dq.popleft()
        while dq and a[dq[-1]]>=a[i]:
            dq.pop()
        dq.append(i)

        print(a[dq[0]], end=" ")

if __name__ =="__main__":
    main()
