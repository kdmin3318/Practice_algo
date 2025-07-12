import sys
input = sys.stdin.readline
from collections import deque

def main():
    m,n = map(int, input().split())
    box = []
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    queue = deque()
    for i in range(n):
            row = list(map(int, input().split()))
            box.append(row)
            for j in range(len(row)):
                  if row[j]==1:
                     queue.append((i,j))   

    while queue:
        cur = queue.popleft()
        for dir in range(4):
            nx = cur[0] + dx[dir]
            ny = cur[1] + dy[dir]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if box[nx][ny]==-1 or box[nx][ny]!=0:
                continue
            queue.append((nx,ny))
            box[nx][ny] = box[cur[0]][cur[1]] + 1

    if any(0 in row for row in box):
        print(-1)
    else:
        print(max(map(max, box)) - 1)

if __name__ == "__main__":
    main()
