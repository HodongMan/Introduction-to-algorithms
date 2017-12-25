
#include<stdio.h>
#include<stdlib.h>

#include"disjoint_set.h"


Item* MakeItem(unsigned int value){

    Item* newItem;
    
    if((newItem = (Item*)malloc(sizeof(Item))) == NULL){
	fprintf(stderr, "ALLOCATION ERROR\n");
	return NULL;
    }

    
    newItem->value = value;
    newItem->prev = NULL;
    newItem->next = NULL;

    return newItem;
}

DisjointSet* MakeSet(Item* item){

    DisjointSet* newSet;
    
    if((newSet = (DisjointSet*)malloc(sizeof(DisjointSet*))) == NULL){
	fprintf(stderr, "ALLOCATION ERROR\n");
	return NULL;
    }

    newSet->Head = item;
    newSet->Tail = item;

    return newSet;
}
