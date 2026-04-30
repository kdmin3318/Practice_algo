def solution(n):
  d = [0]*(n+1)
  d[1] = 1
  d[2] = 2
  for i in range(3,n+1):
    d[i] = (d[i-1] + d[i-2])%1000000007
  return d[n]
"""
DP기초 문제 풀이!!
마지막 타일을 세로로 두는 경우 앞의 타일을 d[i-1]경우의 수로 만들 수 있음
마지막 타일을 가로로 두는 경우 앞의 타일을 d[i-2]경우의 수로 만들 수 있음
1. 공간 복잡도 O(1)로 줄이기
def solution(n):
  a,b = 1,2
  if n<=2: return n

  for _ in range(3, n+1):
    a,b = b, (a+b)%1000000007
  return b
"""
