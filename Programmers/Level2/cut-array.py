def solution(n, left, right):
  answer = []
  def cal(col,row):
    if col>=row: return col+1
    else: return row+1
  for i in range(left, right+1):
    answer.append(cal(i//n,i%n))
  return answer
"""
수학적 이론을 활용한 문제풀이
1. max함수 활용
def solutin(n, left, right):
  for i in range(left, right+1):
    col = i//n
    row = i%n
    answer.append(max(col,row)+1)
  return answer
"""
