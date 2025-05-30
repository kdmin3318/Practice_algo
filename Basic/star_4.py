n = int(input())
for i in range(1,n+1):
    for j in range(i-1):
        print(" ", end="")
    for j in range(n+1-i):
        print("*", end="")
    print()
