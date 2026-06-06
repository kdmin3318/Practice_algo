def solution(numbers):
  answer = []
  for n in numbers:
    if n%2==0: answer.append(n+1)
    else:
      binary = '0'+bin(n)[2:]
      idx = binary.rfind('01')
      temp = binary[:idx] + '10' + binary[idx+2:]
      answer.append(int(temp,2))
  return answer
"""
그리디 문제 풀이
짝수일 경우 0으로 끝나기 때문에 0을 1로 바꾸는것이 가장 간단하게 바꾸는 방법임
홀수일 경우 01로 된 수가 바뀌는것이 가장 간단하게 바뀌는 방법이기 때문에 뒤에서 부터 01로 된 부분을 탐색후 바꿈
참고!
오른쪽 탐색은 rfind와 rindex가 있음, 둘의 차이는 없을 경우 -1반환과 ValueError를 내는 것 밖에 없음
1. 비트 연산자로 풀이
def solution(numbers):
  answer = []
  for n in numbers:
    if n%2==0: answer.append(n+1)
    else:
      last_zero = ~n&(n+1) #가장 오른쪽에 있는 0찾기..
      answer.append((n|last_zero)&~(last_zero>>1))
  return answer
"""
