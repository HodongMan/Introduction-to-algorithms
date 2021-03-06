#include<stdlib.h>

#include"fib_heap.h"


Node* makeNode(int value){

    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->value = value;

    new_node->degree = 0;
    new_node->parent = NULL;
    new_node->child = NULL;
    new_node->mark = FALSE;

    return new_node;
}

Heap* makeFibHeap(){

    Heap* new_heap = (Heap*)malloc(sizeof(Heap));
    
    new_heap->root = (Node**)malloc(sizeof(Node*) * MAX_HEAP_ROOT_COUNT);
    new_heap->root[0] = NULL;
    new_heap->count = 0;
    new_heap->min = NULL;

    return new_heap;
}

void FibHeapInsert(Heap* heap, Node* x){

    Node* temp;
    x->degree = 0;
    x->parent = NULL;
    x->child = NULL;
    x->mark = FALSE;

    if(heap->count == 0){
	heap->root[0] = x;
	heap->min = x;
    }else{
	heap->root[heap->count] = x;
	if(x->value < heap->min->value){
	    temp = heap->min;
	    heap->min->value = x->value;
	    free(temp);
	}
    }
    heap->count += 1;
}

Node* FindMeanHeap(Heap* heap){

    return heap->min;
}

Heap* UnionFibHeap(Heap* heap1, Heap* heap2){

    Heap* new_heap = makeFibHeap();
    new_heap->min = heap1->min;

    addHeapList(new_heap, heap1, heap2);
    
    if((heap1->min == NULL) || ((heap2->min != NULL) && (heap2->min->value < heap1->min->value))){
	new_heap->min = heap2->min;
    }

    free(heap1);
    free(heap2);

    return new_heap;
}

static inline void addHeapList(Heap* new_heap, Heap* heap1, Heap* heap2){

    int i;
    int temp_index = 0;

    for(i = 0; i < heap1->count; i++){
	
	new_heap->root[temp_index] = heap1->root[i];
	temp_index += 1;
    }

    for(i = 0; i < heap2->count; i++){
	new_heap->root[temp_index] = heap2->root[i];
	temp_index += 1;
    }

    new_heap->count = temp_index;
}
