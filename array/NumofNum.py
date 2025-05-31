n = [int(input()) for i in range(3)]
a = [0 for i in range(10)]
sum = n[0] * n[1] * n[2]
while sum>0:
    a[sum%10] +=1
    sum //= 10
for i in range(10):
    print(a[i])
