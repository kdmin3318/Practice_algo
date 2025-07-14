import sys
input = sys.stdin.readline
from collections import deque

def main():
    f,s,g,u,d = map(int, input().split())
    if s==g:
        print(0)
        return
    dx = [u,-d]
    buliding = [0 for _ in range(f+1)]

    queue = deque()
    queue.append(s)
    buliding[s] = 1
    while queue:
        cur = queue.popleft()
        for dir in range(2):
            nx = cur + dx[dir]
            if nx<1 or nx>f:
                continue
            if buliding[nx]!=0:
                continue
            queue.append(nx)
            buliding[nx] = buliding[cur] + 1
            if nx == g:
               print(buliding[g] - 1)
               return

    print("use the stairs") 
    

if __name__ == "__main__":
    main()
