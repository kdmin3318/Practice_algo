import sys
input = sys.stdin.readline

isused1 = [0]*40  # column(열)을 차지하고 있는지
isused2 = [0]*40  # / 방향 대각선을 차지하고 있는지
isused3 = [0]*40  # \ 방향 대각선을 차지하고 있는지
count = 0

def nq(cur, n):
    global count
    
    if cur == n:
        count += 1
        return
        
    for i in range(n):  # cur행, i열에 퀸을 놓을 예정
        if isused1[i] or isused2[i+cur] or isused3[n-1+cur-i]:
            continue
        isused1[i] = 1
        isused2[cur+i] = 1
        isused3[n-1+cur-i] = 1
        nq(cur+1, n)
        isused1[i] = 0
        isused2[cur+i] = 0
        isused3[n-1+cur-i] = 0

def main():
    n = int(input())
    nq(0, n)
    print(count)

if __name__ == "__main__":
    main()
