#include<bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    vector<int>a;
    int sum=0;
    for(int i=0;i<5;i++) {
        int temp;
        cin>>temp;
        sum+=temp;
        a.push_back(temp);
    }
    sort(a.begin(), a.end());
    cout<<sum/5<<"\n"<<a[2];
}
