import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    domain = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    max_h = max(map(max,domain))

    max_safe_domain = 0
    for h in range(max_h+1):
        safe_domain = 0
        vis = [[0 for _ in range(n)] for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(n):
                if domain[i][j]>h and vis[i][j]==0:
                    safe_domain += 1
                    queue.append((i,j))
                    vis[i][j] = 1
                    while queue:
                        x,y = queue.popleft()
                        for dir in range(4):
                            nx = x + dx[dir]
                            ny = y + dy[dir]
                            if nx<0 or nx>=n or ny<0 or ny>=n:
                                continue
                            if domain[nx][ny]<=h or vis[nx][ny]==1:
                                continue
                            queue.append((nx,ny))
                            vis[nx][ny] = 1
        max_safe_domain = max(max_safe_domain, safe_domain)
    
    print(max_safe_domain)

if __name__ == "__main__":
    main()
