def solution(n, wires):
  def dfs(i, graph):
    vis = [0]*(n+1)
    vis[i] = 1
    stack = [i]
    dis = 0
    while stack:
      cur = stack.pop()
      dis += 1
      for next in graph[cur]:
        if vis[next]: continue
        vis[next] = 1
        stack.append(next)
    return dis

  answer = n
  for cur_u, cur_v in wires:
    #그래프 초기화
    graph = [[] for _ in range(n+1)]
    for u,v in wires:
      if (u==cur_u and v==cur_v) or (u==cur_v and v==cur_u):
        continue
    part_size = dfs(1,graph)
    diff = abs((n-part_size)-part_size)
    answer = min(answer, diff)

  return answer
"""
BF와 DFS를 조합하여 풀기!
모든 송전탑의 구간을 짜르고 dfs로 깊이 탐색 후 구간 차이를 하나하나 구하기
1. 그래프를 한번만 그리기(dfs에서 무시할 전선 정보를 넘기기)
def solution(n, wires):
  graph = [[] for _ in range(n+1)]
  for u,v in wires:
    graph[u].append(v)
    graph[v].append(u)

  def dfs(i, skip_u, skip_v):
    vis = [0]*(n+1)
    vis[i] = 1
    dis = 0
    stack = [i]
    while stack:
      cur = stack.pop()
      dis += 1
      for next in graph[cur]:
        if (cur==skip_u and next==skip_v) or (cur==skip_v and next==skip_u):
          continue
        if vis[next]: continue
        vis[next] = 1
        stack.append(next)
    return dis

  answer = n
  for u,v in wires:
    size = dfs(1, u, v)
    answer = min(answer, abs(n-2*size))
  return answer
결과적으로 시간 복잡도는 똑같긴함!
"""
