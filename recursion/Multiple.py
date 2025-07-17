import sys
from collections import deque
input = sys.stdin.readline

def multiply(a, b, c):
    if b == 1:
        return a % c
    half = multiply(a, b//2, c)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

def main():
    a, b, c = map(int, input().split())
    print(multiply(a,b,c))

if __name__ == "__main__":
    main()
