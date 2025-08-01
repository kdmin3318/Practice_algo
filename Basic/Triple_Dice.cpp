#include<bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int a,b,c;
    int m;
    cin>>a>>b>>c;
    if(a==b&&b==c) cout<<10000+a*1000;
    else if(a==b) cout<<1000+a*100;
    else if(a==c) cout<<1000+a*100;
    else if(b==c) cout<<1000+b*100;
    else {
        m = max(a,b);
        m = max(m,c);
        cout<<m*100;
    }
}
