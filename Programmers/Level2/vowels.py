def solution(word):
  answer = 0
  vowels = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
  weights = [781, 156, 31, 6, 1]
  for i,c in enumerate(word):
    answer += weights[i]*vowels[c]+1
  return answer
"""
수학적 구현
각 자리수의 가중치를 781, 156, 31, 6, 1 로 두어서 풀기
"""
