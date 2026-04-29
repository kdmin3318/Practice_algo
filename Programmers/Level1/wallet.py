def solution(wallet, bill):
  answer = 0
  while min(wallet)<min(bill) or max(wallet)<max(bill):
    if bill[0]<bill[1]:
      bill[1] //= 2
    else:
      bill[0] //= 2
    answer += 1
  return answer
"""
문제 내용 그대로 코드로 옮기는 시뮬레이션 문제
주의! min,max함수를 while마다 돌리는 코드는 효율적이지 않지만 길이가 2로 고정이기 때문에 크게 신경쓰지 않아도됨
참고! min,max는 O(n)임..
"""
