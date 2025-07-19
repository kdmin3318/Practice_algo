import sys
input = sys.stdin.readline

cnt = 0

def solve(k,n,s,result,arr):
    global cnt
    if k==n:
        if result==s: cnt += 1
        return
    
    solve(k+1,n,s,result,arr)
    solve(k+1,n,s,result+arr[k],arr)


def main():
    global cnt
    n,s = map(int, input().split())
    arr = list(map(int, input().split()))
    solve(0,n,s,0,arr)
    if s==0: cnt -= 1
    print(cnt)

if __name__ == "__main__":
    main()
