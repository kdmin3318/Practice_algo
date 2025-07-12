import sys
input = sys.stdin.readline
from collections import deque

def main():
    r,c = map(int, input().split())
    board = []
    F = [[0 for _ in range(c)] for _ in range(r)]
    J = [[0 for _ in range(c)] for _ in range(r)]
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]

    Q1 = deque()
    Q2 = deque()
    for i in range(r):
        row = input().strip()
        board.append(row)
        for j in range(c):
            if row[j]=="F":
                Q1.append((i,j))
                F[i][j] = 1
            if row[j]=="J":
                Q2.append((i,j))
                J[i][j] = 1
        
    while Q1:
        cur = Q1.popleft()
        for dir in range(4):
            nx = cur[0] + dx[dir]
            ny = cur[1] + dy[dir]
            if nx<0 or nx>=r or ny<0 or ny>=c:
                continue
            if board[nx][ny]=="#" or F[nx][ny]!=0:
                continue
            Q1.append((nx,ny))
            F[nx][ny] = F[cur[0]][cur[1]] + 1

    while Q2:
        cur = Q2.popleft()
        for dir in range(4):
            nx = cur[0] + dx[dir]
            ny = cur[1] + dy[dir]
            if nx<0 or nx>=r or ny<0 or ny>=c:
                print(J[cur[0]][cur[1]])
                sys.exit()
            if (board[nx][ny] == "#" or J[nx][ny] != 0 or 
                (F[nx][ny] != 0 and J[cur[0]][cur[1]] + 1 >= F[nx][ny])):
                continue
            Q2.append((nx,ny))
            J[nx][ny] = J[cur[0]][cur[1]] + 1

    print("IMPOSSIBLE")
             
if __name__ == "__main__":
    main()
