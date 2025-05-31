a = str(input())
b = str(input())
n = [0] * 26
for i in range(len(a)):
    n[ord(a[i])-ord('a')] += 1
for i in range(len(b)):
    n[ord(b[i])-ord('a')] -= 1
sum=0
for i in n:
    sum += abs(i)
print(sum)
