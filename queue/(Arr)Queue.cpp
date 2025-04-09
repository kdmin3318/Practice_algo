#include<bits/stdc++.h>
using namespace std;

const int MX = 1000005;
int dat[MX];
int head=0, tail = 0;

int size() {
    return tail-head;
}

int empty() {
    if(head==tail) return 1;
    else return 0;
}

void push(int x) {
    dat[tail++] = x;
}

int pop() {
    if(!empty()) return dat[head++];
    return -1;
}

int front() {
    if(!empty()) return dat[head];
    return -1;
}

int back() {
    if(!empty()) return dat[tail-1];
    return -1;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    while(n--) {
        string s;
        cin>>s;
        if(s=="push") {
            int x;
            cin>>x;
            push(x);
        } 
        else if(s=="pop") cout<<pop()<<"\n";
        else if(s=="size") cout<<size()<<"\n";
        else if(s=="empty") cout<<empty()<<"\n";
        else if(s=="front") cout<<front()<<"\n";
        else if(s=="back") cout<<back()<<"\n";
        else cout<<"error\n";
    }
}
