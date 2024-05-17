#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
void timeout_handler(int signum) {
    printf("Time out!\n");
    exit(1);
}
int main() {
    int value;
    signal(SIGALRM, timeout_handler);
    alarm(30);
    scanf("%d",&value);
    if (value < 0){
        value-=1004;
        if (value > 0) {
            system("/bin/sh");
        } else {
            printf("Value: %d\n", value);
        }
    }
    return 0;
}