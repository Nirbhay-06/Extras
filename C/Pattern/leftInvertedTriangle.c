#include<stdio.h>

int main(){
    //Taking user input for number of rows.
    printf("Enter the number of rows: ");
    int row;
    scanf("%d",&row);
    //loop to print the pattern.
    for(int i = 0;i < row; i++){
        for(int j = 0;j < row - i; j++){
            printf("* ");
        }
        printf("\n");

    }
    return 0;
}