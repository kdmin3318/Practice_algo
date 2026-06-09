from collections import defaultdict

def solution(edges):
  graph = defaultdict(list)
  in_degree = defaultdict(int)
  out_degree = defaultdict(int)
  for u,v in edges:
    graph[u].append(v)
    in_degree[v] += 1
    out_degree[u] += 1

  candidates = [node for node in out_degree if in_degree[node]==0]
  if not candidates:
    return [0,0,0,0]

  entry_node = max(candidates, key=lambda x: out_degree[x])
  if not graph[entry_node]:
    return [entry_node,0,0,0]

  visited_global = set()
  dount = bar = eight = 0

  def dfs(start_node):
    stack = [start_node]
    visited_local = set()
    revisited_count = 0
    
    while stack:
      cur = stack.pop()
      if cur in visited_local: 
        revisited_count += 1
        continue
      visited_local.add(cur)
      visited_global.add(cur)
      for next in graph[cur]:
        stack.append(next)
    return revisited_count

  for next_node in graph[entry_node]:
    if next_node in visited_global:
      continue
    revisited_count = dfs(next_node)
    if revisited_count==0: bar += 1
    elif revisited_count==1: dount+=1
    else: eight += 1

  return [entry_node, dount, bar, eight]
"""
시뮬 + 그리디 + DFS 문제 풀이..
1. 그리디(차수 풀이로 풀이 가능)
def solution(edges):
  degree = {}
  for u,v in edges:
    if u not in degree: degree[u] = [0,0]
    if v not in degree: degree[v] = [0,0]
    degree[u][1] += 1
    degree[v][0] += 1

  created_node = 0
  stick_cnt = 0
  eight_cnt = 0

  for node, (in_deg, out_deg) in degree.items():
    if in_deg==0 and out_deg >=2:
      created_node = node
    elif out_deg==0: stick_cnt += 1
    elif out_deg==2: eight_cnt += 1

  total_graphs = degree[created_node][1]
  dount_cnt = total_graphs - stick_cnt - eight_cnt

  return [created_node, dount_cnt, stick_cnt, eight_cnt]
"""
