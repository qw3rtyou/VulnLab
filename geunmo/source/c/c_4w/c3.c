#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int id;
    char name[50];
    int age;
} Person;

int main() {
    printf("%ld\n",sizeof(Person));
    int num_people;

    scanf("%d", &num_people);

    Person *people = (Person *)malloc(num_people * sizeof(Person));

    free(people);

    return 0;
}