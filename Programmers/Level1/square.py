def solution(n):
  root = n**0.5
  if root%1==0: answer = (root+1)**2
  else: answer = -1
  return answer
"""
제곱 연산 활용
"""
