from collections import deque

def solution(info, n, m):
  answer = 121
  l = len(info)
  queue = deque()
  queue.append((0,0,0))
  visited = set()
  while queue:
    i,a,b = queue.popleft()
    if i==l: #끝까지 갔을때 a의 최소값 갱신
      answer = min(answer, a)
      continue

    if (i,a,b) in visited: #중복 계산 없애기(가지치기)
      continue
    visited.add((i,a,b))
    
    if a+info[i][0]<n:
      queue.append((i+1,a+info[i][0],b))
    if b+info[i][1]<m:
      queue.append((i+1,a,b+info[i][1]))
  return answer if answer!=121 else -1 #끝까지 못갔을 경우
"""
BFS + Pruning을 활용한 풀이 방법(O(2^n)으로 시간복잡도는 높음)
1. DP를 활용하여 풀이(O(n*m))
def solution(info, n, m):
    L = len(info)
    INF = float('inf')
    # dp[i][b]: 첫 i개 아이템을 처리했을 때, B의 누적 흔적이 b일 때 A의 최소 누적 흔적
    dp = [[INF] * m for _ in range(L + 1)]
    dp[0][0] = 0

    for i in range(L):
        a_cost, b_cost = info[i]
        for b in range(m):
            if dp[i][b] == INF:
                continue
            # Case 1: 아이템 i를 A가 맡는 경우
            new_a = dp[i][b] + a_cost
            if new_a < n:  # A의 흔적이 n 미만이어야 함
                dp[i + 1][b] = min(dp[i + 1][b], new_a)
            # Case 2: 아이템 i를 B가 맡는 경우
            new_b = b + b_cost
            if new_b < m:  # B의 흔적이 m 미만이어야 함
                dp[i + 1][new_b] = min(dp[i + 1][new_b], dp[i][b])

    ans = min(dp[L])
    return ans if ans != INF else -1
추가로 다익스트라(우선순위 큐)를 사용하는 방법도 존재함
"""
