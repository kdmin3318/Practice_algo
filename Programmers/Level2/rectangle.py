def gcd(a,b):
  a,b = (a,b) if a>b else (b,a)
  for i in range(a,0,-1):
    if a%i==0 and b%i==0:
      return i
  return 1

def solution(w,h):
  answer = w*h
  g = gcd(w,h)
  w //= g
  h //= g
  return answer-(w+h-1)*g
"""
수학적 지식(기하학 및 정수론)을 활용하여 문제
1. maht라이브러리 gcd함수 활용
import math
def soltuion(w,h):
  g = math.gcd(w,h)
  x,y = w//g, h//g
  return w*h+(x+y-1)*g
"""
