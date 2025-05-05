#include<bits/stdc++.h>
using namespace std;

const int MX=1000005;
int dat[MX*2+1];
int head = MX, tail = MX;
bool isReversed = false;

int isEmpty() {
    return head == tail;
}

void R() {
    isReversed = !isReversed;
}

void D() {
    if(!isEmpty()) {
        if(isReversed) tail--;
        else head++;
    }
}

void push_front(int x) {
    dat[--head] = x;
}

void push_back(int x) {
    dat[tail++] = x;
}

int pop_front() {
    if(!isEmpty()) return dat[head++];
    return -1;
}

int pop_back() {
    if(!isEmpty()) return dat[--tail];
    return -1;
}

bool P(string& temp, int n) {
    vector<int> arr;
    int num=0;
    bool hasNumber = false;
    // Skip the '[' at the beginning
    for(int i=1; i<(int)temp.size()-1; i++) {
        if(isdigit(temp[i])) {
            num = num*10 + (temp[i]-'0');
            hasNumber = true;
        } else if(hasNumber) {
            arr.push_back(num);
            num = 0;
            hasNumber = false;
        }
    }
    
    if(hasNumber) arr.push_back(num);
    
    if(n == (int)arr.size()) {
        for(int i=0; i<(int)arr.size(); i++) 
            push_back(arr[i]);
        return true;
    } else {
        cout << "error\n";
        return false;
    }
}

void print() {
    cout << "[";
    if(!isEmpty()) {
        if(!isReversed) {
            cout << pop_front();
            while(!isEmpty()) {
                cout << "," << pop_front();
            }
        }
        else {
            cout << pop_back();
            while(!isEmpty()) {
                cout << "," << pop_back();
            }
        }
    }
    cout << "]";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    while(n--) {
        string s;
        cin>>s;
        int num;
        string a;
        cin>>num;
        cin>>a;
        head=MX;
        tail=MX;
        isReversed = false;
        bool success = P(a, num);
        if(!success) {
            continue;  
        }
        bool hasError = false;
        for(auto a:s) {
            if(a=='R') R();
            else if(a=='D') {
                if(isEmpty()) {
                    hasError = true;
                    break;
                }
                D();
            }
        }
        if(hasError) {
            cout<<"error\n";
        } else {
            print();
            cout<<"\n";
        }
    }
}
