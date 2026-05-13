from collections import deque

def solution(cacheSize, cities):
  if cacheSize==0:
    return len(cities)*5

  answer = 0
  queue = deque(maxlen=cacheSize)
  for city in cities:
    city = city.lower()
    if city in queue:
      answer += 1
      queue.remove(city)
      queue.append(city)
    else:
      answer += 5
      queue.append(city)
  return answer
"""
queue를 활용한 문제 풀이
참고! deque에 maxlen을 지정해두면 append시에 maxlen을 넘을경우 자동으로 popleft를 실행함!!
"""
