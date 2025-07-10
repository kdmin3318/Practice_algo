#include<bits/stdc++.h>
using namespace std;

int isBracket(string s) {
    stack<char> a;
    for(auto p:s) {
        if(p=='(') a.push(p);
        if(p==')') {
            if(a.empty()) return 0;
            if(a.top()!='(') return 0;
            a.pop();
        }
    }
    if(a.empty()) return 1;
    else return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    while(n--) {
        string s;
        cin>>s;
        if(isBracket(s)) cout<<"YES\n";
        else cout<<"NO\n";
    }
}
