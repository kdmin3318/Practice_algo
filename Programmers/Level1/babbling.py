def solution(babblings):
  answer = 0
  dic = {"aya":1, "ye":2, "woo":3, "ma":4}
  for b in babblings:
    for key, value in dic.items():
      b = b.replace(key, str(value))
    last = ""
    possible = True
    for i in b:
      if b.isalpha():
        possible = False
        break
      if last and last==i:
        possible = False
        break
      last = i
    answer += 1 if possible else 0
  return answer
"""
시뮬레이션 문제, replace활용
1. split추가 활용
def solution(babblings):
  words = ["aya", "ye", "woo", "ma"]
  answer = 0
  for word in babblings:
    temp = word
    for w in words:
      temp = temp.replace(w, w+" ")
    tokens = temp.split()
    if all(t in words for t in tokens) and all(tokens[i] != tokens[i+1] for i in range(len(tokens)-1)):
      answer += 1
  return answer
"""
