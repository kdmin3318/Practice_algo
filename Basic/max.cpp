#include<bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a[9], b[9];
    for(int i=0;i<9;i++) {
        cin>>a[i];
        b[i] = a[i];
    }
    sort(b,b+9);
    cout<<b[8]<<"\n";
    for(int i=0;i<9;i++) {
        if(b[8] == a[i]) cout<<i+1;
    }
}
