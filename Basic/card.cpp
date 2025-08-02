#include<bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int card[20] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
    int a,b, temp;
    for(int i=0;i<10;i++) {
        cin>>a>>b;
            for(int i=0;i<(b-a+1)/2;i++) {
                temp = card[a+i-1];
                card[a+i-1] = card[b-i-1];
                card[b-i-1] = temp;
            }
    }
    for(int i=0;i<20;i++) cout << card[i] << " ";
}
