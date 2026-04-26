def solution(number, limit, power):
  def count(num):
    temp = 0
    for i in range(1,int(num**0.5)+1):
      if num%i==0:
        if i*i==num: temp+=1
        else: temp+=2
      if temp>limit:
        return power
    return temp
  answer = sum(count(n+1) for n in range(number))
  return answer
"""
약수의 개수 구하는 함수 구현!
1. 전체 방식을 다 구해야한다면 에라토스테네스의 체 방법도 활용 가능(NlogN)
def solution(number, limit, power):
  counts = [0] * (number+1)

  for i in range(1, number+1):
    for j in range(i, number+1, i):
      counts[j] += 1

  answer = 0
  for i in range(1, number+1):
    if counts[i]>limit:
      answer += power
    else:
      answer += counts[i]

  return answer
"""
