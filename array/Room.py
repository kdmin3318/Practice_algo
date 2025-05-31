n, k = map(int, input().split())
r = [[0]*6 for i in range(2)]
for i in range(n):
    s, y = map(int, input().split())
    r[s][y-1] += 1
count = 0
for i in range(2):
    for j in range(6):
        count += (r[i][j]+k-1)//k
print(count)
