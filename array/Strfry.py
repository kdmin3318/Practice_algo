#strfry함수는 입력된 문자열을 무작위로 재배열 하여 새로운 문자열 만듦
n = int(input())
for i in range(n):
    a = [0] * 26
    c, d = map(str, input().split())
    for i in range(len(c)):
        a[ord(c[i])-ord('a')] += 1
    for i in range(len(d)):
        a[ord(d[i])-ord('a')] -= 1
    if all(x==0 for x in a):
        print("Possible")
    else:
        print("Impossible")
    
