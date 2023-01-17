#include <lists.h>

size_t dlistint_len(const dlistint_t *h){
    size_t nbr = 0;
    if (h == NULL){
        return nbr;
    }
    while(h -> prev){
        h  = h -> prev;
    }
    while (h){
        nbr++;
        h = h -> next;
    }
    return nbr;

}