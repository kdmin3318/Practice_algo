import sys
input = sys.stdin.readline

class NandM:
    def __init__(self,n,m,num):
        self.n = n
        self.m = m
        self.num = sorted(num)
        self.arr = [0]*10
        self.result = [0]*m

    def solve(self, k):
        if k==self.m:
            for i in range(self.m):
                print(self.result[i], end=" ")
            print()
            return
        
        st = self.arr[k-1] + 1 if k!=0 else 0
        temp = 0
        for i in range(st,self.n):
            if temp != self.num[i]:
                self.result[k] = self.num[i]
                temp = self.result[k]
                self.arr[k] = i
                self.solve(k+1)

def main():
    n,m = map(int, input().split())
    num = list(map(int, input().split()))
    NM = NandM(n,m,num)
    NM.solve(0)

if __name__ == "__main__":
    main()
