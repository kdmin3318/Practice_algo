from collections import Counter

def solution(str1, str2):
  def get_multiset(s):
    temp = []
    s = s.lower()
    for i in range(len(s)-1):
      if s[i].isalpha() and s[i+1].isalpha():
        temp.append(s[i]+s[i+1])
    return temp

  c1 = Counter(get_multiset(str1))
  c2 = Counter(get_multiset(str2))

  intersection = sum((c1&c2).values())
  union = sum((c1|c2).values())

  if union==0: return 65536
  return int(intersection/union*65536)
"""
다중 집합의 교집합과 합집합을 구하는 문제
참고! Counter 함수는 기본적으로 다중집합의 교집합 합집합을 지원함!, set은 단일 집합!!
1. Counter를 쓰지 않고 구현
def get_cal(arr1, arr2):
  intersection = 0
  for c in arr1:
    if c in arr2:
      arr2.remove(c)
      intersection += 1
  union = len(arr1) + len(arr2)
  return intersection, union

def solution(str1, str2):
  def get_multiset(s):
    temp = []
    s = s.lower()
    for i in range(len(s)-1):
      if s[i].isalpha() and s[i+1].isalpha():
        temp.append(s[i]+s[i+1])
    return temp
  str1 = get_multiset(str1)
  str2 = get_multiset(str2)
  intersection, union = get_cal(str1, str2)
  if union==0: return 65536
  return int(intersection/union*65536)
  """
