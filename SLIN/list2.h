#ifndef LISTS2_H
#define LISTS2_H
#include <stdlib.h>

#include <stdio.h>
#include <string.h>

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;


#endif