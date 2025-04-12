#include<bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    deque<int> D;

    int n, m, count=0;
    cin>>n>>m;
    for(int i=1;i<=n;i++) D.push_back(i);
    while(m--) {
        int o, i=0;
        cin>>o;
        while(D[i]!=o) i++;
        if((int)D.size()-i>i) {
            for(int j=0;j<i;j++) {
                D.push_back(D.front());
                D.pop_front();
                count++;
            }
        } else {
            for(int j=0;j<(int)D.size()-i;j++) {
                D.push_front(D.back());
                D.pop_back();
                count++;
            }
        }
        D.pop_front();
    }
    cout<<count;
}
