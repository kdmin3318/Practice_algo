def solution(participant, completion):
  temp = {}
  for p in participant:
    temp[p] = temp.get(p,0) + 1
  for c in completion:
    temp[c] -= 1
  for key,value in temp.items():
    if value>0:
      return key
"""
1. collections의 Counter이용
from collections import Counter
def solution(participant, completion):
  result = Counter(participant)  Counter(completion)
  return list(result.keys())[0]

2. zip을 이용하기
def solution(participant, completion):
  participant.sort()
  completion.sort()

  for p,c in zip(participant, completion):
    if p!=c:
      return p

  return participant[-1]
