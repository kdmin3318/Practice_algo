import math

def solution(n, a, b):
  answer = int(math.log2(n))
  while True:
    mid = n//2
    if (mid<b and mid>=a) or (mid<a and mid>=b):
      break
    if (mid<a and mid<b):
      a -= mid #왼쪽 그룹으로 이동
      b -= mid #왼쪽 그룹으로 이동
    n //= 2
    answer -= 1
  return answer
"""
이진 탐색을 활용하여 풀이
1. 만날 때까지 라운드를 직접 올리기
def solution(n, a, b):
  answer = 0
  a,b = a-1, b-1
  while a!=b:
    a //=2
    b //=2
    answer += 1
  return answer
2. 비트 연산자 활용
def solution(n, a, b):
  return ((a-1)^(b-1)).bit_length()
"""
