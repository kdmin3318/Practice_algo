import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y,selected,board):
    queue = deque()
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    vis = [[0]*5 for _ in range(5)]
    som = 0
    check = 0

    queue.append((x,y))
    vis[x][y] = 1
    if(board[x][y]=='S'): som += 1
    while queue:
        check += 1
        cx, cy = queue.popleft()
        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]
            if nx<0 or nx>=5 or ny<0 or ny>=5: continue
            if selected[nx][ny]!=1: continue
            if vis[nx][ny]==1: continue
            vis[nx][ny] = 1
            if board[nx][ny]=='S': som+=1
            queue.append((nx,ny))

    if check==7:
        if som>=4: return True
    return False

def solve(k, idx, selected, board):
    if k==7:
        for i in range(5):
            for j in range(5):
                if selected[i][j]==1:
                    if bfs(i,j,selected,board): return 1
                    return 0

    
    if idx==25: return 0

    x = idx//5
    y = idx%5

    selected[x][y] = 1
    result = solve(k+1,idx+1,selected,board)
    selected[x][y] = 0

    result += solve(k,idx+1,selected,board)

    return result

def main():
    board = [list(input().strip()) for _ in range(5)]
    selected = [[0]*5 for _ in range(5)]
    cnt = solve(0,0,selected,board)
    print(cnt)

if __name__ == "__main__":
    main()
