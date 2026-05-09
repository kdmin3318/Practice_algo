def prime(num):
  if num==1: return 0
  temp = 1
  for i in range(2, int(num**0.5)+1):
    if num%i==0:
      # 가장 작은 약수의 n//i는 가장 큰 약수기 때문에 n//i를 반환함
      if num//i <= 10000000:
        return num//i
      # 천만 보다 크다면 일단 가장 작은 약수를 가지고 다음으로 넘어감
      temp = i
  return temp

def solution(begin, end):
  answer = [prime(i) for i in range(begin, end+1)]
  return answer
"""
그리디 문제 풀이
가장 큰 약수를 구할 때는 가장 작은 약수만 구해도 가장 큰 약수를 구할 수 있음!!
그리고 규칙을 정리해봤을때 해당 숫자의 가장 큰 약수 가 마지막에 덮어 씌워진다 라는 가정이 맞다는 것에서 출발
"""
