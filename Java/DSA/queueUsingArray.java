
import java.util.Scanner;
import java.util.InputMismatchException;

public class queueUsingArray {

    private int[] Queue;
    private int capacity;
    private int front,rear;

    queueUsingArray(int size){
        Queue = new int[size];
        front = -1;
        rear = -1;
    }

    void insert(int ele){
        if(rear == capacity){
            System.out.println("Queue is Overflow.");
            return;
        }

        rear++;
        Queue[rear]=ele;
        if(front == -1){
            front++;
        }
    }

    void delete(){
        if(front == -1 | rear == -1){
            System.out.println("Queue is Underflow");
            return;
        }

        System.out.printf("Element removed is %d\n",Queue[front]);
        front++;
        if(front == rear){
            front=0;
            rear=0;

        }
        if(front > rear){
            front = -1;
            rear = -2;
        }
    }


    public static void main(String args[]){
        Scanner read = new Scanner(System.in);

        System.out.println("Enter the size of the Queue: ");
        int size = read.nextInt();

        queueUsingArray queue = new queueUsingArray(size);

        int option = -1;
        try{
            System.out.printf("""
            1. Insertion\n
            2. Deletion\n
            3. Transverse\n
            4. Search\n
            5. isEmpty\n
            0. Exit\n
            Choose an Option:     
            """);
            option = read.nextInt();
        }
        catch(InputMismatchException e){
            System.out.println("Choose the number before the Operation.");
            read.nextLine();
               
        }

        switch(option){
            case 0:
                System.out.println("Exiting..................");
                break;

            case 1:
                System.out.print("Enter an element to Insert: ");
                int element = read.nextInt();
                queue.insert(element);
                break;
            
            case 2:
                queue.delete();
                break;

            case 3:
                queue.display();
                break;

            case 4:
                System.out.println("Enter an element to search: ");
                int element = read.nextInt();
                queue.search(element);
                break;
            

            case 5:
                queue.isEmpty();
                break;

            default:
                System.out.println("Option Invalid");
                break;
        }

        read.close();
    }
    
}
