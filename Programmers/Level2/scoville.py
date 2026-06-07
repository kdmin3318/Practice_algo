import heapq

def solution(scoville, K):
  answer = 0
  heapq.heapify(scoville)
  while len(scoville)>=2 and scoville[0]<K:
    a = heapq.heappop(scoville)
    b = heapq.heappop(scoville)
    temp = a+b*2
    heapq.heappush(scoville, temp)
    answer += 1
  if scoville[0]<K: return -1
  return answer
"""
우선순위 큐를 활용한 문제 풀이
"""
