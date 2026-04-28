def solution(s, skip, index):
  answer = ''
  temp = []
  for c in skip:
    temp.append(ord(c)-ord('a'))
  for c in s:
    n = index
    i = ord(c) - ord('a')
    while n!=0:
      i = (i+1)%26
      if i in skip:
        continue
      else:
        n -= 1
    answer += chr(i+ord('a'))
  return answer
"""
O(s*index*len(skip))으로 모든 경우를 조회하는 BF방식 풀이
주의!, 문제의 제한조건에 s에 skip의 문자가 나오지 않는 다는 조건하에 더 효율적으로 작성 가능!
1. 딕셔너리를 이용한 풀이법( 시간복잡도 max(O(26),O(s) )
def solution(s, skip, index):
  alpha = "abcdefghijklmnopqrstuvxyz"
  for c in skip:
    alpha = alpha.replace(c,"")

  char_to_idx = {c:i for i,c in enumerate(alpha)}

  n = len(alpha)
  answer = []

  for c in s:
    i = (char_to_idx[c]+index)%n
    answer.append(alpha[i])

  return "".join(answer)
"""
