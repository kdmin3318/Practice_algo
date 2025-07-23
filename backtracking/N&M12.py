import sys
input = sys.stdin.readline

class NandM:
    def __init__(self,n,m,num):
        self.n = n
        self.m = m
        self.num = sorted(num)
        self.arr = [0]*m

    def solve(self, k, st):
        if k==self.m:
            for i in range(self.m): print(self.arr[i], end=" ")
            print()
            return
        
        temp = 0
        for i in range(st, self.n):
            if temp != self.num[i]:
                self.arr[k] = self.num[i]
                temp = self.arr[k]
                self.solve(k+1, i)

def main():
    n,m = map(int, input().split())
    num = list(map(int, input().split()))
    NM = NandM(n,m,num)
    NM.solve(0,0)
    
if __name__ == "__main__":
    main()
