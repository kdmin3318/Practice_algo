import sys
input = sys.stdin.readline

def solve(k,n,m,arr,used,result):
    if k==m:
        for i in range(m):
            print(result[i], end=" ")
        print()
        return
    
    for i in range(n):
        if not used[i]:
            used[i] = 1
            result[k] = arr[i]
            solve(k+1,n,m,arr,used,result)
            used[i] = 0

def main():
    n,m = map(int,input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    used = [0]*n
    result = [0]*m
    solve(0,n,m,arr,used,result)

if __name__ == "__main__":
    main()
