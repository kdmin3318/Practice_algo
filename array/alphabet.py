n = [0 for i in range(26)]
s = input()
for i in range(len(s)):
    n[ord(s[i])-ord('a')] += 1 #ord가 유니코드변환
for i in range(26):
    print(n[i], end=" ")
