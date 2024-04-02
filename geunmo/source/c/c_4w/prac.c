#include <stdio.h>

// Person 구조체 정의와 typedef
typedef struct {
    int id;
    int age;
} Person;

int main() {
    // 두 명의 사람 정보를 저장할 구조체 배열 선언
    Person people[2];

    // 첫 번째 사람 정보 입력
    printf("첫 번째 사람 정보 입력\n");
    printf("ID: ");
    scanf("%d", &people[0].id);
    printf("나이: ");
    scanf("%d", &people[0].age);

    // 두 번째 사람 정보 입력
    printf("두 번째 사람 정보 입력\n");
    printf("ID: ");
    scanf("%d", &people[1].id);
    printf("나이: ");
    scanf("%d", &people[1].age);

    // 입력된 두 명의 사람 정보 출력
    printf("\n입력된 사람 정보:\n");
    printf("첫 번째 사람 - ID: %d, 나이: %d\n", people[0].id, people[0].age);
    printf("두 번째 사람 - ID: %d,  나이: %d\n", people[1].id, people[1].age);

    return 0;
}