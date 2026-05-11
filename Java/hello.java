import java.util.Scanner;

class hello{
    public static void main(String args[]){
        Scanner read = new Scanner(System.in);
        
        System.out.print("Enter your name : ");
        String name=read.nextLine();

        System.out.print("Enter your age : ");
        int age=read.nextInt();

        System.out.println("Hello " + name + " you are " +  age +" years old");
        
        read.close();

    }
}