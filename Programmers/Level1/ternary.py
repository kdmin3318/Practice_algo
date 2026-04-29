def ternary(n):
  temp = ''
  while n>0:
    temp += str(n%3)
    n //= 3
  return temp
def solution(n):
  return int(ternary(n), 3)
"""
int함수로 10진수로 간단하게 변환이 가능!!
"""
