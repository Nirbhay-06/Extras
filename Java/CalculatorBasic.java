import java.util.Scanner;


public class CalculatorBasic{

    public static double sum(double num1, double num2){

        return num1 + num2;
    } 

    public static double sub(double num1, double num2){

        return num1 - num2;
    }

    public static double mult(double num1, double num2){
        return num1 * num2;
    }

    public static double div(double num1,double num2){
        if(num2 == 0 ){
            System.out.printf("Not divisible by ZERO");
            return -0;
        }

        return num1/num2;

    }

    public static void main(String args[]){
        Scanner read = new Scanner(System.in);

        System.out.print("Enter a Number : ");
        double number1=read.nextDouble();

        System.out.print("Enter the Operation : ");
        String operation=read.next();
       
        System.out.print("Enter another number : ");
        double number2=read.nextDouble();

        if(operation.equals("+")){
            System.out.printf("The addition of the numbers %.2f and %.2f is %.2f",number1,number2,sum(number1,number2));
        }
        else if(operation.equals("-")){
           System.out.printf("The Subtraction of the number %.2f and %.2f is %.2f",number1,number2,sub(number1,number2));
        }
        else if(operation.equals("*")){
            System.out.printf("The multiplication of the numbers %.2f and %.2f is %.2f",number1,number2,mult(number1,number2));
        }
        else if(operation.equals("/")){
            System.out.printf("The Divion of the numbers %.2f and %.2f is %.2f",number1,number2,div(number1,number2));
        }
        else{
            System.out.println("Invalid Operation!!");
        }
        read.close();
    }
}