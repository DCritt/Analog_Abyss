#include "linked_list.h"

Linked_List *init_linked_list() {
    Linked_List *list = malloc(sizeof(Linked_List));
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;

    return list;
}

void push_back(Linked_List *list, void *data) {
    if (list == NULL) { return; }
    list->size++;

    Node *new_node = malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = NULL;

    if (list->tail == NULL) {
        new_node->prev = NULL;
        list->head = new_node;
        list->tail = new_node;
    } else {
        new_node->prev = list->tail;
        list->tail->next = new_node;
        list->tail = new_node;
    }
}

void *get_index(Linked_List *list, int index) {
    if (list == NULL || index < 0 || index >= list->size) { return NULL; }

    Node *curr = list->head;
    for (int i = 0; i < index; i++) { curr = curr->next; }

    return curr->data;
}

void *set_index(Linked_List *list, int index, void *data) {
    if (list == NULL || index < 0 || index >= list->size) { return NULL; }

    Node *curr = list->head;
    for (int i = 0; i < index; i++) { curr = curr->next; }

    void *old = curr->data;
    curr->data = data;

    return old;
}

void *remove_index(Linked_List *list, int index) {
    if (list == NULL || index < 0 || index >= list->size) { return NULL; }

    Node *curr = list->head;
    for (int i = 0; i < index; i++) { curr = curr->next; }

    void *data;

    if (curr->prev == NULL) { data = remove_first(list); }
    else if (index == (list->size - 1)) { data = remove_last(list); }
    else {
        list->size--;
        curr->prev->next = curr->next;
        curr->next->prev = curr->prev;
        data = curr->data;
        free(curr);
    }
    return data;
}

void *remove_first(Linked_List *list) {
    if (list == NULL || list->head == NULL) { return NULL; }
    list->size--;

    Node *node = list->head;
    void *data = node->data;

    if (node == list->tail) { 
        list->head = NULL;
        list->tail = NULL;
    } else {
        list->head = node->next;
    }
    
    free(node);

    return data;
}

void *remove_last(Linked_List *list) {
    if (list == NULL || list->head == NULL) { return NULL; }
    list->size--;

    Node *node = list->tail;
    void *data = node->data;

    if (node == list->head) {
        list->head = NULL;
        list->tail = NULL;
    } else {
        list->tail = node->prev;
    }

    free(node);

    return data;
}