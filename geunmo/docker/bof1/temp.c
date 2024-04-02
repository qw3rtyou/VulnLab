#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void alarm_handler() {
    puts("TIME OUT");
    exit(-1);
}


void initialize() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    signal(SIGALRM, alarm_handler);
    alarm(30);
}

int main(){
    char buffer[20];
    int i;
    initialize();
    
    printf("Input: ");
    scanf("%s",buffer);
    if (i == 1751212907){
        system("/bin/sh");
    }

    return 0;
}