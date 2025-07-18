import sys
input = sys.stdin.readline

result = [0] * 3

def check(paper, x, y, n):
    for i in range(x,x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:
                return False
        
    return True

def p(paper,x,y,z):
    if check(paper,x,y,z):
        result[paper[x][y]+1] += 1
        return
    
    n = z//3
    for i in range(3):
        for j in range(3):
            p(paper,x+i*n,y+j*n,n)


def main():
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    p(paper, 0,0,n)

    for i in range(3):
        print(result[i])

if __name__ == "__main__":
    main()
