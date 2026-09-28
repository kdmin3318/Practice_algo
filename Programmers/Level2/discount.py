from collections import Counter

def solution(want, number, discount):
  answer = 0
  temp = dict(zip(want, number))
  my_want = Counter(temp)

  l = len(discount)
  for i in range(0,l-9):
    count = Counter(discount[i:i+10])
    if my_want==count: answer += 1
  return answer
"""
해싱 문제(Counter 함수 활용)
"""
