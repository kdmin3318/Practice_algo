def solution(nums):
  n = len(nums)//2
  pokemon = len(set(nums))
  return min(n,pokemon)
"""
가질수 있는 포켓몬과 포켓몬 종류중 작은것이 무조건 정답이라는 초급 그리디 문제풀이
"""
