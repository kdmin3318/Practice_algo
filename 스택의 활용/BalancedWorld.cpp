#include<bits/stdc++.h>
using namespace std;

int isBalanced(string s) {
    stack<char> a;
    for(auto p:s) {
        if(p=='('|| p=='[') a.push(p);
        if(p==')'||p==']') {
            if(a.empty()) return 0;
            if((p==')' && a.top() !='(')||(p==']'&&a.top() != '[')) return 0;
            a.pop();
        }
    }
    if(a.empty()) return 1;
    else return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string x;
    while(true) {
        getline(cin,x);
        if(x==".") break;
        if(isBalanced(x)) cout<<"yes\n";
        else cout<<"no\n";
    }
}
