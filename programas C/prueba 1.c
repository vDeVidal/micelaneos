#include<stdio.h>
#include<stdlib.h>

typedef struct arbol {
    char elem;
    struct arbol *izq;
    struct arbol *der;


}arb;

void crearArbol(arb **raiz){
    *raiz = NULL;
}

void visit(char elem){
    printf("%c -", elem);
}
void pre(arb *a){
    if(a!=NULL){
        visit(a->elem);
        pre(a->izq);
        pre(a->der);

    }
}
void ino(arb *a){
    if(a!=NULL){
    
        ino(a->izq);
        visit(a->elem);
        ino(a->der);

    }
}
void post(arb *a){
    if(a!=NULL){
        
        post(a->izq);
        post(a->der);
        visit(a->elem);

    }
}









int main(){
    arb *raiz, *a, *b, *c, *d, *e, *f;
    a=(arb *)malloc(sizeof(arb));
    b=(arb *)malloc(sizeof(arb));
    c=(arb *)malloc(sizeof(arb));
    d=(arb *)malloc(sizeof(arb));
    e=(arb *)malloc(sizeof(arb));
    f=(arb *)malloc(sizeof(arb));

    a->elem ='a';
    a->izq=b;
    a->der=c;

    b->elem='b' ;
    b->izq=NULL;
    b->der=d;

    d->elem='d';
    d->izq=NULL;
    d->der=NULL;

    c->elem='c';
    c->izq=e;
    c->der=f;

    e->elem='e';
    e->izq=NULL;
    e->der=NULL;

    f->elem='f';
    f->izq=NULL;
    f->der=NULL;

    raiz=a;
    printf("\n preorden ");
    pre(raiz);
    printf("\n Inorden ");
    ino(raiz);
    printf("\n Postorden ");
    post(raiz);
    printf("\n FINALIZADO \n");
    return 0;
}