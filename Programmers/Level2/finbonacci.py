def solution(n):
  dp = [0 for _ in range(n+1)]
  if n>=1: dp[1] = 1
  for i in range(2,n+1):
    dp[i] = (dp[i-1] + dp[i-2])%1234567
  return dp[n]
"""
dynamic programming 풀이법
1. 변수 만 써서 풀기
def solution(n):
  a,b = 0,1
  for _ in range(n):
    a, b = b, (a+b)%1234567
  return a
"""
