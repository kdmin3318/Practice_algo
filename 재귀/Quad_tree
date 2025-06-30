#include<bits/stdc++.h>
using namespace std;

int tree[2200][2200];

bool check(int a, int b, int c) {
    for(int i=a;i<a+c;i++) {
        for(int j=b;j<b+c;j++) {
            if(tree[a][b]!=tree[i][j]) return false;
        }
    }
    cout<<tree[a][b];
    return true;
}

void QT(int x, int y, int z) {
    if(check(x,y,z)) return;
    int new_size = z/2;
    cout<<"(";
    for(int i=0;i<2;i++) {
        for(int j=0;j<2;j++) {
            QT(x+i*new_size,y+j*new_size,new_size);
        }
    }
    cout<<")";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin>>n;
    for(int i=0;i<n;i++) {
        string str;
        cin>>str;
        for(int j=0;j<n;j++) {
            tree[i][j] = str[j]-'0';
        }
    }
    QT(0,0,n);
}
