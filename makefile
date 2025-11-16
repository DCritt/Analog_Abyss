##makefile for analog abyss
CC = gcc
CFLAGS = -Wall -O2 -fPIC -c
CFLAGS_DL = -shared -o

all: compile run

run:
	python analog_abyss.py

compile: compile_linux compile_windows

compile_linux: compile_graphics compile_raycasting compile_lighting compile_map compile_textures
	$(CC) $(CFLAGS_DL) libs/graphics_lib/mygraphics.so libs/graphics_lib/*.o

compile_windows: compile_graphics compile_raycasting compile_lighting compile_map compile_textures
	$(CC) $(CFLAGS_DL) libs/graphics_lib/mygraphics.dll libs/graphics_lib/*.o
	
compile_graphics:
	$(CC) $(CFLAGS) src/c_modules/graphics.c -o libs/graphics_lib/graphics.o

compile_raycasting:
	$(CC) $(CFLAGS) src/c_modules/raycasting.c -o libs/graphics_lib/raycasting.o

compile_lighting:
	$(CC) $(CFLAGS) src/c_modules/lighting.c -o libs/graphics_lib/lighting.o

compile_map:
	$(CC) $(CFLAGS) src/c_modules/map.c -o libs/graphics_lib/map.o

compile_textures:
	$(CC) $(CFLAGS) src/c_modules/textures.c -o libs/graphics_lib/textures.o

compile_linked_list:
	$(CC) $(CFLAGS) src/c_modules/linked_list.c -o libs/graphics_lib/linked_list.o

clean:
ifeq ($(OS),Windows_NT)
	del /Q libs\graphics_lib\*.o libs\graphics_lib\*.dll libs\graphics_lib\*.so
	cls
else
	rm -f libs/graphics_lib/*.o libs/graphics_lib/*.dll libs/graphics_lib/*.so
	clear
endif