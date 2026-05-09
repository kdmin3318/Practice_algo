def solution(n):
  answer = 0
  while n>0:
    if n%2==0: n //= 2
    else:
      n -= 1
      answer += 1
  return answer
"""
그리디 문제 풀이법(도착 지점을 기준으로 반대로 추적)
1. 비트 연산자를 활용하여 풀이
1101 이라고 가정했을때, 2의 지수 승까지의 이동이 1의 개수랑 같음
def solution(n):
  return bin(n).count('1')

2. dp를 활용 하여 풀이(dp를 활용하면 공간, 시간 복잡도가 높아서 오답으로 나옴..)
def solution(n):
  dp = [0]*(2*n+1)
  dp[1] = 1
  for i in range(1,n+1):
    if not dp[2*i]: dp[2*i] = dp[i]
    if not dp[i+1]: dp[i+1] = dp[i+1] + 1
  return dp[n]
"""
