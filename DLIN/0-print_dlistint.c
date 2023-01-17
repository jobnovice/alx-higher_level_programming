#include <lists.h>
/**
 *print_dlistint - a function that printts
 *  @h: the head of the dLinked list
 * Returns: the number nodes in the list 
 * 
 */

size_t print_dlistint(const dlistint_t *h){

    size_t nbr = 0;
    dlistint_t *temp = h;
    if (h = NULL){return 0;}
    while(temp){
        printf("%d",temp -> n);
        nbr++;
        temp = temp -> next;
    } 
    return nbr;
}