def solution(n):
  answer = ''
  num_map = ["1","2","4"]
  while n>0:
    n-=1
    answer = num_map[n%3]+answer
    n//=3
  return answer
"""
0이 없는 진법(zero-less Number System)문제로 
원래 0,1,2로 되어 있는 숫자를 1,2,4 1부터 시작으로 바꾸었기 때문에
0부터 시작으로 맞춰주기 위해서 각 단계마다 -1를 진행해주는 것!
"""
