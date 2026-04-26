def solution(s):
  answer = ''
  s = s.lower()
  for st in s.split(" "):
    temp = ""
    for i, c in enumerate(st):
      if i%2==0:
        c = c.upper()
      temp += c
    answer += temp + " "
  return answer[:-1]
"""
대문자<->소문자 변환 함수 활용
주의!
- 문자열은 +는 사용할수 있지만, - 기호를 사용할 수 없음!
- split()는 기본적으로 공백의 개수를 상관없이 분리하기 때문에 한칸 분리라면 split(" ")를 명시해야함
1. join함수 활용
def solution(s):
  res = []
  for word in s.split(" "):
    new_word = ""
    for i, char in enumerate(word):
      if i%2==0:
        new_word += char.upper()
      else:
        new_word += char.lower()
    res.append(new_word)

  return " ".join(res)
"""
