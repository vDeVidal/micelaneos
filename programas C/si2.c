#include<stdio.h>
#include<stdlib.h>

struct lista{
int dato;
struct lista *sig;
};


struct lista *L;
struct lista *p;
int i;
L = NULL; /* Crea una lista vacía */
for(i = 4; i >= 1; i--)
{
 /* Reserva memoria para un nodo */
    p = (struct lista *) malloc(sizeof(struct lista));
    p->dato = i;
    p->sig = L;
    L = p;
}