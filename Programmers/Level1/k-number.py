def solution(array, commands):
  answer = []
  for i,j,k in commands:
    temp = [t for t in array[i-1:j]]
    temp.sort()
    answer.append(temp[k-1])
  return answer
"""
리스트 slicing과 comprehension의 활용 풀이
1. sorted를 이용
def solution(array, commands):
  answer = []
  for i,j,k in commands:
    temp = sorted(array[i-1:j])
    answer.append(temp[k-1])
  return answer

2. list comprehension극한 사용
def solution(array, commands):
  return [sorted(array[i-1:j])[k-1] for i,j,k in commands]
"""
