#include<bits/stdc++.h>
using namespace std;

// const int MX = 1000000;
// int dat[MX], pre[MX], nxt[MX];
// int unused = 1;

// void traverse() {
//     int cur = nxt[0];
//     while(cur != -1) {
//         cout << (char)dat[cur];
//         cur = nxt[cur];
//     }
//     cout << "\n";
// }

// void P_x(int addr, char c) {
//     dat[unused] = c;
//     pre[unused] = addr;
//     nxt[unused] = nxt[addr];
//     if(nxt[addr] != -1) pre[nxt[addr]] = unused;
//     nxt[addr] = unused;
//     unused++;
// }

// int B(int addr) {
//     if(pre[addr]==-1) return addr;
//     nxt[pre[addr]] = nxt[addr];
//     if(nxt[addr] != -1) pre[nxt[addr]] = pre[addr];
//     return pre[addr];
// }

// int L(int cur) {
//     if(pre[cur]==-1) return cur;
//     return pre[cur];
// }

// int D(int cur) {
//     if(nxt[cur]==-1) return cur;
//     return nxt[cur];
// }

// int main(void) {
//     ios::sync_with_stdio(0);
//     cin.tie(0);

//     int n;
//     cin>>n;
//     for(int i=0;i<n;i++) {
//         fill(pre,pre+MX,-1);
//         fill(nxt,nxt+MX,-1);
//         int cur=0;
//         string s;
//         cin>>s;
//         for(int i=0;i<(int)s.size();i++) {
//             if(s[i]=='<') cur = L(cur);
//             else if(s[i]=='>') cur = D(cur);
//             else if(s[i]=='-') cur = B(cur);
//             else {
//                 P_x(cur, s[i]);
//                 cur = unused - 1;
//             }
//         }
//         traverse();
//     }
// }

//STL list.ver
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;

    cin >> n;

    for(int i=0;i<n;i++) {
        list<char> L = {};
        string s;
        auto p = L.begin();

        cin>>s;
        for(auto c:s) {
            if(c=='<') {
                if(p!=L.begin()) p--;
            }
            else if(c=='>') {
                if(p!=L.end()) p++;
            }
            else if(c=='-') {
                if(p!=L.begin()) {
                    p--;
                    p = L.erase(p);
                }
            }
            else{
                L.insert(p, c);
            }
        }
        for(auto c: L) cout << c;
        cout << '\n';
    }
}
