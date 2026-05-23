def solution(n):
  answer = 0
  for i in range(1,n+1);
    j = i+1
    s = i
    while s<n:
      s += j
      j += 1
    if s==n:
      answer += 1
  return answer
"""
BF풀이 방법(O(n^2)으로 시간 복잡도가 높음)
1. 투 포인터
def solution(n):
  answer = 0
  left, right = 1,1
  current_sum = 0
  while left<=n:
    if current_sum < n:
      current_sum += right
      right += 1
    elif current_sum > n:
      current_sum -= left
      left += 1
    else:
      current_sum -= left
      left += 1
      answer += 1
  return answer
2. 수학적 이론(약수중 홀수 인 것의 개수!)
def solution(n):
  return len([i for i in range(1,n+1,2) if n%i==0])
"""
