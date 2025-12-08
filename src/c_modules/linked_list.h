#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <stdlib.h>

typedef struct Node {
    void *data;
    int dynamic;
    struct Node *next;
    struct Node *prev;
} Node;

typedef struct Linked_List {
    Node *head;
    Node *tail;
    size_t size;
} Linked_List;

Linked_List *init_linked_list();
void push_back(Linked_List *list, void *data);
void *get_index(Linked_List *list, int index);
void *set_index(Linked_List *list, int index, void *data);
void *remove_index(Linked_List *list, int index);
void *remove_first(Linked_List *list);
void *remove_last(Linked_List *list);

#endif