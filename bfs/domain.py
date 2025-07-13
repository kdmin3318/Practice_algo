import sys
input = sys.stdin.readline
from collections import deque

def main():
    m,n,k = map(int, input().split())
    paper = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1,x2):
            for j in range(y1,y2):
                paper[i][j] = 1
        
    vis = [[0 for _ in range(m)] for _ in range(n)]
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    queue = deque()
    count = 0
    size = []
    for i in range(n):
        for j in range(m):
            if paper[i][j]==0 and vis[i][j]==0:
                queue.append((i,j))
                vis[i][j] = 1
                count += 1
                s = 0
                while queue:
                    s += 1
                    x,y = queue.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if nx<0 or nx>=n or ny<0 or ny>=m:
                            continue
                        if paper[nx][ny]==1 or vis[nx][ny]!=0:
                            continue
                        queue.append((nx,ny))
                        vis[nx][ny] = 1
                size.append(s)
    
    print(count)
    size.sort()
    print(" ".join(map(str, size)))

if __name__ == "__main__":
    main()
