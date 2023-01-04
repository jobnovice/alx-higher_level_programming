#include <stdlib.h>
#include <lists.h>

size_t print_list(const list_t *h){

    size_t nbr_node = 0;
    list_t *trv;


    if (h == NULL){
        return 1;
    }
    trv = h;
    while(trv){
        nbr_node += 1;
        printf("[%d]  %c",trv -> len, trv -> str);
        trv = trv -> next;
    }
    return nbr_node;
}
size_t list_len(const list_t *h){
    size_t nbt = 0;
    while (h){
        nbt++;
        h = h -> next;
    }
    return nbt;
}

list_t *add_node(list_t **head, const char *str){
    list_t *new;
    size_t nbr = 0;
    
    if (str == NULL){
        return NULL;
    }
    new = malloc(sizeof(list_t));
    if (new == NULL){
        return NULL;
    }
    while (str){
        nbr++;
    }

    new -> len = nbr;
    new -> next = *head;
    *head = new;
    
    
    return new;
}