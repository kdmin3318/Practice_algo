import sys
input = sys.stdin.readline
from collections import deque

def bfs(sea, n, m):
    vis = [[0]*m for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    queue = deque()
    count = 0
    
    for i in range(n):
        for j in range(m):
            if sea[i][j] != 0 and vis[i][j] == 0:
                count += 1
                queue.append((i, j))
                vis[i][j] = 1
                
                while queue:
                    x, y = queue.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if sea[nx][ny] != 0 and vis[nx][ny] == 0:
                            queue.append((nx, ny))
                            vis[nx][ny] = 1
    
    return count

def main():
    n, m = map(int, input().split())
    sea = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    year = 0
    
    while True:
        ice_count = bfs(sea, n, m)
        
        if ice_count >= 2:
            print(year)
            break
        elif ice_count == 0:
            print(0)
            break

        new_sea = [row[:] for row in sea]
        
        for i in range(n):
            for j in range(m):
                if sea[i][j] != 0:
                    melting = 0
                    for dir in range(4):
                        nx = i + dx[dir]
                        ny = j + dy[dir]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if sea[nx][ny] == 0:
                            melting += 1
                    new_sea[i][j] = max(0, sea[i][j] - melting)
        
        sea = new_sea
        year += 1

if __name__ == "__main__":
    main()
