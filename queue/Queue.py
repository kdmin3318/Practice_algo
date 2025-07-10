import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    queue = deque()

    for _ in range(n):
        o = input().strip().split()
        op = o[0]
        if op=="push":
            queue.append(o[1])
        elif op=="pop":
            print(queue.popleft()) if queue else print(-1)
        elif op=="size":
            print(len(queue))
        elif op=="empty":
            print(0) if queue else print(1)
        elif op=="front":
            print(queue[0]) if queue else print(-1)
        elif op=="back":
            print(queue[-1]) if queue else print(-1)

if __name__ =="__main__":
    main()
