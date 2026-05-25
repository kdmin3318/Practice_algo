from itertools import product

def solution(users, emoticons):
  discount = [40,30,20,10]
  join,revenue = 0,0
  for dis in product(discount, repeat=len(emticons)):
    j,r = 0,0
    for rate, budget in users:
      spend = 0
      for i,price in enumerate(emoticons):
        if dis[i]>=rate:
          spend += price * (100-dis[i])//100
      if spend>=budget: j += 1
      else: r += spend
    if (j,r) > (join,revenue):
      join = j
      revenue = r

  return [join, revenue]
"""
itertools 라이브러리 중복 순열 product사용 + BF풀이 방법...
"""
