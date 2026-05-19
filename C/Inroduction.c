#include<stdio.h>

int main(){

    char name[10];
    int age;

    printf("Enter Your Name: ");
    scanf("%s",&name);

    printf("Enter Your Age: ");
    scanf("%d",&age);

    printf("Hello %s you are %d years Old.",name,age);
    
    return 0;
}