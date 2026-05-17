def solution(n):
  answer = list(str(n))
  answer.reverse()
  return list(map(int,answer))
"""
reverse()함수 이해하기
1. 문자열 특성 이용하기
def solution(n):
  return [int(x) for x in str(x)[::-1]]
"""
