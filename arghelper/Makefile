all: arghelper arghelper.o

arghelper: arghelper.c
	gcc -O -DMAIN -g $< -o $@

arghelper.o: arghelper.c
	gcc -fPIC -c -O -g $< -o $@
