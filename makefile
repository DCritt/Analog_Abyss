##makefile for analog abyss
CC = gcc
CFLAGS = -Wall -O2 -fPIC -c
CFLAGS_DL = -shared -o

OBJS := $(wildcard C_Files/*.o)

all: compile run

run:
	python analog_abyss.py

compile: compile_linux compile_windows

compile_linux: compile_graphics compile_raycasting compile_lighting compile_map compile_textures
	$(CC) $(CFLAGS_DL) Object_Linker_Files/mygraphics.so Object_Linker_Files/*.o

compile_windows: compile_graphics compile_raycasting compile_lighting compile_map compile_textures
	$(CC) $(CFLAGS_DL) Object_Linker_Files/mygraphics.dll Object_Linker_Files/*.o
	
compile_graphics:
	$(CC) $(CFLAGS) C_Files/graphics.c -o Object_Linker_Files/graphics.o

compile_raycasting:
	$(CC) $(CFLAGS) C_Files/raycasting.c -o Object_Linker_Files/raycasting.o

compile_lighting:
	$(CC) $(CFLAGS) C_Files/lighting.c -o Object_Linker_Files/lighting.o

compile_map:
	$(CC) $(CFLAGS) C_Files/map.c -o Object_Linker_Files/map.o

compile_textures:
	$(CC) $(CFLAGS) C_Files/textures.c -o Object_Linker_Files/textures.o

compile_linked_list:
	$(CC) $(CFLAGS) C_Files/linked_list.c -o Object_Linker_Files/linked_list.o

clean:
ifeq ($(OS),Windows_NT)
	del /Q Object_Linker_Files\*.o Object_Linker_Files\*.dll Object_Linker_Files\*.so
	cls
else
	rm -f Object_Linker_Files/*.o Object_Linker_Files/*.dll Object_Linker_Files/*.so
	clear
endif