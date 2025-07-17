import sys
input = sys.stdin.readline

def hanoi(a,b,n):
    if n==1:
        print(f"{a} {b}")
        return
    hanoi(a,6-a-b,n-1)
    print(f"{a} {b}")
    hanoi(6-a-b,b,n-1)


def main():
    n = int(input())
    print(2**n-1)
    hanoi(1,3,n)

if __name__ =="__main__":
    main()
