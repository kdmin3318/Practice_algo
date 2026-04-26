def solution(a, b):
  answer = 0
  (a,b) = (a,b) if a<b else (b,a)
  for i in range(a,b+1):
    answer += i
  return answer
"""
for문의 범위 range로 조절하여 풀이!
1. 등차수열 합공식 이용하기
def solution(a, b):
  return ((a+b) * (abs(a-b)+1))//2
"""
