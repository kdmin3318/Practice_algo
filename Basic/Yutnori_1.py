from collections import Counter
import sys
input = sys.stdin.readline

result = ["D", "C", "B", "A", "E"]

for _ in range(3):
    a = list(map(int, input().split()))
    n = Counter(a)
    print(result[n[0]])
