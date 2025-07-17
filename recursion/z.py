import sys
input = sys.stdin.readline

def z(n,r,c):
    if n==0:
        return 0
    half = 2**(n-1)
    if r<half and c<half:
        return z(n-1,r,c)
    if r<half and c>=half:
        return half*half + z(n-1,r,c-half)
    if r>= half and c<half:
        return 2*half*half + z(n-1,r-half,c)
    if r>=half and c>=half:
        return 3*half*half + z(n-1,r-half,c-half)

def main():
    n,r,c = map(int, input().split())
    print(z(n,r,c))

if __name__ == "__main__":
    main()
