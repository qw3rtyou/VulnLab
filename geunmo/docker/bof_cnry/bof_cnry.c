#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

void alarm_handler()
{
    puts("TIME OUT");
    exit(-1);
}

void initialize()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    signal(SIGALRM, alarm_handler);
    alarm(30);
}

void shell()
{
    system("/bin/sh");
}
void inputComment(char* comment){
    printf("plz input your comment!\n>> ");
    read(0,comment,100);
    printf("Your comment : ");
    while(*comment != '\0'){
        printf("%c",*comment++);
    }
    printf("\n");
}

int main()
{
    char comment[30];
    char check[3];
    char* p = comment;

    initialize();

    inputComment(comment);

    printf("Want to change comment?(yes/no): ");
    scanf("%s", &check);

    if (strcmp(check, "yes") == 0){
        int len = strlen(comment);
        memset(comment,'\0',len * sizeof(char));
        inputComment(comment);
    }
    else if (strcmp(check, "no") == 0){
        printf("Thank you:)\n");
    }
    else {
        printf("Invalid input.\n");
    }
    return 0;

}

// gcc -fstack-protector -z execstack -no-pie -fno-pie -o bof_cnry bof_cnry.c