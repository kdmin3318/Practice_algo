import sys
input = sys.stdin.readline
from collections import deque

def main():
    n, m = map(int, input().split())

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    queue = deque()
    board = [list(map(int, input().strip())) for _ in range(n)]
    vis = [[[0]*2 for _ in range(m)] for _ in range(n)]

    vis[0][0][0] = 1
    queue.append((0,0,0))
    while queue:
        x, y, breaking = queue.popleft()
        if x==n-1 and y ==m-1:
            print(vis[x][y][breaking])
            return
        
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if board[nx][ny]==1 and breaking == 0:
                vis[nx][ny][1] = vis[x][y][0] + 1
                queue.append((nx,ny,1))
                continue
            if board[nx][ny]==0 and vis[nx][ny][breaking]==0:
                vis[nx][ny][breaking] = vis[x][y][breaking] + 1
                queue.append((nx,ny,breaking))
                continue

    print(-1)

    

if __name__ == "__main__":
    main()
