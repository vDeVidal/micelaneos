#include <stdlib.h>
#include<stdio.h>

struct tarbol{
    char elem;
    struct tarbol *izq;
    struct tarbol *der;
};

typedef struct tarbol ARBOL;

// Declaracion
void crearArbol(ARBOL **raiz);
void visitar(char elem);
void preorden(ARBOL *a);
void inorden(ARBOL *a);
void postorden(ARBOL *a);
void arbolito(ARBOL **raiz);
int max(int a, int b);
int altura(ARBOL * a);
void contadorNodos(ARBOL *a, int *CONTADOR);
void contadorHojas(ARBOL *a, int *CONTADOR);
void contadorInternos(ARBOL *a, int *CONTADOR);

// Implementacion Arbol

void crearArbol(ARBOL **raiz){
    *raiz = NULL;
}

void visitar(char elem){
    printf("%c -", elem);
}

void preorden(ARBOL *a){
    if (a != NULL){ 
        visitar(a->elem);
        preorden(a->izq);
        preorden(a->der);
    }
}

void inorden(ARBOL *a){
    if (a != NULL){
        inorden(a->izq);
        visitar(a->elem);
        inorden(a->der);
    }
}

void postorden(ARBOL *a){
    if (a != NULL){
        postorden(a->izq);
        postorden(a->der);
        visitar(a->elem);
    }
}

void arbolito(ARBOL **raiz){
    ARBOL *h, *m, *z, *k, *c, *j, *a, *i;
    ARBOL *n, *p, *y, *b, *e, *d, *x, *l;
    h = (ARBOL *)malloc(sizeof(ARBOL));
    m = (ARBOL *)malloc(sizeof(ARBOL));
    z = (ARBOL *)malloc(sizeof(ARBOL));
    k = (ARBOL *)malloc(sizeof(ARBOL));
    c = (ARBOL *)malloc(sizeof(ARBOL));
    j = (ARBOL *)malloc(sizeof(ARBOL));
    a = (ARBOL *)malloc(sizeof(ARBOL));
    i = (ARBOL *)malloc(sizeof(ARBOL));
    n = (ARBOL *)malloc(sizeof(ARBOL));
    p = (ARBOL *)malloc(sizeof(ARBOL));
    y = (ARBOL *)malloc(sizeof(ARBOL));
    b = (ARBOL *)malloc(sizeof(ARBOL));
    e = (ARBOL *)malloc(sizeof(ARBOL));
    d = (ARBOL *)malloc(sizeof(ARBOL));
    x = (ARBOL *)malloc(sizeof(ARBOL));
    l = (ARBOL *)malloc(sizeof(ARBOL));
    h->elem = 'h';
    h->izq = m;
    h->der = z;
    m->elem = 'm';
    m->izq = k;
    m->der = NULL;
    z->elem = 'z';
    z->izq = c;
    z->der = j;
    k->elem = 'k';
    k->izq = a;
    k->der = i;
    c->elem = 'c';
    c->izq = NULL;
    c->der = NULL;
    j->elem = 'j';
    j->izq = n;
    j->der = p;
    a->elem = 'a';
    a->izq = NULL;
    a->der = NULL;
    i->elem = 'i';
    i->izq = NULL;
    i->der = y;
    n->elem = 'n';
    n->izq = NULL;
    n->der = NULL;
    p->elem = 'p';
    p->izq = b;
    p->der = e;
    y->elem = 'y';
    y->izq = NULL;
    y->der = NULL;
    b->elem = 'b';
    b->izq = NULL;
    b->der = NULL;
    e->elem = 'e';
    e->izq = d;
    e->der = x;
    d->elem = 'd';
    d->izq = NULL;
    d->der = l;
    x->elem = 'x';
    x->izq = NULL;
    x->der = NULL;
    l->elem = 'l';
    l->izq = NULL;
    l->der = NULL;
    *raiz = h; 
}

int altura(ARBOL * a){
    // caso base: el árbol vacío tiene una altura de 0
    if (a == NULL) {
        return 0;
    }
    // Visita el subárbol izquierdo y derecho y considera 
    // la profundidad máxima
    return 1 + max(altura(a->izq), altura(a->der));
}

int max(int a, int b){
    if (a > b){
        return a;
    }
    else{
        return b;
    }
}

void contadorNodos(ARBOL *a, int *CONTADOR){
	if (a != NULL){		
		*CONTADOR = *CONTADOR + 1;
		contadorNodos(a->izq, CONTADOR);
		contadorNodos(a->der, CONTADOR);
	}
}

void contadorHojas(ARBOL *a, int *CONTADOR){
	if (a != NULL){		
        if ((a->izq == NULL) && (a->der == NULL)){
            *CONTADOR = *CONTADOR + 1;
        }
		contadorHojas(a->izq, CONTADOR);
		contadorHojas(a->der, CONTADOR);
	}
}

void contadorInternos(ARBOL *a, int *CONTADOR){
	if (a != NULL){		
        if (!((a->izq == NULL) && (a->der == NULL))){
            *CONTADOR = *CONTADOR + 1;
        }
		contadorInternos(a->izq, CONTADOR);
		contadorInternos(a->der, CONTADOR);
	}
}