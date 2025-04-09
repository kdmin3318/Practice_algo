#include<bits/stdc++.h>
using namespace std;

typedef struct Stack {
    int top;
    int capacity;
    int *array;
} Stack;

Stack *create_stack(int capacity) {
    Stack *stack = (Stack*)malloc(sizeof(Stack));

    if(!stack) return NULL;

    stack->top = -1;
    stack->capacity = capacity;
    stack->array = (int*)malloc(stack->capacity*sizeof(int));

    if(!stack) return NULL;

    return stack;
}

int isFull(Stack *stack) {
    return stack->top == stack->capacity-1;
}

int isEmpty(Stack *stack) {
    return stack->top == -1;
}

int pop(Stack *stack) {
    if(!isEmpty(stack)) return stack->array[stack->top--];
    return -1;
}

void push(Stack *stack, int new_element) {
    if(!isFull(stack)) stack->array[++stack->top] = new_element;
}

int peek(Stack *stack) {
    if(!isEmpty(stack)) return stack->array[stack->top];
    return 0;
}

int sum_stack(Stack *stack) {
    int sum=0;
    for(int i=0;i<(stack->top+1);i++) sum+=stack->array[i];
    return sum;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    Stack *my_stack;
    int n, a;
    
    cin>>n;
    my_stack = create_stack(n);
    while(n--) {
        cin>>a;
        if(a==0) pop(my_stack);
        else push(my_stack, a);
    }
    cout<<sum_stack(my_stack);
}
