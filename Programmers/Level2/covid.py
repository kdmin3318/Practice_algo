from collections import deque

def solution(places):
  answer = []
  dir = [(-1,0),(1,0),(0,-1),(0,1)]

  def bfs(board, x, y):
    queue = deque([(x,y,0)])
    vis = [[0]*5 for _ in range(5)]
    vis[x][y] = 1
    while queue:
      x,y,d = queue.popleft()
      if d==2: continue
      for dx, dy in dir:
        nx = x+dx
        ny = y+dy
        if nx<0 or nx>=5 or ny<0 or ny>=5: continue
        if vis[nx][ny] or board[nx][ny]=="X": continue
        if board[nx][ny]=="P": return False
        vis[nx][ny] = 1
        queue.append((nx,ny,d+1))
    return True

  for board in places:
    is_possible = True
    for i in range(5):
      for j in range(5):
        if board[i][j]=="P":
          if not bfs(board, i, j):
            is_possible = False
            break
        if not is_possible: break
    answer.append(int(is_possible))
  return answer
"""
bfs문제 풀이!
"""
