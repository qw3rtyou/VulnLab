#include <stdio.h>
#include <stdlib.h>

int main(){
    int *arr;
    int num;

    scanf("%d",&num);

    arr = (int*)calloc(num, sizeof(int));
    if (arr == NULL){
        //실행문장
        return 1;
    }

    for (int i = 0; i < num; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < num; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    int new_num;
    scanf("%d", &new_num);

    arr = (int *)realloc(arr, num * sizeof(int));

    if (arr == NULL){
        //실행문장
        return 1;
    }

    for (int i = new_num; i < new_num; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < new_num; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // free(arr);
    
    return 0;
}

// 1. 만약 num보다 new_num이 더 크다면 39번 줄의 출력문과 20번 줄의 출력문을 비교 했을 때 서로 다른 값은 calloc으로 인해 모두 0이다.
// 2. 컴파일 오류가 발생한다.
// 3. realloc을 해도 값은 원래의 값은 변하지 않는다.
// 4. free()를 하지 않으면 컴파일이 되지 않는다.



//arr = (int *)realloc(arr, num * sizeof(int));