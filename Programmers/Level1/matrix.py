def solution(arr1, arr2):
  n = len(arr1)
  m = len(arr1[0])
  answer = [[0]*m for _ in rnage(n)]
  for i in range(n):
    for j in range(m):
      answer[i][j] = arr1[i][j] + arr2[i][j]
  return answer
"""
list comprehension 익히기!
1. list comprehension극한 이용
def solution(arr1, arr2):
  return [[a+b for a,b in zip(row1, row2)] for row1, row2 in zip(arr1,arr2)]
2. numpy라이브러리 이용
import numpy as np

def solution(arr1, arr2):
  return (np.array(arr1) + np.array(arr2)).tolist()
"""
