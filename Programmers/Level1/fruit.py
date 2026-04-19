def solution(k,m,score):
  answer = 0
  score.sort(reverse=True)
  n = len(score)
  for i range(n//m):
    answer += m*score[(i+1)*m-1)]
  return answer
"""
Slicing이용하기!
def solution(k,m,score):
  answer = 0
  score.sort(reverse=True)
  for i range(m-1, len(score), m):
    answer += m*score[i]
  return answer
"""
