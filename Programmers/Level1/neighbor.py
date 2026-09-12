def solution(board, h, w):
  answer = 0
  n,m = len(board), len(board[0])
  dir = [(-1,0), (1,0), (0,-1), (0,1)]
  for dx, dy in dir:
    nx = h + dx
    ny = w + dy
    if nx<0 or nx>=n or ny<0 or ny>=m: continue
    if board[nx][ny] == board[h][w]:
      answer += 1
  return answer
"""
dfs 기초 문제
"""
