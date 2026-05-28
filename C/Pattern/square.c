#include<stdio.h>

int main(){
    printf("Enter the number of rows: ");
    int row;
    scanf("%d",&row);

    printf("Enter the number of colums: ");
    int column;
    scanf("%d",&column);
    
    for(int i=0;i<row;i++){
        for(int j=0;j<column;j++){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}