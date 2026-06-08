def solution(n, words):
  dictionary = set()
  for i,word in enumerate(words):
    if i!=0:
      if temp!=word[0] or word in dictionary:
        return [i%n+1,i//n+1]
    temp = word[-1]
    dictionary.add(word)
  return [0,0]
"""
해시(Hash, set())활용한 문제풀이
"""
