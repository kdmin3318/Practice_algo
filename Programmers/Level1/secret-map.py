def bin(n):
    temp = []
    while n>0:
        temp.append(n%2)
        n //= 2
    return temp

def solution(n, arr1, arr2):
    map = [[0]*n for _ in range(n)]
    for i,a in enumerate(arr1):
        b = bin(a)
        for j in range(len(b)):
            map[i][j] = b[j]
    for i,a in enumerate(arr2):
        b = bin(a)
        for j in range(len(b)):
            if map[i][j]!=b[j] and map[i][j]==1: map[i][j]=1
            else: map[i][j] = b[j]
        map[i].reverse()
    answer = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if map[i][j]==1:
                temp += "#"
            else: temp += " "
        answer.append(temp)
    return answer
"""
bin이라는 이진 변환 함수를 작성해서 풀었음..
1. bin 기본 함수 활용하기(이진 변환 기본 함수가 존재함), zfill 기본 함수 활용(빈 부분을 0으로 채워주는 함수)
def solution(n,arr1,arr2):
  answer = []
  arr1 = [bin(i)[2:].zfill(n) for i in arr1] #bin함수는 0b가 앞에 무조건 붙게 되어있
  arr2 = [bin(i)[2:].zfill(n) for j in arr2]

  for i in range(n):
    temp = ''.join(" " if a=='0' and b=='0' else "#" for a,b in zip(arr1[i],arr2[i]))
    answer.append(temp)

  return answer
2. | 비트 연산자 이용하기
def solution(n, arr1, arr2):
  answer = []
  for a,b in zip(arr1, arr2):
    combined = a|b #9와 30이 들어가면 31을 출력함 이진 수 상으로 or연산 후 출력값

    binary_str = bin(combined)[:2].zfill(n)

    row = binary_str.replace("1","#").replace("0"," ")
    answer.append(row)
  return answer
"""
