MX = 1000005
dat = [0] * MX
pre = [-1] * MX
nxt = [-1] * MX
unused = 1

def traverse():
    cur = nxt[0]
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
    if nxt[addr] != -1:
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    unused += 1

def B(addr):
    if pre[addr] == -1:
        return addr
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]
    return pre[addr]

def L(cur):
    if pre[cur] == -1:
        return cur
    return pre[cur]

def D(cur):
    if nxt[cur] == -1:
        return cur
    return nxt[cur]

def main():
    global unused
    cur = 0

    s = input().strip()
    for char in s:
        P_x(cur, char)
        cur = unused - 1

    n = int(input())

    for _ in range(n):
        command = input().strip().split()
        o = command[0]

        if o=='L':
            cur = L(cur)
        elif o=='D':
            cur = D(cur)
        elif o=='B':
            cur = B(cur)
        elif o=='P':
            a = command[1]
            P_x(cur, a)
            cur = unused -1
        else:
            print("error")
            continue
    
    traverse()

if __name__ == "__main__":
    main()
