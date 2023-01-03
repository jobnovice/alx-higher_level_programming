#include "list2.h"
/**
 * print_listint_safe - a fucniton that prints 
 * 
 * @head: 
 * @return: size_t 
 */


size_t print_listint_safe(const listint_t *head){
    size_t i =0;
    listint_t *temp = head;
    if (!head){return   98;}
    while(temp){
        printf("[%s] %d",temp ->next,temp ->n);
        i++;
        temp = temp -> next;
    }
    return i;
}