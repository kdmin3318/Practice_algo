def solution(numbers):
  numbers = list(map(str, numbers))
  numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
  answer = ''.join(numbers)
  return str(int(answer))
"""
문자열 대소 비교 이해, sorted key활용을 통한 문제 풀이
중요!!! 문자열의 대소비교는 길이에 상관없이 앞에서 비교하다가 높은 부분이 나오면 거기서 바로 끝남
즉, "999" 와 "991991991"을 비교하면 "9"와 "1" 부분에서 비교가 끝나서 "999"가 큰 문자열로 나옴

참고!
x*3을 한 이유 numbers원소가 1000이하 이기 때문에 한자리 수와 3자리수를 비교하기 위해서는 최소 *3을 해주어야함!
"""
