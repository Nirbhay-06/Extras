
import java.util.InputMismatchException;
import java.util.Scanner;

class stackUsingArray{
    private int STK[];
    private int size;
    private int top;

    public stackUsingArray(int capacity){
        STK = new int[capacity];
        size = capacity;
        top = -1;
    }

    public void push(int ele){
        if(top == size - 1){
            System.out.println("Stack is overflow!");
            return;
        }
        top = top +1;
        STK[top]=ele;
        System.out.printf("Inserted element %d at position %d",ele,top);
    }

    public void pop(){
        if(top == -1){
            System.out.println("Stack is Undeflow"); 
        }
        else{
            System.out.printf("Element %d removed form position %d\n",STK[top],top);
            top = top - 1;
        }
    }

    public void display(){
        if(top == -1){
            System.out.println("Stack is Empty");
        }
        else{
            for(int i = 0;i <= top ;i++){
                System.out.printf("%d -> ",STK[i]);
            }
            System.out.println("Null");
        }
    }

    public void size(){
        System.out.printf("The number of element in the stack are : %d",top+1);
    }

    public void search(int target){
        if(top == -1){
            System.out.println("Stack is Empty");
        }
        else{
            for(int i = 0 ; i<=top ; i++){
                if(STK[i] == target){
                    System.out.printf("Element found at position %d\n",i);
                    return;
                }

            }
            System.out.println("Element NOT found");

        }
    }
    public static void main(String args[]){
        Scanner read = new Scanner(System.in);

        System.out.print("Enter the Size of the Stack : ");
        int capacity = read.nextInt();

        if(capacity <= 0){
            System.out.println("Capacity cannot be in Negative.");
            read.close();
            return;
        }

        stackUsingArray stk = new stackUsingArray(capacity);
        System.out.printf("Stack Created with size %d\n",capacity);


        loop:
        while (true) {
            int option;
            try{
                System.out.printf("Enter a Operation\n1. Push\n2. Pop\n3. Display\n4. Search\n5. Size\n0. Exit\n Option: ");
                option = read.nextInt();
            }
            catch(InputMismatchException e){
            read.nextLine();
                System.out.println("Enter a the number before the operation.");
                continue;
            }

            switch(option){
                case 0:
                    System.out.println("Exiting............");
                    break loop;
                
                case 1:
                    System.out.print("Enter an element to insert: ");
                    int ele = read.nextInt();
                    stk.push(ele);
                    break;

                case 2:
                    stk.pop();
                    break;

                case 3:
                    stk.display();
                    break;

                case 4:
                    System.out.print("Enter a element to search: ");
                    int target = read.nextInt();
                    stk.search(target);
                    break;

                case 5:
                    stk.size();
                    break;

                default:
                    System.out.println("Invalid Input/Option");
                    break;
                
                
            }

       }


        read.close();
    }
}