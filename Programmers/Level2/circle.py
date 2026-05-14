import math

def solution(r1, r2):
  answer = 0
  for i in range(1,r2+1):
    y_max = int((r2**2-i**2)**0.5)
    if i<r1:
      y_min = math.ceil((r1**2-i**2)**0.5)
    else:
      y_min = 0
    answer += y_max-y_min+1
  return answer*4
"""
math라이브러리 ceil올림 함수 활용
"""
