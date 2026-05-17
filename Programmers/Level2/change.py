from collections import deque

def solution(x, y, n):
  queue = deque([(x,0)])
  vis = set()
  while queue:
    cur, cnt = queue.popleft()
    if cur==y: return cnt
    for next in [cur*2, cur*3, cur+n]:
      if next>y: continue
      if next in vis: continue
      vis.add(next)
      queue.append((next, cnt+1))

  return -1
"""
간단한 BFS문제 풀이
"""
