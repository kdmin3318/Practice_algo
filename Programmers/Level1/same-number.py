def solution(arr):
  answer = []
  for n in arr:
    if not answer or n!=answer[-1]:
      answer.append(n)
  return answer
"""
리스트 순회를 이용하여 풀이!
"""
