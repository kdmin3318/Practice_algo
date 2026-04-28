def solution(s):
  n = len(s)
  if n%2==0:
    answer = s[n//2-1:n//2+1]
  else:
    answer = s[n//2]
"""
len함수 활용
"""
