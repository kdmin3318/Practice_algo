//LinkedList(array.ver)
#include<bits/stdc++.h>
using namespace std;

const int MX = 1000005;
int dat[MX], pre[MX], nxt[MX];
int unused = 1;

void traverse() {
    int cur = nxt[0];
    while(cur != -1) {
        cout << (char)dat[cur];
        cur = nxt[cur];
    }
    cout << "\n";
}

void P_x(int addr, char c) {
    dat[unused] = c;
    pre[unused] = addr;
    nxt[unused] = nxt[addr];
    if(nxt[addr] != -1) pre[nxt[addr]] = unused;
    nxt[addr] = unused;
    unused++;
}

int B(int addr) {
    if(pre[addr]==-1) return addr;
    nxt[pre[addr]] = nxt[addr];
    if(nxt[addr] != -1) pre[nxt[addr]] = pre[addr];
    return pre[addr];
}

int L(int cur) {
    if(pre[cur]==-1) return cur;
    return pre[cur];
}

int D(int cur) {
    if(nxt[cur]==-1) return cur;
    return nxt[cur];
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    fill(pre,pre+MX,-1);
    fill(nxt,nxt+MX,-1);

    int cur=0, n;
    char o, a;
    string s;
    cin>>s;
    for(int i=0;i<(int)s.size();i++) {
        P_x(cur, s[i]);
        cur = unused - 1;
    }

    cin>>n;
    for(int j=0;j<n;j++) {
        cin>>o;
        if(o=='L') cur = L(cur);
        else if(o=='D') cur = D(cur);
        else if(o=='B') cur = B(cur);
        else if(o=='P') {
            cin>>a;
            P_x(cur, a);
            cur = unused -1;
        }
        else {
            cout<<"error\n";
            continue;
        }
    }
    traverse();
}
