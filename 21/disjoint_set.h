
#ifndef _DISJOINT_SET_H__
#define _DISJOINT_SET_H__

typedef struct _item{

    unsigned int value;
    struct _item* prev;
    struct _item* next;

}Item;

typedef struct _set{

    Item* Head;
    Item* Tail;

}DisjointSet;


Item* MakeItem(unsigned int value);
DisjointSet* MakeSet(Item* item);
DisjointSet* Union(DisjointSet* set1, DisjointSet* set2);
Item* FindSet(unsigned int value);


#endif
