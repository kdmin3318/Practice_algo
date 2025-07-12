import sys
input = sys.stdin.readline
from collections import deque

def main():
    n,m = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(n)]
    vis = [[0 for _ in range(m)] for _ in range(n)]
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    queue = deque()

    queue.append((0,0))
    vis[0][0] = 1
    while queue:
        cur = queue.popleft()
        for dir in range(4):
            nx = cur[0] + dx[dir]
            ny = cur[1] + dy[dir]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if board[nx][ny]==0 or not vis[nx][ny]==0:
                continue
            queue.append((nx,ny))
            vis[nx][ny] = vis[cur[0]][cur[1]] + 1
    
    print(vis[n-1][m-1])

if __name__ == "__main__":
    main()
