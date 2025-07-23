import sys
input = sys.stdin.readline

def solve(k,n,m,arr,num):
    if k==m:
        for i in range(m): print(arr[i], end=" ")
        print()
        return
    
    for i in range(n):
        arr[k] = num[i]
        solve(k+1,n,m,arr,num)

def main():
    n,m = map(int, input().split())
    num = set(map(int, input().split()))
    num = sorted(num)
    n = len(num)
    arr = [0]*m
    solve(0,n,m,arr,num)

if __name__ == "__main__":
    main()
