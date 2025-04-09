#include<bits/stdc++.h>
using namespace std;

typedef struct Queue{
    int front, rear;
    int capacity;
    int *array;
} Queue;

Queue *createQueue(int capacity) {
    Queue *queue = (Queue*)malloc(sizeof(Queue));

    if(!queue) return NULL;

    queue->front = 0;
    queue->rear = -1;
    queue->capacity = capacity;
    queue->array = (int*)malloc(queue->capacity*sizeof(int));

    if(!queue) return NULL;
    return queue;
}

int isFull(Queue *queue) {
    if(queue->front == queue->capacity-1) return 1;
    else return 0;
}

int isEmpty(Queue *queue) {
    if(queue->front-1 == queue->rear) return 1;
    else return 0;
}

void enqueue(Queue *queue, int new_element) {
    if(!isFull(queue)) queue->array[++queue->rear] = new_element;
}

int dequeue(Queue *queue) {
    if(!isEmpty(queue)) return queue->array[queue->front++];
    return -1;
}

int front(Queue *queue) {
    if(!isEmpty(queue)) return queue->array[queue->front];
    else return -1;
}

int rear(Queue *queue) {
    if(!isEmpty(queue)) return queue->array[queue->rear];
    else return -1;
}

int size(Queue *queue) {
    return queue->rear - queue->front + 1;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    Queue *my_queue = createQueue(n);
    while(n--) {
        string s;
        cin>>s;
        if(s=="push") {
            int x;
            cin>>x;
            enqueue(my_queue,x);
        } 
        else if(s=="pop") cout<<dequeue(my_queue)<<"\n";
        else if(s=="size") cout<<size(my_queue)<<"\n";
        else if(s=="empty") cout<<isEmpty(my_queue)<<"\n";
        else if(s=="front") cout<<front(my_queue)<<"\n";
        else if(s=="back") cout<<rear(my_queue)<<"\n";
        else cout<<"error\n";
    }
}
