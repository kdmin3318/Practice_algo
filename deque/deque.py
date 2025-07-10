import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    dq = deque()
    for _ in range(n):
        o = input().strip().split()
        op = o[0]
        if op=="push_front":
            dq.appendleft(o[1])
        elif op=="push_back":
            dq.append(o[1])
        elif op=="pop_front":
            print(dq.popleft()) if dq else print(-1)
        elif op=="pop_back":
            print(dq.pop()) if dq else print(-1)
        elif op=="size":
            print(len(dq))
        elif op=="empty":
            print(0) if dq else print(1)
        elif op=="front":
            print(dq[0]) if dq else print(-1)
        elif op=="back":
            print(dq[-1]) if dq else print(-1)
    
if __name__ =="__main__":
    main()
