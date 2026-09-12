def solution(numbers):
  answer = set()
  l = len(numbers)
  for i in range(l-1):
    for j in range(i+1,l):
      answer.add(numbers[i]+numbers[j])
  return sorted(answer)
"""
set() 으로 중복 제거
1. combinations 활용
from itertools import combinations

def solution(numbers):
  return sorted({a+b for a,b in combinations(numbers,2)})
"""
