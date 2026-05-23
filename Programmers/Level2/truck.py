from collections import deque

def solution(bridge_length, weight, truck_weights):
  answer = 0
  queue = deque([0]*brdige_length)
  w = 0
  for truck in truck_weights:
    while True:
      w -= queue.popleft()
      answer += 1

      if w+truck <= weight:
        queue.append(truck)
        w += truck
        break
      else:
        queue.append(0)
  return answer + bridge_length
"""
시뮬레이션 + 큐 활용 문제
"""
