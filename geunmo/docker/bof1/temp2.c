#include <stdio.h>
#include <stdlib.h>

int main(void){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("Hello\n");
    system("/bin/sh");

    return 0;

}