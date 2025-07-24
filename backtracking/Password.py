import sys
input = sys.stdin.readline

class Password:
    def __init__(self, l, c, arr):
        self.m = l
        self.n = c
        self.arr = sorted(arr)
        self.result = [0] * l
        self.con = 0
        self.vo = 0
    
    def isvowel(self, i):
        return self.arr[i] in 'aeiou'
    
    def solve(self, k, st):
        if k == self.m:
            if self.vo >= 1 and self.con >= 2:
                print(''.join(self.result))
            return
        
        for i in range(st, self.n):
            self.result[k] = self.arr[i]
            if self.isvowel(i): 
                self.vo += 1
            else: 
                self.con += 1
            self.solve(k+1, i+1)
            if self.isvowel(i): 
                self.vo -= 1
            else: 
                self.con -= 1

def main():
    l, c = map(int, input().split())
    arr = input().split()
    PW = Password(l, c, arr)
    PW.solve(0, 0)

if __name__ == "__main__":
    main()
