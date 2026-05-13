def solution(phone_book):
  phone_book.sort() #비슷한 접두어끼리 인접하게 만듦
  for i in range(len(phone_book)-1):
    if phone_book[i+1].startswith(phone_book[i]): return False
  return True
"""
문자열 정렬 법칙을 활용(O(nlogn)
"119" 와 접두어가 같은 "1195524421"이 바로 뒤로 정렬이 됨!
1. 해시를 활용하여 문제풀기! (O(n*L))
def solution(phone_book):
  hash_map = {p:True for p in phone_book} #딕셔너리가 아니라 set(phone_book)도 가능
  for phone_number in phone_book:
    prefix = ""
    for digit in phone_number[:-1]: #자기 자신은 제외
      prefix += digit
      if prefix in hash_map:
        return False
  return True
"""
