#include <stdio.h>

typedef int IntArray[5];

int sub(IntArray arr) {
    int num = 0;
    for (int i = 0; i < 5; ++i) {
        num += arr[i];
    }
    return num;
}

int main() {
    IntArray numbers = {1, 2, 3, 4, 5};

    int res = sub(numbers);
    
    printf("%d\n", res);

    return 0;
}

//1. IntArray numbers = {1, 2, 3, 4, 5}; 와 int numbers[5] = {1, 2, 3, 4, 5}; 은 같은 의미이다.
//2. IntArray numbers[2] 라고 선언하면 2차원 배열이 선언된다.
//3. sub 함수의 반환형, int를 IntArray로 변경가능하다.
//4. numbers의 5개의 수를 모두 더하는 코드이다.