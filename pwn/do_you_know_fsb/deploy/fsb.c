//gcc -fno-stack-protector -no-pie -o fsb fsb.c
//aslr disabled

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

char auth;

void timeout_handler(int sig) {
    puts("Time's up!");
    exit(0);
}

int main() {
    char name[128];
    setbuf(stdout, NULL);

    signal(SIGALRM, timeout_handler);
    alarm(30);

    puts("Do you know FSB??");
    ssize_t read_bytes = read(STDIN_FILENO, name, sizeof(name));
    if (read_bytes == -1) {
        perror("read");
        exit(1);
    }

    printf(name);
    puts("");

    if (auth < 0) {
        system("/bin/sh");
    }

    return 0;
}