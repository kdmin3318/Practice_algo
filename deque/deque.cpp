#include<bits/stdc++.h>
using namespace std;

const int MX = 1000005;
int dat[2*MX+1];
int head = MX, tail = MX;

void push_front(int x) {
    dat[--head] = x;
}

void push_back(int x) {
    dat[tail++] = x;
}

int empty() {
    if(head == tail) return 1;
    return 0;
}

int size() {
    return tail-head;
}

int pop_front() {
    if(!empty()) return dat[head++];
    else return -1;
}

int pop_back() {
    if(!empty()) return dat[--tail];
    else return -1;
}

int front() {
    if(!empty()) return dat[head];
    else return -1;
}

int back() {
    if(!empty()) return dat[tail-1];
    else return -1;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    while(n--) {
        string s;
        cin>>s;
        if(s=="push_front") {
            int x;
            cin>>x;
            push_front(x);
        }
        else if(s=="push_back") {
            int x;
            cin>>x;
            push_back(x);
        }
        else if(s=="pop_front") cout<<pop_front()<<"\n";
        else if(s=="pop_back") cout<<pop_back()<<"\n";
        else if(s=="size") cout<<size()<<"\n";
        else if(s=="empty") cout<<empty()<<"\n";
        else if(s=="front") cout<<front()<<"\n";
        else if(s=="back") cout<<back()<<"\n";
        else cout<<"error\n";
    }
}
