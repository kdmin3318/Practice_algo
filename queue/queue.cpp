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
    return queue->front == queue->capacity-1;
}

int isEmpty(Queue *queue) {
    return queue->front-1==queue->rear;
}

void enqueue(Queue *queue, int new_element) {
    if(!isFull) queue->array[++queue->rear] = new_element;
}

int dequeue(Queue *queue) {
    if(!isEmpty) return queue->array[queue->front++];
    return 0;
}

int front(Queue *queue) {
    if(!isEmpty) return queue->array[queue->front];
}

int rear(Queue *queue) {
    if(!isEmpty) return queue->array[queue->rear];
}

int main(void) {

}
