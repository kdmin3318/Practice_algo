from collections import deque

def solution(board):
  n = len(board)
  m = len(board[0])
  move = [(-1,0),(1,0),(0,-1),(0,1)]
  vis = [[0]*m for _ in range(n)]
  def bfs(i,j):
    queue = deque([(i,j)])
    vis[i][j] = 1
    while queue:
      x,y = queue.popleft()
      if board[x][y]=="G": return vis[x][y]-1
      for dx, dy in move:
        nx, ny = x,y
        while True:
          nx += dx
          ny += dy
          if nx<0 or nx>=n or ny<0 or ny>=m: break
          if board[nx][ny]=="D": break
        nx, ny = nx-dx, ny-dy
        if vis[nx][ny]: continue
        vis[nx][ny] = vis[x][y] + 1
        queue.append((nx,ny))
    return -1
  for i in range(n):
    for j in range(m):
      if board[i][j]=="R":
        answer = bfs(i,j)
        break
  return answer
"""
BFS문제 풀이!
"""
