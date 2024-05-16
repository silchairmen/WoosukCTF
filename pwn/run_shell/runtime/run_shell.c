//gcc -m32 -fno-stack-protector -no-pie -o run_shell run_shell.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_string() {
    char buffer[256];
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);

    printf("stdout = %p\n", stdout);
    printf("Enter a string: \n");
    gets(buffer);
    printf(buffer);

    printf("\nEnter a string: \n");
    gets(buffer);
    printf(buffer);
}

int main() {
    print_string();
    return 0;
}