import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,-2,2,-1,1]

    for _ in range(n):
        i = int(input())
        board = [[-1 for _ in range(i)] for _ in range(i)]
        x,y = map(int, input().split())
        goal_x, goal_y = map(int, input().split())
        if x==goal_x and y==goal_y:
            print(0)
            continue

        queue = deque()
        queue.append((x,y))
        board[x][y] = 0
        find = False
        while queue:
            cur = queue.popleft()
            for dir in range(8):
                nx = cur[0] + dx[dir]
                ny = cur[1] + dy[dir]
                if nx<0 or nx>=i or ny<0 or ny>=i:
                    continue
                if board[nx][ny]!=-1:
                    continue
                queue.append((nx,ny))
                board[nx][ny] = board[cur[0]][cur[1]] + 1
                if nx==goal_x and ny==goal_y:
                    print(board[nx][ny])
                    find = True
                    break
            if find:
                break
        
if __name__ == "__main__":
    main()
