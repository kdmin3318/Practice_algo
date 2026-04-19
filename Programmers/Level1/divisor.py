def get_div(n):
  temp = []
  for i in range(1,n+1):
    if n%i==0: temp.apend(i)
  return temp

def solution(n):
  return sum(get_div(n))
"""
sum 기본 함수 활용 및 % 기본 연산 활용
1. 한줄 풀이
def solution(n):
  return sum(i for i in range(1,n+1) if n%i==0)
2. O(루트n)으로 줄이는 풀이(ex. 16의 약수는 1,2,4까지 찾고 16//1, 16//2, 16//4를 추가로 더하면 됨!)
def solution(n):
  answer = 0
  for i in range(1, int(n**0.5)+1):
    if n%i==0:
      answer += i
      if i**2 != n: answer += n//i #n 자체 수 말고 n//i 도 약수기 때문에 더해줘야함!
  return answer
"""
