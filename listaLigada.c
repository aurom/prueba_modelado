#include <stdio.h>
#include <stdlib.h>
#include "list.h"

int main(void){
	struct node_struct* l = NULL; //lista
	int i;
	/*llenamos la lista*/
	for(i = 0; i < 10; i++){
		struct node_struct* nuevo;
		nuevo = newNode(i);
		nuevo->next = l;
		l = nuevo;
	}
	struct node_struct* l_inversa = inversa(l);
	printf("Tamaño de la lista recursivamente: %d\n",len_rec(l));
	printf("Tamaño de la lista iterativamente: %d\n",len_iter(l));
	printf("Numero maximo de la lista: %d\n",max(l));
	printf("Inversa de la lista: \n");
	print_list(l_inversa);
	printf("La lista: \n");
	print_list(l);
	/*liberacion de memoria.*/
	struct node_struct* next;
	/*borramos l*/
	while(l){
		next = l->next;
		free(l);
		l = next;
	}
	/*borramos l_inversa*/
	while(l_inversa){
		next = l_inversa->next;
		free(l_inversa);
		l_inversa = next;
	}
	return 0;
}