#include<bits/stdc++.h>
using namespace std;

int n;
stack<int> s;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>n;
    int arr[n];
    int result[n];
    for(int i=n-1;i>=0;i--) {
        cin>>arr[i];
    }
    for(int i=0;i<n;i++) {
        while(!s.empty()&&s.top()<=arr[i]) s.pop();
        if(!s.empty()) result[n-i-1] = s.top();
        else result[n-i-1] = -1;
        s.push(arr[i]);
    }
    for(int i=0;i<n;i++) {
        cout<<result[i]<<" ";
    }
}
