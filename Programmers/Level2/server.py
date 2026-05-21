def solution(players, m, k):
  answer = 0
  n = len(players)
  server = {i:0 for i in range(n)}
  for i,p in enumerate(players):
    if p//m>server[i]:
      need_server = p//m-server[i]
      for j in range(k):
        if i+j==n: break
        server[i+k] += need_server
      answer += need_server
  return answer
"""
시뮬레이션 + 딕셔너리 문제(딕셔너리를 전부 탐색히야하므로 O(n*k)시간복잡도가 나옴)
1. queue를 활용한 문제 풀이(O(n))
from collections import deque

def solution(players, m, k):
    answer = 0 
    current_servers = 0 
    expired_queue = deque()

    for i, p in enumerate(players):
        while expired_queue and expired_queue[0][0] == i:
            time, count = expired_queue.popleft()
            current_servers -= count

        required_servers = p // m

        if required_servers > current_servers:
            need_server = required_servers - current_servers
            answer += need_server
            current_servers += need_server

            expired_queue.append((i + k, need_server))
            
    return answer
"""
