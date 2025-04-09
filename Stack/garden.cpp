#include<bits/stdc++.h>
using namespace std;

int n;
stack<int> s;
long long ans;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    long long h;
    cin>>n;
    while(n--){
        cin>>h;
        while(!s.empty()&&s.top()<=h) s.pop();
        ans += s.size();
        s.push(h);
    }
    cout<<ans;
    return 0;
}
