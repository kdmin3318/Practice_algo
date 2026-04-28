def solution(s):
  answer = 0
  same, diff = 0,0
  for c in s:
    if same==0:
      same = 1
      temp = c
      continue

    if temp==c: same += 1
    else: diff += 1

    if same==diff:
      answer += 1
      same, diff = 0,0

  if same>0: answer += 1
  return answer
"""
for문 활용하여 문제 풀이
"""
