#include<bits/stdc++.h>
using namespace std;

int count=0;

void hanoi(int a, int b, int n) {
    if(n==1) {
        cout<<a<<" "<<b<<"\n";
        
        return;
    }
    hanoi(a, 6-a-b, n-1);
    cout<<a<<" "<<b<<"\n";
    hanoi(6-a-b, b, n-1);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    cout<<(1<<n)-1<<"\n";
    hanoi(1,3,n);
}
