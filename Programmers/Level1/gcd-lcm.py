def gcd(a,b):
  a,b = (a,b) if a<b else (b,a)
  for i in range(a,0,-1):
    if a%i==0 and b%i==0: return i

def lcm(a,b):
  a,b = (a,b) if a<b else (b,a)
  for i in range(b,b*a+1):
    if i%a==0 and i%b==0: return i

def solution(n, m):
  answer = []
  answer.append(gcd(n,m))
  answer.append(lcm(n,m))
  return answer
"""
수학적 이론 구현(최대공약수, 최소 공배수)
1. 유클리드 호제법
def gcd(a,b):
  while b:
    a,b = b, a%b
  return a

def solution(n, m):
  g = gcd(n,m)
  l = (n*m)//g
  return [g,l]

2. math라이브러리 활용
import math

def solution(n,m):
  return [math.gcd(n,m), math.lcm(n,m)]
"""
