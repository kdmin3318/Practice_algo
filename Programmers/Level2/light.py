from collections import deque

def solutioin(grid):
  n = len(grid)
  m = len(grid[0])
  move = [(-1,0),(0,1),(1,0),(0,-1)] #상우하좌
  vis = [[[0]*4 for _ in range(m)] for _ in range(n)]

  def bfs(i,j,dir):
    x,y,d = i,j,d
    cycle = 0
    while True:
      if vis[x][y][d]:
        break
      vis[x][y][d] = 1 #해당 노드에 들어오는 방향으로 체크
      cycle += 1
      if c=="L": d = (d+3)%4 #상 방향이였다면 좌 방향으로 틀어야함
      elif c=="R": d= (d+1)%4 #상 방향이였다면 우 방향으로 틀어야함
      dx, dy = move[d]
      x = (x+dx)%n
      y = (y+dy)%m

  answer = []
  for i in range(n):
    for j in range(m)
      for dir in range(4):
        if vis[i][j][dir]==0:
          answer.append(bfs(i,j,dir))
  return answer
"""
방향성을 추가한 DFS문제 풀이
"""
