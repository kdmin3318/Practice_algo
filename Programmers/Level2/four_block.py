def solution(m,n,board):
  answer = 0
  dir = [(1,0), (0,1), (1,1)]
  board = [list(c) for c in board]
  
  def four(i,j):
    if board[i][j]=="0": return False
    for dx, dy in dir:
      nx, ny = i+dx, j+dy
      if board[nx][ny]!= board[i][j]: return False
    return True

  while True:
    possible = False
    vis = [[0]*n for _ in range(m)]
    for i in range(m-1):
      for j in range(n-1):
        if four(i,j):
          possible = True
          vis[i][j] = 1
          for dx,dy in dir:
            nx,ny = i+dx, j+dy
            vis[nx][ny] = 1
    if not possible: break
    answer += sum(sum(row) for row in vis)

    for j in range(n):
      col = [board[i][j] for i in range(m) if vis[i][j]!=1]
      col = ["0"]*(m-len(col)) + col
      for i in range(m):
        board[i][j] = col[i]

  return answer
"""
시뮬레이션 문제 풀이
"""
