from collections import deque

def bracket(string):
  stack = []
  for c in string:
    if c=="(" or c=="{" or c=="[": stack.append(c)
    elif c==")":
      if not stack: return 0
      if stack[-1]!="(": return 0
      stack.pop()
    elif c=="}":
      if not stack: return 0
      if stack[-1]!="{": return 0
      stack.pop()
    elif c=="]":
      if not stack: return 0
      if stack[-1]!="[": return 0
      stack.pop()
  if stack: return 0
  return 1

def solution(s):
  answer = 0
  queue = deque(list(s))
  n = len(queue)
  for _ in range(n):
    answer += bracket(queue)
    queue.append(queue.popleft())
  return answer
"""
스택 + 큐를 활용한 문제 풀이 올바른 괄호 맞추기!
"""
