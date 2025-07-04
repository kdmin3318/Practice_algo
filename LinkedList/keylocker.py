import sys

MX = 1000005
dat = [0] * MX
pre = [-1] * MX
nxt = [-1] * MX
unused = 1

def traverse():
    cur = nxt[0]  # nxt[0]에서 시작해야 함
    result = []
    while cur != -1:
        result.append(chr(dat[cur]))
        cur = nxt[cur]
    print(''.join(result))

def P_x(addr, c):
    global unused
    dat[unused] = ord(c)
    pre[unused] = addr
    nxt[unused] = nxt[addr]
    if nxt[addr] != -1:  # nxt[unused]가 아니라 nxt[addr]
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    unused += 1

def L(cur):
    if pre[cur] == -1:
        return cur
    return pre[cur]

def R(cur):
    if nxt[cur] == -1:
        return cur
    return nxt[cur]

def B(addr):
    if pre[addr] == -1:
        return addr
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]
    return pre[addr]

def main():
    input = sys.stdin.readline
    global unused
    
    n = int(input())
    
    for _ in range(n):
        unused = 1  # 각 테스트케이스마다 초기화
        # 배열들도 초기화
        for i in range(MX):
            dat[i] = 0
            pre[i] = -1
            nxt[i] = -1
        
        cur = 0  # 헤드 노드에서 시작
        s = input().rstrip()
        
        for char in s:
            if char == '<':
                cur = L(cur)
            elif char == '>':
                cur = R(cur)
            elif char == '-':
                cur = B(cur)
            else:
                P_x(cur, char)
                cur = unused - 1  # 새로 추가된 노드로 커서 이동
        
        traverse()

if __name__ == "__main__":
    main()
