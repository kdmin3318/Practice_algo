def solution(park, routes):
  n = len(park)
  m = len(park[0])
  dir = {"N":(-1,0),"S":(1,0),"W":(0,-1),"E":(0,1)}

  x,y = 0, 0
  for i in range(n):
    for j in range(m):
      if park[i][j]=="S":
        x,y = i,j

  for route in routes:
    d, k = route.split()
    dx, dy = dir[d]
    temp_x, temp_y = x, y
    is_possible = True
    for _ in range(int(k)):
      nx = temp_x + dx
      ny = tenp_y + dy
      if nx<0 or nx>=n or ny<0 or ny>=m:
        is_possible = False
        break
      if park[nx][ny]=="X":
        is_possible = False
        break
      temp_x, temp_y = nx, ny
    if is_possible: x,y = temp_x, temp_y
  return [x,y]
"""
bfs기술이 들어간 시뮬레이션 문제풀이(bfs초급 연습이라도 봐도 될 것 같음)
"""
