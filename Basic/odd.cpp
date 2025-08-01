#include<bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    vector<int> a;
    for(int i=0;i<7;i++) {
        int temp;
        cin>>temp;
        if(temp%2==1) a.push_back(temp);
    }
    if(a.empty()){
        cout<<-1;
        return 0;
    }
    int min = a[0];
    int sum = a[0];
    for(int i=1;i<int(a.size());i++){
        if(a[i]<min) min = a[i];
        sum += a[i];
    }
    cout<<sum<<"\n"<<min;
}
