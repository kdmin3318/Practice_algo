from itertools import combinations

def is_prime(n):
  if n<2: return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0: return False
  return True

def solution(nums):
  answer = 0
  for a in combinations(nums,3):
    if is_prime(sum(a)): answer+=1
  return answer
"""
itertools.combinations를 활용하여 풀이
1. combinations을 안쓴다면 삼중 for문으로 순회하여 풀어야함!
for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      total = nums[i] + nums[j] + nums[k]
2. DFS를 이용하여 combination구현하기(재귀이용)
def combine(arr, n):
  result = []
  if n==0: return [[]]

  for i in range(len(arr)):
    elem = arr[i]
    for rest in combine(arr[i+1:], n-1):
      result.append([elem}+rest)
  return result
"""
