from collections import deque

def solution(maps):
  move = [(-1,0),(1,0),(0,-1),(0,1)]
  
  n = len(maps)
  m = len(maps[0])
  vis = [[0]*m for _ in range(n)]
  queue = deque([(0,0)])
  vis[0][0] = 1
  while queue:
    x,y = queue.popleft()
    for dx, dy in move:
      nx = x + dx
      ny = y + dy
      if nx<0 or nx>=n or ny<0 or ny>=m: continue
      if maps[nx][ny]==0 or vis[nx][ny]: continue
      vis[nx][ny] = vis[x][y]+1
      queue.append((nx,ny))
  answer = vis[n-1][m-1] if vis[n-1][m-1] else -1
  return answer
"""
BFS문제 풀이
"""
