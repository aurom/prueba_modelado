HEADERS = list.h

default: testList

list.o: list.c $(HEADERS)
	gcc -c list.c -o list.o
listaligada.o : listaLigada.c $(HEADERS)
	gcc -c listaLigada.c -o listaLigada.o 
testList: listaLigada.o list.o
	gcc listaLigada.o list.o -o testList