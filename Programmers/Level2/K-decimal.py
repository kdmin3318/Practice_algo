def decimal(num, k):
  temp = ""
  while num>0:
    temp = str(num%k) + temp
    num //= k
  return temp

def prime(num):
  if num<2: return 0
  for i in range(2, int(num**0.5)+1):
    if num%i==0: return 0
  return 1

def solution(n, k):
  answer = 0
  temp = ""
  for i in decimal(n,k):
    if i=="0":
      if temp and prime(int(temp)): answer += 1
      temp = ""
    else:
      temp += i
  if temp and prime(int(temp)): answer += 1
  return answer
"""
문제를 코드로 옮기는 시뮬레이션과 모든 경우의 수를 커버히는 BF 문제 풀이
참고!
1. Sentimel 기법을 활용하여 마지막 숫자 처리!
def soltuion(n,k):
  answer = 0
  temp = ""
  converted = decimal(n,k) + "0"
  for i in converted:
    if i==0:
      if temp and prime(int(temp)): answer += 1
      temp = ""
    else:
      temp += i
"""
