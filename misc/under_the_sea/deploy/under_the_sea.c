#include <stdio.h>
#include <stdlib.h>

int main() {
    int value;
    
    scanf("%d",&value);
    if (value < 0)
        value-=1004;
    if (value > 0) {
        system("/bin/sh");
    } else {
        printf("Value: %d\n", value);
    }

    return 0;
}