def solution(n):
  answer = []
  def hanoi(n, start, end, sub):
    if n==1:
      answer.append([start, end])
      return
    hanoi(n-1,start, sub, end)
    answer.append([start, end])
    hanoi(n-1,sub, end, start)
  hanoi(n,1,3,2)
  return answer
"""
recursion문제 풀이
"""
