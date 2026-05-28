#include<stdio.h>

int main(){
    printf("Enter the number of rows: ");
    int row;
    scanf("%d",&row);


    for(int i=0;i<=row;i++){
        for(int j=0;j<i;j++){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}