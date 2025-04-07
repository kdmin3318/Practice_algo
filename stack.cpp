#include<bits/stdc++.h>
using namespace std;

typedef struct {
    int top;
    int capacity;
    int* array;
}Stack;

Stack *createStack(int capacity) {
    Stack *stack = (Stack*)malloc(sizeof(Stack));

    if(!stack) return NULL;

    stack->top = -1;
    stack->capacity = capacity;
    stack->array = (int*)malloc(stack->capacity*sizeof(int));

    if(!stack->array) return NULL;

    return stack;
}

int isFull(Stack *stack) {
    return stack->top == stack->capacity-1;
}

int isEmpty(Stack *stack) {
    return stack->top == -1;
}

int peek(Stack *stack) {
    if(isEmpty(stack)) return -1;
    return stack->array[stack->top];
}

int pop(Stack *stack) {
    if(!isEmpty(stack)) return stack->array[stack->top--];
    return -1;
}

void push(Stack *stack, int new_element) {
    if(!isFull(stack)) stack->array[++stack->top] = new_element;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    Stack *my_stack;
    int n,a;
    cin>>n;
    my_stack = createStack(n);
    while(n--) {
        string s;
        cin>>s;;
        if(s=="push") {
            cin>>a;
            push(my_stack,a);
        } 
        else if(s=="pop") cout<<pop(my_stack)<<"\n";
        else if(s=="top") cout<<peek(my_stack)<<"\n";
        else if(s=="empty") cout<<isEmpty(my_stack)<<"\n";
        else if(s=="size") cout<<my_stack->top+1<<"\n";
    }
}
