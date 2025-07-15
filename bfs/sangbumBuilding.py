import sys
input = sys.stdin.readline
from collections import deque

def main():
    l,r,c = map(int, input().split())
    if l==0 and r==0 and c==0:
        return 0

    queue = deque()
    building = []
    vis = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    for i in range(l):
        layer = []
        for j in range(r):
            row = input().strip()
            for k in range(c):
                if row[k] == "S":
                    queue.append((i,j,k))
                    vis[i][j][k] = 1
            layer.append(row)
        building.append(layer)
        input()
    
    dz = [-1,1,0,0,0,0]
    dx = [0,0,-1,0,1,0]
    dy = [0,0,0,-1,0,1]

    while queue:
        z,x,y = queue.popleft()
        for dir in range(6):
            nz = z + dz[dir]
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nz<0 or nz>=l or nx<0 or nx>=r or ny<0 or ny>=c:
                continue
            if building[nz][nx][ny]=="#" or vis[nz][nx][ny]!=0:
                continue
            queue.append((nz,nx,ny))
            vis[nz][nx][ny] = vis[z][x][y] + 1
            if building[nz][nx][ny] == "E":
                print(f"Escaped in {vis[nz][nx][ny]-1} minute(s).")
                return 1
        
    print("Trapped!")
    return 1

if __name__ == "__main__":
    while main():
        continue
