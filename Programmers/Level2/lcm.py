import math

def solution(arr):
  return math.lcm(*arr)
"""
math라이브러리를 활용하여 간단하게 풀이가능
1. math라이브러리를 못쓸때 최소 공배수 구하기
def get_gcd(a,b):
  while b>0:
    a,b = b,a%b
  return a

def get_lcm(a,b):
  return (a//get_gcd(a,b))*b

def solution(arr):
  answer = arr[0]
  for i in arr[1:]:
    answer = get_lcm(answer, i)
  return answer
"""
