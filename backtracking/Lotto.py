import sys
input = sys.stdin.readline

def solve(a,k,num,arr,result):
    if a==6:
        for i in range(6): print(result[i], end=" ")
        print()
        return
    
    st = arr[a-1]+1 if a!=0 else 0
    for i in range(st,k):
        result[a] = num[i]
        arr[a] = i
        solve(a+1,k,num,arr,result)

def main():
    while(1):
        data = list(map(int, input().split()))
        k = data[0]
        if k==0: break
        num = data[1:]
        num = sorted(num)
        arr = [0]*6
        result = [0]*6
        solve(0,k,num,arr,result)
        print()

if __name__ == "__main__":
    main()
