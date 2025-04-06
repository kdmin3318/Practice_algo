#include<bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
     
    list<int> L = {};
    int n,k;
    cin>>n>>k;
    for(int i=0;i<n;i++) {
        L.push_back(i+1);
    }
    auto p = L.begin();
    cout<<"<";
    while(!L.empty()) {
        for(int j=0;j<k-1;j++) { //k번째를 없애기 위해 현 위치에서 k-1번 움직여야됨
            p++;
            if(p==L.end()) p = L.begin();
        }
        cout<<*p;
        p = L.erase(p);
        if(p==L.end()) p = L.begin(); //삭제 후 반복자가 end()라면
        if(!L.empty()) cout<<", "; // 마지막 쉼표 방지
    }
    cout<<">";
}
