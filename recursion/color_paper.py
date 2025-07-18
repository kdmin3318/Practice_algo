import sys
input = sys.stdin.readline

result = [0]*2

def check(paper,x,y,n):
    for i in range(x,x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def color_paper(paper,x,y,z):
    if check(paper,x,y,z):
        result[paper[x][y]] += 1
        return
    
    n = z//2
    for i in range(2):
        for j in range(2):
            color_paper(paper, x+i*n, y+j*n, n)

def main():
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    color_paper(paper, 0,0,n)
    
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
