#include<bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    int count=0;
    cin>>n;
    while(n--) {
        string s;
        cin>>s;

        stack<char> a;
        for(auto p:s) {
            if(a.empty()) a.push(p);
            else {
                if((a.top()=='A'&&p=='A')||(a.top()=='B'&&p=='B')){
                    a.pop();
                }
                else a.push(p);
            }
        }
        if(a.empty()) count++;
    }
    cout<<count;
}
