def solution(dirs):
  move = {"U":(0,1), "D":(0,-1), "L":(-1,0), "R":(1,0)}
  x,y = 5,5
  vis = set()
  answer = 0
  for d in dirs:
    dx, dy = move[d]
    nx, ny = x+dx, y+dy
    if nx<0 or nx>=11 or ny<0 or ny>=11: continue
    if not (x,y,nx,ny) in vis:
      answer += 1
      vis.add((x,y,nx,ny))
      vis.add((nx,ny,x,y))
    x,y = nx, ny
  return answer
"""
set()를 활용함으로 탐색 속도를 O(1)로 줄여서 풀이
"""
