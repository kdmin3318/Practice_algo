n = [i+1 for i in range(20)]
for i in range(10):
    a,b = map(int, input().split())
    n[a-1:b] = reversed(n[a-1:b])
for i in range(20):
    print(n[i], end=" ")
