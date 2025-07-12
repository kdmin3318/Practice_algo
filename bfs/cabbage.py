import sys
input = sys.stdin.readline
from collections import deque

def main():
    t = int(input())
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    for _ in range(t):
        m,n,k = map(int, input().split())
        farm = [[0 for _ in range(m)] for _ in range(n)]
        vis = [[0 for _ in range(m)] for _ in range(n)]
        queue = deque()

        for _ in range(k):
            x,y = map(int, input().split())
            farm[y][x] = 1

        count = 0
        for i in range(n):
            for j in range(m):
                if farm[i][j]==1 and vis[i][j]!=1:
                    vis[i][j] = 1
                    count += 1
                    queue.append((i,j))
                    while queue:
                        cur = queue.popleft()
                        for dir in range(4):
                            nx = cur[0] + dx[dir]
                            ny = cur[1] + dy[dir]
                            if nx<0 or nx>=n or ny<0 or ny>= m:
                                continue
                            if farm[nx][ny]==0 or vis[nx][ny]==1:
                                continue
                            queue.append((nx,ny))
                            vis[nx][ny] = 1
        print(count)

if __name__ == "__main__":
    main()
