def decimal(num, k):
  temp = ""
  base = "0123456789ABCDEF"
  if num==0: return "0"
  while num>0:
    temp = base[num%k] + temp
    num //= k
  return temp

def solution(n, t, m, p):
  answer = ''
  temp = ""
  num = 0 

  limit = t*m
  while len(temp)<limit:
    temp += decimal(num, n)
    num += 1

  for i in range(p-1, limit, m):
    answer += temp[i]
  return answer
"""
시뮬레이션 문제 풀이(문제를 코드로 옮겨서 풀이)
참고! 11진수 이상의 진수를 변환할 때는 base="0123456789ABCDEF"를 이용하는 것이 편함!
"""
