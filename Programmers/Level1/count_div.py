def counter_div(n):
  count = 0
  for i in range(1,n//2+1):
    if n%i==0: count+=1
  count+=1
  return count

def solution(left, right):
  answer = 0
  for n in range(left, right+1):
    temp = counter_div(n)
    answer += n if temp%2==0 else -n
  return answer
"""
O(N^2), BF풀이법 모든 경우의 수 직접 계산
1. 수학적 이론 사용(완전제곱수만 약수의 개수가 홀수 임을 이용)
def solution(left, right):
  answer = 0
  for n in range(left, right+1):
    root = int(n**0.5)
    if n==root**2: answer -= n
    else: answer += n
  return answer
"""
