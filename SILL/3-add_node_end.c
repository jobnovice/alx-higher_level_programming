#include <lists.h>
list_t *add_node_end(list_t **head, const char *str){
    list_t *new, *last;
    if (str == NULL){
        return NULL;
    }
    new = malloc(sizeof(list_t));
    int i = 0;
    while(str){
        i++;
    }
    new -> str = strdup(str);
    new -> len = i;
    last = *head; 
    while(last){
        last = last -> next;
    }
    last -> next = new;

}
/* the answer for the Question that asks to write a
function that get's called rigght before main*/
static void print_s(void){
    printf("You're beat! and yet, you must allow,\nI bore my house upon my back!\n");
}