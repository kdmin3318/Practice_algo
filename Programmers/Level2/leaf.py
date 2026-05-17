from collections import deque

def solution(dist_limit, split_limit):
  #queue에 (현재 분배도, 현재까지 쓴 분배노드 수, 현재 리프 수, 현재 층 가용 노드 수) 저장
  queue = deque([(1,0,1,1)])

  visited = {}
  max_overall_leaves = 1

  while queue:
    split, used, leaves, available = queue.popleft()
    max_overall_leaves = max(max_overall_leaves, leaves)

    # 더 쪼갤 수 있는 선택지(2배 또는 3배)
    for s in [2,3]:
      next_split = split * s
      if next_split > split_limit: continue

      # 그리디 하게 전부 아니면 남은 전부를 씀..
      k = min(availalbe, dist_limit - used)
      if k<=0: continue

      next_used = used+k
      next_leaves = leaves + k*(s-1)
      next_availble = k*s

      #가지치기 부분
      state = (next_split)
      if state in visited:
        prev_leaves, prev_used = visited[state]
        if next_leaves <= prev_leaves and next_used >= prev_used:
          continue
      visited[state] = (next_leaves, next_used)
      queue.append((next_split, next_used, next_leaves, next_available))

  return max_overall_leaves
"""
BFS를 바탕으로 그리디(greedy)와 Pruning을 활용하여 풀이..
"""
