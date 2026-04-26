def solution(a, b):
  answer = 0
  for i,j in zip(a,b):
    answer += i*j
  return answer
"""
zip활용해서 문제 풀이
"""
