from itertools import product
from collections import deque

def solution(n, infection, edges, k):
  answer = 0
  graph = [[] for _ in range(n+1)]
  for u,v,type in edges:
    graph[u].append((v,type))
    graph[v].append((u,type))
  types = [1,2,3]
  for case in product(types, repeat=k):
    infect = [0]*(n+1)
    infect[infection] = 1
    for t in case:
      queue = deque()
      for i in range(n+1):
        if infect[i]==1: queue.append(i)
      while queue:
        u = queue.popleft()
        for v,type in graph[u]:
          if type!=t: continue
          if infect[v]==1: continue
          infect[v] = 1
          queue.append(v)
    answer = max(answer, sum(infect))
  return answer
"""
product, deque라이브러리 사용
BF + BFS문제 풀이!(BF로 모든 경우의 수를 돌기 때문에 시간 복잡도가 높음!)
1. BFS+DP(Top-down DP방식)으로 시간복잡도를 줄일 수 있음

def solution(n, infection, edges, k):
  graph = {1: [[] for _ in range(n+1)],
    2: [[] for _ in range(n+1)],
    3: [[] for _ in range(n+1)]}

  for u,v,t in edges:
    graph[t][u].append(v)
    graph[t][v].append(u)

  memo = {}

  def get_max_infected(current_infect, remaining_k):
    if remaining_k==0: return sum(current_infect)

    state = (tuple(current_infect), remaining_k)
    if state in memo: return memo[state]

    max_result = 0
    for next_t in [1,2,3]:
      next_infect = list(current_infect)
      queue = [i for i in range(1,n+1) if next_infect[i]==1]
      for u in queue:
        for v in graph[next_t][u]:
          if next_infect[v]==0:
            next_infect[v]=1
            queue.append(v)

      max_result = max(max_result, get_max_infected(next_infect, remaining_k-1))
    memo[state] = max_result
    return max_result

  start_infect = [0]*(n+1)
  start_infect[infection] = 1

  return get_max_infected(start_infect, k)
"""
