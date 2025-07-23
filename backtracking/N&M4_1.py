import sys
input = sys.stdin.readline

def solve(k,n,m,arr,st):
    if k==m:
        for i in range(m): print(arr[i]+1, end=" ")
        print()
        return
    
    for i in range(st,n):
        arr[k] = i
        solve(k+1,n,m,arr,i)

def main():
    n,m = map(int, input().split())
    arr = [0]*m
    solve(0,n,m,arr,0)

if __name__ == "__main__":
    main()
