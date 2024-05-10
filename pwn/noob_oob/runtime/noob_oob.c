#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <time.h>

void alarm_handler() {
    puts("TIME OUT");
    exit(-1);
}

void initialize(char buffer[], int size) {
    signal(SIGALRM, alarm_handler);
    alarm(30);
    for (int i = 0; i < size; i++) {
        buffer[i] = rand() % 100;
    }
}

int calculateSecretKey(int buffer[], int size) {
    int secret_key;
    do {
        secret_key = 0;
        int randomCount = rand() % 16;
        for (int i = 0; i < randomCount; i++) {
            int randomIndex = rand() % size;
            secret_key += buffer[randomIndex];
        }
    } while (secret_key == 0);
    return secret_key;
}

void Shell() {
    char *cmd = "/bin/sh";
    char *args[] = {cmd, NULL};
    execve(cmd, args, NULL);
}

int main() {
    char buffer[0x10];
    int secret_key;
    int idx;
    srand(time(NULL));
    initialize(buffer, 0x10);
    secret_key = calculateSecretKey(buffer, 0x10);

    printf("Buffer idx: ");
    scanf("%d", &idx);

    if (idx >= 0 && idx < 0x10) {
        printf("%d\n", buffer[idx]);
    } else if (idx >= -0x10 && idx < 0) {
        printf("%d\n", *((int*)(buffer + idx)));
    } else {
        printf("Invalid index\n");
    }
    printf("secret_key address : %p\n",&secret_key);
    printf("Enter the key: ");
    scanf("%d", &idx);
    if (idx == secret_key) {
        Shell();
    } else {
        printf("Access denied\n");
    }

    return 0;
}