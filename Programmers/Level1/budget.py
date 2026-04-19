def solution(d, budget):
  answer = 0
  d.sort()
  while answer<len(d) and budget>=d[answer]:
    budget -= d[answer]
    answer+=1
  return answer
"""
while문에서 or과 and차이 조심하기!
1. for문으로 풀기
def solution(d, budget):
  answer = 0
  d.sort()
  for i in d:
    if budget<i: break
    budget -= i
    answer += 1
  return ansewr
2. 그리디 풀이방식(O(n^2으로 비효율적임..)
def solution(d, budget):
  d.sort()
  while sum(d)>budget:
    d.pop(-1)
  answer = len(d)
  return answer
"""
