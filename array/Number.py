n = int(input())
a = list(map(int, input().split()))
v = int(input())
count = 0
for i in range(len(a)):
    if a[i]==v:
        count += 1
print(count)
