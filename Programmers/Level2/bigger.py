def solution(n):
  a = bin(n)[2:].count('1')
  while True:
    n += 1
    b = bin(n)[2:].count('1')
    if a==b: break
  return n
"""
bin()함수 활용
1. 비트 연산으로 풀기(2의 보수의 특성 활용
def solution(n):
  right_one = n&-n #가장 오른쪽 1

  next_num = n + right_one #가장 오른쪽 1를 올림 처리
  
  onns = n^next_num #right_one했을떄 올라갔던 자리가 1로 나옴
  ones = (ones//right_one) >> 2

  return next_num | ones
"""
