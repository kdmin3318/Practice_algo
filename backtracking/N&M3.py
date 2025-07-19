import sys
input = sys.stdin.readline

def solve(k,n,m,arr):
    if k==m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    for i in range(1,n+1):
        arr[k] = i
        solve(k+1,n,m,arr)

def main():
    n,m = map(int, input().split())
    arr = [0]*m
    solve(0,n,m,arr)

if __name__ == "__main__":
    main()
