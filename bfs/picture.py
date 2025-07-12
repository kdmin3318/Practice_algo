import sys
input = sys.stdin.readline
from collections import deque

def main():
    n,m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    vis = [[False for _ in range(m)] for _ in range(n)]
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    queue = deque()
    count = 0
    max_picture = 0

    for i in range(n):
        for j in range(m):
            if board[i][j]==1 and not vis[i][j]:
                count += 1
                queue.append((i,j))
                vis[i][j] = True

                size = 1
                while queue:
                    cur = queue.popleft()
                    for dir in range(4):
                        nx = cur[0] + dx[dir]
                        ny = cur[1] + dy[dir]
                        if nx<0 or nx>=n or ny<0 or ny>=m:
                            continue
                        if board[nx][ny]==0 or vis[nx][ny]:
                            continue
                        queue.append((nx,ny))
                        vis[nx][ny] = True
                        size += 1
                max_picture = max(max_picture, size)

    print(count)
    print(max_picture)

if __name__ == "__main__":
    main()
