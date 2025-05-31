n = int(input())
a = list(map(int, input().split()))
x = int(input())
count = 0
t = set() #list보다 탐색이 빠름, 중복 저장x
for i in range(n):
    if x-a[i] in t:
        count +=1
    t.add(a[i])
print(count)
