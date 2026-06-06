def solution(A, B):
  answer = 0
  A.sort()
  B.sort()
  for a,b in zip(A,B):
    answer += a*b
  return answer
"""
그리디 문제풀이
가장 큰 숫자는 최대한 작은 숫자랑 곱하는 것이 가장 작은 수가 나올 것이다라는 가정에서 출발
1. Pythonic한 풀이
def solution(A,B):
  return sum(a*b for a,b in zip(sorted(A), sorted(B,reverse=True)))
"""
