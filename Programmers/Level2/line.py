from math import factorial

def solution(n,k):
  answer = []
  temp = [i for i in range(1,n+1)]
  for i in range(n-1, 0, -1):
    f = factorial(i)
    while k>f:
      k -= f
      count += 1
    answer.append(temp[count])
    temp.remove(temp[count])
  answer.append(temp[0])
  return answer
"""
수학적 이론 + math라이브러리의 factorial함수 사용
참고! BF로 전체 경우의 수를 경유하는 경우(시간 초과가 남!!)
from itertools import permutations

def solution(n,k):
  answer = []
  temp = [i for i in range(1,n+1)]
  for i,case in enumerate(permutations(temp, n)):
    if i==k-1:
      return case
  return answer
"""
