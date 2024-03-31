#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// 주어진 문자열을 디코딩하여 반환하는 함수
bool easyEncrypt(const char *input) {
    char flag[] = "CuhbXbV3WLbPhpehuBKdKDKC"; 
    char decoded[strlen(input) + 1]; // 디코딩된 문자열을 저장할 버퍼

    // 입력값을 -3만큼 이동하여 디코딩
    for (int i = 0; input[i] != '\0'; i++) {
        decoded[i] = input[i] + 3;
    }
    decoded[strlen(input)] = '\0'; // 문자열 끝에 널 문자 추가

    // 디코딩된 문자열과 flag를 비교하여 일치하는지 확인
    if (strcmp(decoded, flag) == 0) {
        return true; // 일치하면 true 반환
    } else {
        return false; // 일치하지 않으면 false 반환
    }
}

int main() {

    printf("1. 문제 소개\n");
    printf("2. 패스워드 입력\n");

    int choice;
    printf("번호를 입력하세요: ");
    scanf("%d", &choice);

    if (choice == 1) {
        printf("SOTI만 공유하고 있는 비밀번호가 있다는 정보를 입수했다.\n해당 정보는 동아리원들이 게으른 관계로 약한 강도로 암호화 되있다고 하는데... 비밀번호를 알아낼 수 있을까?\n");
    } else if (choice == 2) {
        char input_password[50];
        printf("패스워드를 입력하세요: ");
        scanf("%50s", input_password); // 버퍼 오버플로우를 방지하기 위해 입력 크기를 제한합니다.

        if(easyEncrypt(input_password)){
            printf("정답입니다! 너무 쉬웠나요?\n");
            printf("정답은! SOTI{%s}", input_password);
        } 
        else {
            printf("ㅋ\n");
        }
        
    } else {
        printf("잘못된 선택입니다. 숫자 1 or 2만 입력하세요.\n");
    }

    return 0;
}
