def solution(clothes):
  closet = {}
  for name,kind in clothes:
    closet[kind] = closet.get(kind, 0) + 1

  answer = 1
  for i in closet.values():
    answer *= (i+1)
  return answer - 1
"""
딕셔너리 해시, 경우의 수(수학적 정의) 활용하여 문제 풀이
1. Counter활용
from collections import Counter
def solution(clothes):
  answer = 1
  count = Counter(clothes[i][1] for i in range(len(clothes)))
  for kind in count:
    answer *= (count[kind]+1)
  return answer-1
"""
