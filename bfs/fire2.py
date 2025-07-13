import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    for _ in range(n):
        w,h = map(int, input().split())
        F = [[0 for _ in range(w)] for _ in range(h)]
        S = [[0 for _ in range(w)] for _ in range(h)]
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        Q1 = deque()
        Q2 = deque()

        buliding = []
        for i in range(h):
            row = input().strip()
            buliding.append(row)
            for j in range(w):
                if row[j]=="*":
                    Q1.append((i,j))
                    F[i][j] = 1
                if row[j]=="@":
                    Q2.append((i,j))
                    S[i][j] = 1

        while Q1:
            cur = Q1.popleft()
            for dir in range(4):
                nx = cur[0] + dx[dir]
                ny = cur[1] + dy[dir]
                if nx<0 or nx>=h or ny<0 or ny>=w:
                    continue
                if F[nx][ny]!=0 or buliding[nx][ny]=="#":
                    continue
                Q1.append((nx,ny))
                F[nx][ny] = F[cur[0]][cur[1]] + 1
        
        find = False
        while Q2:
            cur = Q2.popleft()
            for dir in range(4):
                nx = cur[0] + dx[dir]
                ny = cur[1] + dy[dir]
                if nx<0 or nx>=h or ny<0 or ny>=w:
                    print(S[cur[0]][cur[1]])
                    find = True
                    break
                if S[nx][ny]!=0 or buliding[nx][ny]=="#":
                    continue
                if F[nx][ny]!=0 and F[nx][ny] <= S[cur[0]][cur[1]] + 1:
                    continue

                Q2.append((nx,ny))
                S[nx][ny] = S[cur[0]][cur[1]] + 1
                
            if find:
                break
        if not find:
            print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
