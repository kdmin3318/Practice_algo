import sys
input = sys.stdin.readline
from collections import deque

def main():
    n,k = map(int, input().split())
    if n==k:
        print(0)
        return
    dx = [-1,1,2]
    position = [0 for _ in range(100001)]
    queue = deque()

    queue.append(n)
    while queue:
        cur = queue.popleft()
        for dir in range(3):
            if dir==2:
                nx = cur * dx[dir]
            else:
                nx = cur + dx[dir]
            if nx==k:
                print(position[cur]+1)
                return
            if nx<0 or nx>=100001:
                continue
            if position[nx]!=0:
                continue
            queue.append(nx)
            position[nx] = position[cur] + 1

if __name__ == "__main__":
    main()
