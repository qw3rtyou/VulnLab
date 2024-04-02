#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char *str;
    int num;
    char buf[100]; 

    fgets(buf, sizeof(buf), stdin);

    num = strlen(buf);

    str = (char*)malloc(num * sizeof(char));

    if (str == NULL){
        //실행코드
        return 1;
    }

    strcpy(str,buf);

    return 0;
}

// 1. 문자열을 입력받고 str과 buf를 비교하는 코드이다.
// 2. 17번의 실행코드에는 malloc을 성공했을 때 실행될 코드를 넣으면 된다.
// 3. num은 100이다.
// 4. 15번 줄의 malloc을 호출하면 num 바이트 크기의 메모리 공간이 할당된다.