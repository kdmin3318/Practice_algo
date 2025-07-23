import sys
input = sys.stdin.readline

def solve(k,n,m,num,used,arr):
    if k==m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return
    
    temp = 0
    for i in range(n):
        if not used[i] and temp != num[i]:
            used[i] = 1
            arr[k] = num[i]
            temp = arr[k]
            solve(k+1,n,m,num,used,arr)
            used[i] = 0

def main():
    n,m = map(int, input().split())
    num = list(map(int, input().split()))
    num = sorted(num)
    used = [0]*10
    arr = [0]*m
    solve(0,n,m,num,used,arr)

if __name__ == "__main__":
    main()
