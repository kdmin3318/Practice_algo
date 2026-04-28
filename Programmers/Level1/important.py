def soulution(message, spoiler_ranges):
  words = []
  start = 0

  #단어 위치 기록
  for i, c in enumerate(message):
    if c==" ":
      words.append((message[start:i],start,i-1))
      start = i+1
  words.append((message[start:],start,len(message)-1))
  print(words) #[('here', 0, 3), ('is', 5, 6), ('muzi', 8, 11), ('here', 13, 16), ('is', 18, 19), ('a', 21, 21), ('secret', 23, 28), ('message', 30, 36)]

  #일반 단어 추출!
  normal_words = set()
  for word, s, e in words:
    spoiler = False
    for a, b in spoiler_ranges:
      if not(e<a or s>b): #끝보다 스포일러가 뒷부분이거나, 시작보다 스포일러가 작을 경우는 일반 단어에 해당함!
        spoiler = True
        break
    if not spoiler:
      normal_words.add(word)
  print(normal_words) # {'here', 'message', 'is', 'muzi', 'a'}

  #스포 구간 순서대로 확인
  important = set()
  count = 0
  for a, b in spoiler_ranges:
    for word, s, e in words:
      if not(e<a or s>b):
        if word not in normal_words and word not in important:
          important.add(word)
          count += 1
  return count
"""
구간 시뮬레이션 + 해시(set) 활용하여 문제 풀이
"""
