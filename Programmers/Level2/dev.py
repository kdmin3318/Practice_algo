from math import ceil

def solution(progresses, speeds):
  answer = []
  temp = []
  for p,s in zip(progresses, speeds):
    temp.append(ceil((100-p)/s))
  n = len(temp)
  i = 0
  while i!=n:
    j = i+1
    while j<n and temp[i]>=temp[j]:
      j += 1
    answer.append(j-i)
    i = j
  return answer
"""
시뮬레이션 문제!
1. queue 활용(문제의 의도 대로 큐를 활용, 비추천..)
from collections import deque
from math import ceil

def solution(progresses, speeds):
  answer = []

  prog_q = deque(progresses)
  speed_q = deque(speeds)

  while prog_q:
    for i in range(len(prog_q)):
      prog_q[i] += speed_q[i]

    count = 0
    while prog_q and progq[0]>=100:
      prog_q.popleft()
      speed_q.popleft()
      count += 1
    if count>0:
      answer.append(count)

  return answer
"""
