def solution(number):
  answer = 0
  n = len(number)
  for i in range(n-2):
    for j in range(i+1,n-1):
      target = -number[i]-number[j]
      answer += number[j+1:].count(target)
  return answer
"""
이중 for문과 count를 사용한 풀이 사실상 O(n^3)이랑 같음
1. itertools의 combinations사용
def solution(number):
  from itertools import combinations
  answer = 0
  for i in combinations(number, 3):
    if sum(i)==0: answer += 1
  return answer
"""
