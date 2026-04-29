def solution(wallpaper):
  n = len(wallpaper)
  m = len(wallpaper[0])
  min_x, min_y, max_x, max_y = n,m,0,0
  for i in range(n):
    for j in range(m):
      if wallpaper[i][j]=="#":
        min_x = min(i,min_x)
        min_y = min(j,min_y)
        max_x = max(i+1, max_x)
        max_y = max(j+1, max_y)
  return [min_x, min_y, max_x, max_y]
"""
BF 초급 문제 풀이
"""
