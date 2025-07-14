import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    board = [list(map(int, input().strip())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    queue = deque()
    count = 0
    size = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queue.append((i, j))
                board[i][j] = 0
                count += 1
                s = 0
                
                while queue:
                    x, y = queue.popleft()
                    s += 1
                    
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if board[nx][ny] != 1:
                            continue
                        
                        queue.append((nx, ny))
                        board[nx][ny] = 0
                
                size.append(s)
    
    print(count)
    size.sort()
    for i in range(len(size)):
        print(size[i])

if __name__ == "__main__":
    main()
