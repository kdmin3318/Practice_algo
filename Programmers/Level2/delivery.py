def solution(N, road, K):
  graph = [[] for _ in range(N+1)]
  for u,v,e in road:
    graph[u].append((v,e))
    graph[v].append((u,e))
  stack = [(1,0)]
  possible = {1}
  vis = [-1]*(N+1)
  vis[1] = 0
  while stack:
    cur, cost = stack.pop()
    for next, edge in graph[cur]:
      if vis[next]!=-1 and vis[next]<cost+edge: continue
      if cost+edge > K: continue
      vis[next] = cost+edge
      stack.append((next, cost+edge))
      possible.add(next)
  answer = len(possible)
  return answer
"""
DFS 풀이 방법
1. 다익스트라로 풀이 가능
import heapq

def solution(N, road, K):
  graph = [[] for _ in range(N+1)]
  for u,v,e in road:
    graph[u].append((v,e))
    graph[v].append((u,e))
  hp = [(0,1)]
  vis = [-1]*(N+1)
  vis[1] = 0
  possible = {1}
  while hq:
    cost, cur = heapq.heappop(hq)
    for next, edge in graph[cur]:
      if vis[next]!=-1 and vis[next]<cost+edge: continue
      if cost+edge>K: continue
      vis[next] = cost+edge
      heapq.heappush(hq, (cost+edge,next))
      possible.add(next)
  answer = len(possible)
  return answer
"""
