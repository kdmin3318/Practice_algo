#include<bits/stdc++.h>
using namespace std;

int n;
stack<pair<int, int>> s;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int MX = 100000001;

    cin>>n;
    s.push({MX,0});

    for(int i=1;i<=n;i++) {
        int height;
        cin>>height;
        while(s.top().first<height) s.pop();
        cout<<s.top().second<<" ";
        s.push({height,i});
    }
}
