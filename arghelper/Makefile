all: arghelper arghelper.o

arghelper: arghelper.c
	gcc -std=c99 -O -DMAIN -g $< -o $@

arghelper.o: arghelper.c
	gcc -std=c99 -fPIC -c -O -g $< -o $@
