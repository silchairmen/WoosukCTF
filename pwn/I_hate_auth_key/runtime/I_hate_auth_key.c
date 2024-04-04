// Compile: gcc -o I_hate_auth_key I_hate_auth_key.c -fno-stack-protector -no-pie

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>

char FLAG[0x20];

void alarm_handler(int signum) {
    printf("30초가 경과하여 프로그램을 종료합니다.\n");
    exit(0);
}

void init() {
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
}

void Shell() {
    char *cmd = "/bin/sh";
    char *args[] = {cmd, NULL};
    execve(cmd, args, NULL);
}

char *generate_random_key() {
    char *key = (char *)malloc(17 * sizeof(char)); 
    const char *charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    for (int i = 0; i < 16; i++) {
        key[i] = charset[rand() % 62];
    }
    key[16] = '\0';

    return key;
}

int main() {
    char auth_key[0x10];

    init();
    signal(SIGALRM, alarm_handler);
    alarm(30);
    puts("Input :");

    scanf("%s", auth_key);

    if (strcmp(generate_random_key(), auth_key) == 0) {
        printf("%s",FLAG);
    }

    return 0;
}
