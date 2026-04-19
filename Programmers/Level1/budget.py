def solution(d, budget):
  answer = 0
  d.sort()
  while answer<len(d) and budget>=d[answer]:
    budget -= d[answer]
    answer+=1
  return answer
"""
while문에서 or과 and차이 조심하기!
for문으로 풀기
def solution(d, budget):
  answer = 0
  d.sort()
  for i in d:
    if budget<i: break
    budget -= i
    answer += 1
  return ansewr
"""
