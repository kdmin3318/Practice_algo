import heapq

def solution(k, score):
  answer = []
  pq = []
  for c in score:
    heapq.heappush(pq, c)
    if len(pq)>k:
      heapq.heappop(pq)
    answer.append(pq[0])
  return answer
"""
우선순위 큐를 활용한 문제 풀이
"""
