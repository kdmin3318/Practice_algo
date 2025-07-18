import sys
input = sys.stdin.readline

def check(paper, x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def quad_tree(paper, x, y, z):
    if check(paper, x, y, z):
        print(paper[x][y], end="")
        return
    
    n = z//2
    print("(", end="")
    for i in range(2):
        for j in range(2):
            quad_tree(paper, x+i*n, y+j*n, n)
    print(")", end="")

def main():
    n = int(input())
    paper = [list(map(int, input().strip())) for _ in range(n)]
    quad_tree(paper, 0, 0, n)
    print()  # 개행 추가

if __name__ == "__main__":
    main()
