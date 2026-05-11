import java.util.Scanner;

public class CalcuatorAdvance {
    public static void main(String args[]){

        Scanner read = new Scanner(System.in);
        System.out.print("Enter a number: ");
        double num1 = read.nextDouble();

        double result = 0;
        while(true){
            System.out.print("Enter Operation(+ , - ,/ ,* ,= ) : ");
            String operation = read.next();

            if(operation.equals("=")){
                System.out.printf("Result = %.2f",result);
                return;
            }
            else {
            
                System.out.print("Enter another Number : ");
                double num2 = read.nextDouble();

                if(operation.equals("+")){
                    result = num1 + num2;
                    num1 = result;
                }
                else if(operation.equals("-")){
                    result = num1 - num2;
                    num1 = result;
                }
                else if(operation.equals("*")){
                    result = num1 * num2;
                    num1 = result;
                }
                else if(operation.equals("/")){
                    if(num2 == 0){
                        System.out.println("Not Divisible by ZERO");
                        return;
                    }
                    else{
                        result = num1 / num2;
                        num1 = result;
                    }
                }
                
                else{
                    System.out.println("Invalid Operation!!");
                    break;
                }
            }
        }

        read.close();

    }
}
