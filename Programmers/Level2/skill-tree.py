from collections import deque

def test(t, std):
  queue = deque(std)
  skill_set = set(std)

  for c in t:
    if not c in skill_set: continue
    if c != queue[0]: return 0
    queue.popleft()
  return 1

def solution(skill, skill_trees):
  answer = 0
  for tree in skill_trees:
    answer += test(tree, skill)
  return answer
"""
큐를 활용한 문제 풀이
"""
