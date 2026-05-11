import java.util.Scanner;

public class PatternPrinter {

    public static void leftSideTriangle(char pattern,int row){
        System.out.println("Printing Left Side Triangle.");
        for(int i = 1;i<=row;i++){
            for(int j=1;j<=i;j++){
                System.out.printf("%c",pattern);
            }
            System.out.println();
        }        

    }


    public static void leftInvertedTriangle(char pattern,int row){
        System.out.println("Printing Left Side Inverted Triangle.");
        for(int i = row; i >= 1 ; i--){
            for(int j = 1; j <= i ; j++){
                System.out.printf("%c",pattern);
            }
            System.out.println();
        }
    }

    public static void rightTriangle(char pattern, int row){
        System.out.println("Printing Rigth Side Triangle.");
        for(int i = 1; i <= row ;i++){
            //loop to print Blank Space.
            for(int j = row; j > i ;j--){
                System.out.print(" ");
            }

            //loop to print the actual Star  Pattern.
            for(int j = 1; j <= i ; j++){
                System.out.printf("%c",pattern);
            }
            System.out.println();
        }
    }

    public static void rightInvertedTriangle(char pattern,int row){
        System.out.println("Printing Right Side Inverted Triangle.");
        for(int i=1;i<=row ;i++){
            //Space loop.
            for(int j=1;j<i;j++){
                System.out.print(" ");
            }

            //Pattern loop.
            for(int j=i;j<=row;j++){
                System.out.printf("%c",pattern);
            }

            System.out.println();
        }
    }


    public static void main(String args[]){
        Scanner read = new Scanner(System.in);
        System.out.print("Enter the Symbol for pattern: ");
        char pattern = read.next().charAt(0);

        System.out.print("Enter the number of rows: ");
        int row = read.nextInt();

        leftSideTriangle(pattern, row);
        leftInvertedTriangle(pattern, row);
        rightTriangle(pattern, row);
        rightInvertedTriangle(pattern, row);




        read.close();
    }
}
