import sys
input = sys.stdin.readline
from collections import deque

def main():
    m,n,h = map(int, input().split())
    box = []
    queue = deque()
    for i in range(h):
        layer = []
        for j in range(n):
            row = list(map(int, input().split()))
            layer.append(row)
            for k in range(m):
                if row[k]==1:
                    queue.append((i,j,k))
        box.append(layer)

    dz = [-1,1,0,0,0,0]
    dx = [0,0,-1,0,1,0]
    dy = [0,0,0,-1,0,1]
    while queue:
        cur = queue.popleft()
        for dir in range(6):
            nz = cur[0] + dz[dir]
            nx = cur[1] + dx[dir]
            ny = cur[2] + dy[dir]
            if nz<0 or nz>=h or nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if box[nz][nx][ny]!=0 or box[nz][nx][ny]==-1:
                continue
            queue.append((nz,nx,ny))
            box[nz][nx][ny] = box[cur[0]][cur[1]][cur[2]] + 1

    if any(0 in row for layer in box for row in layer):
        print(-1)
    else:
        print(max([max(row) for layer in box for row in layer]) - 1)

if __name__ == "__main__":
    main()
