import sys
input = sys.stdin.readline

def star(s,x, y, z):
    if z==1:
        s[x][y] = "*"
        return

    n = z//3
    for i in range(3):
        for j in range(3):
            if i==1 and j==1: continue
            star(s, x+i*n, y+j*n, n)


def main():
    n = int(input())
    s = [[" "]*n for _ in range(n)]
    star(s,0,0,n)
    for row in s:
        print(''.join(map(str,row)))

if __name__ == "__main__":
    main()
