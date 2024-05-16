#include <stdio.h>
#include <windows.h>
#include <string.h>

#define KEY1 0xA3
#define KEY2 0x5F
#define KEY3 0xC7

// func1: 가짜
void func1() {
    volatile int x = 17, y = 0;
    while (x-- > 0) {
        for (int i = 0; i < 7; i++) {
            y += i * x;
        }
        if (y % 3 == 0) {
            y /= 3;
        } else {
            y = (y * 2) + 1;
        }
    }
}

// func2: 가짜
void func2(int n) {
    if (n <= 1) return;
    func2(n - 2);
    volatile int dummy = n % 5;
}

// func3: 가짜
void func3() {
    char buffer[15];
    for (int i = 0; i < sizeof(buffer); i++) {
        buffer[i] = (i * 37) % 256;
    }
    volatile char result = buffer[4] + buffer[9];
}

// func4: 가짜
void func4() {
    volatile int randValue = 0;
    for (int i = 0; i < 10; i++) {
        randValue += (i * i) % 4;
    }
}

// func5: 가짜
void func5() {
    volatile double value = 1.0;
    for (int i = 1; i <= 5; i++) {
        value *= i / (value + i);
    }
}

// flag: flag 출력
void flag(char* encoded_file, char* decoded_str) {
    FILE* fp = fopen(encoded_file, "rb");
    if (fp == NULL) {
        printf("Failed to open file for reading.\n");
        return;
    }

    func1(); // 가짜

    int i = 0;
    unsigned char encoded;
    while (fread(&encoded, sizeof(unsigned char), 1, fp) == 1) {
        func2(i); // 가짜

        encoded ^= (i * 3) & 0xFF;

        func3(); // 가짜
        encoded = (encoded & 0xF0) >> 4 | (encoded & 0x0F) << 4;
        encoded ^= (i % 2) ? KEY2 : KEY3;
        encoded ^= KEY1;
        encoded = (encoded << 5) | (encoded >> 3);

        decoded_str[i++] = encoded;

        if (i % 2 == 0) func4(); // 가짜
    }
    decoded_str[i] = '\0';

    func5(); // 가짜

    fclose(fp);
    printf("flag: SOTI{%s}\n", decoded_str);
}

int main(){
	char encoded_file[] = "encoded.bin";
	char decoded_str[30];

	printf("  ^--^\n");
	printf("_(´ω`_)⌒)_\n");
	printf("Sleep .....\n\n");
	Sleep(1000000000000000000000);
	
	
	printf("Oh.. Wa...ke... up..?\n\n");
	Sleep(2000);
	
	printf("  ^--^\n");
	printf("_(´ω`_)⌒)_\n");
	printf("No... Sleep .....\n\n");
	Sleep(1000000000000000000000);
	
	printf("  ^--^\n");
	printf("_('ω'_)⌒)_\n");
	printf("Wake UP :) \nWait! I will give you flag!!! \n");
	
	Sleep(1000);
	printf("\n");
	
	flag(encoded_file, decoded_str);
	
	system("pause"); 
}

