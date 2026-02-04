# Makefile.c - builds c_program from c_program.c

# Default target when we run: make -B -f Makefile.c
all: c_program

# Rule: build the executable c_program from c_program.c
c_program: c_program.c
	gcc -Wall -Wextra -o c_program c_program.c

# Optional: remove the compiled binary
clean:
	rm -f c_program

