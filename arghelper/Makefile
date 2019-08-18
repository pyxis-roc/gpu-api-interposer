all: arghelper arghelper.o

arghelper: arghelper.c
	gcc -O -DMAIN -g $< -o $@

arghelper.o: arghelper.c
	gcc -c -O -g $< -o $@
