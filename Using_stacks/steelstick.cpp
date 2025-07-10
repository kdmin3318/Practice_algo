#include<bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> a;
    string s;
    cin>>s;
    int sum=0;

    for(int i=0; i<(int)s.size();i++) {
        if(s[i]=='(') a.push(i);
        else {
            if(i-a.top()==1) {
                a.pop();
                sum+=(int)a.size();
            }\
            else {
                a.pop();
                sum++;
            }
        }
    }
    cout<<sum;
}
