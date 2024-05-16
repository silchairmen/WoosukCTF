#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_string() {
    char buffer[256];
    printf("printf = %p\n", printf);
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