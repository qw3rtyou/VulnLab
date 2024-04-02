#include <stdio.h>
#define NUM1 2
#define NUM2 3
#define NUM3 4
int main(){
    int arr[NUM1][NUM2][NUM3] = {
        {{1,2,3,4},{5,6,7,8},{9,10,11,12}}
        ,
        {{12,11,10,9},{8,7,6,5},{4,3,2,1}}
    };
    for (int i = 0; i < NUM1; i++){
        for (int j = 0; j < NUM2; j++){
            for (int k = 0; k < NUM3; k++){
                if (i == 1){
                    arr[i][j][k] = 0;
                }
                if (j % 2 == 0){
                    arr[i][j][k] = arr[i][j][k] / 2;
                }
                if (k < 1 || k > 2){
                    arr[i][j][k] = 1;
                }
            }
        }
    }
    for (int i = 0; i < NUM1; i++){
        for (int j = 0; j < NUM2; j++){
            for (int k = 0; k < NUM3; k++){
                printf("%d ",arr[i][j][k]);
            }
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}
