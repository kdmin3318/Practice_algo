import sys
input = sys.stdin.readline

def solve(k, n, m, arr, num):
    if k==m:
        for i in range(m):
            print(num[arr[i]], end=" ")
        print()
        return
    
    st = arr[k-1]+1 if k!=0 else 0
    for i in range(st,n):
        arr[k] = i
        solve(k+1,n,m,arr,num)

def main():
    n,m = map(int, input().split())
    num = list(map(int, input().split()))
    num = sorted(num)
    arr = [0]*10
    solve(0,n,m,arr,num)

if __name__ == "__main__":
    main()
