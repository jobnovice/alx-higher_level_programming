#include <list2.h>
size_t print_listint(const listint_t *h){
    size_t nbr = 0;
    while(h){
        printf("[%d]", h -> n);
        nbr++;
        h = h-> next;
    }
    return nbr;
}
/*1-listint_len.c*/
size_t listint_len(const listint_t *h){
    size_t nbr_elem = 0;
    while(h){
        nbr_elem++;
        h = h-> next;
    }
    return nbr_elem;
}
/*2-add_nodeint.c*/
listint_t *add_nodeint(listint_t **head, const int n){
   listint_t *new;
   if (n == NULL){
    return NULL;
   }
   new = malloc(sizeof(listint_t));
   new -> n = n;
   new -> next = *head;
   *head = new;
   return new;
}
/*3-add_nodeint_end.c*/
listint_t *add_nodeint_end(listint_t **head, const int n){
   	listint_t *new_nodeint, *last_nodeint;

	new_nodeint = malloc(sizeof(listint_t));
	if (new_nodeint == NULL)
		return (NULL);

	new_nodeint->n = n;
	new_nodeint->next = NULL;

	/* if head is a null pointer, assign new node to it*/
	if (*head == NULL)
		*head = new_nodeint;

	else
	{
		last_nodeint = *head;

		while (last_nodeint->next != NULL)
			last_nodeint = last_nodeint->next;

		last_nodeint->next = new_nodeint;
	}

	return (new_nodeint);
}
/*4-free_listint.c*/
void free_listint(listint_t *head){
    while(head){
        free(head -> n);
        free(head);
        head = head -> next;
    }

}
/*5-free_listint2.c*/
void free_listint2(listint_t **head){
    listint_t *temp;

}
/*6-pop_listint.c*/
int pop_listint(listint_t **head){
    listint_t *temp;
    temp = *head;
    if (*head != NULL){
        *head = temp -> next;
        remove (temp);
        return (temp -> n);
    }
    return 0;
}
/*7-get_nodeint.c*/
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index){
   unsigned int i = 0;
   listint_t *temp = head;

    while (temp && i < index)
    {
        temp = temp->next;
        i++;
    }
    return (temp ? temp : NULL);
}
/*8-sum_listint.c*/
int sum_listint(listint_t *head){

    int sum = 0;
    if (head == NULL){return 0;}
    while(head){
        sum += head -> n;
        head = head -> next;
    }    
    return sum;
}
/*9-insert_nodeint.c*/
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n){
    listint_t *temp = *head;
    listint_t *new;

    

    int i = 0;
    if (*head == NULL && idx ){
        new = malloc(sizeof(listint_t));
        new -> n = n;
        new -> next = *head;
        *head = new;
    }


}