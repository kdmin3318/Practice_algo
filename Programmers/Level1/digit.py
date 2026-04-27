def solution(n):
  answer = 0
  while n>0:
    answer += n%10
    n //= 10
  return answer
"""
while문을 활용하여 문제 풀이
1. Pythonic한 풀이
def solution(n):
  return sum(int(i) for i in str(n))
2. divmod 함수 활용(몫과 나머지를 뱉는 함수)
def solution(n):
  answer = 0
  while n>0:
    n, remainder = divmod(n, 10)
    answer += remainder
  return answer
"""
