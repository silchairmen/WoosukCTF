//gcc -m32 -fno-stack-protector -no-pie -o got got.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_string() {
    char buffer[256];
    printf("stdout = %p\n", stdout);
    printf("Enter a string: \n");
    gets(buffer);
    printf(buffer);

    printf("/bin/sh");
}

int main() {
    print_string();
    return 0;
}