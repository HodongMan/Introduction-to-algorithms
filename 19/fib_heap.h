#ifndef _FIB_HEAP_H__
#define _FIB_HEAP_H__


#define MAX_HEAP_ROOT_COUNT 10


typedef enum{
    
    TRUE = 1,
    FALSE = 0,
}Boolean;


typedef struct _node{

    unsigned int degree;
    Boolean mark;
    int value;

    struct _node* parent;
    struct _node* child;

}Node;


typedef struct{

    unsigned int count;
    Node* min;
    Node** root;

}Heap;


Node* makeNode(int value);
Heap* makeFibHeap();

void FibHeapInsert(Heap* heap, Node* x);
Node* FindMeanHeap(Heap* heap);
Heap* UnionFibHeap(Heap* heap1, Heap* heap2);


#endif
