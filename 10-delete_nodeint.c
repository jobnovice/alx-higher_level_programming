#include <list2.h>
/***
 * delete_nodeint_at_index - deletes a node 
 * @head: pointer to pointer of the first element of the linked list
 * @index: is the index of the node to be deleted
 * Return: the result of deleting the node
*/

int delete_nodeint_at_index(listint_t **head, unsigned int index)
{
    listint_t *temp, *curr;
    temp = *head;
    int i = 0;
    if (*head == NULL){return -1;}
    while (temp && i < index)
    {
        i++;
        temp = temp -> next;
    }
    if (temp){
        curr = temp;
        temp = temp -> next;
        free(curr);
        return 1;
    }
    return -1;

    



}