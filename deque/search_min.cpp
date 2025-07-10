#include<bits/stdc++.h>
using namespace std;

vector<int> a;
deque<int> d;
int n;

void D(int i, int l) {
    if(!d.empty() && d.front()<i-l+1) d.pop_front();
    while(!d.empty() && a[d.back()]>a[i]) d.pop_back();
    d.push_back(i);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int l;
    cin>>n>>l;

    a.resize(n);

    for(int i=0;i<n;i++) cin>>a[i];
    for(int i=0;i<n;i++) {
        D(i, l);
        if(d.empty()) cout<<"Error\n";
        else cout<<a[d.front()]<<" ";
    }
}
