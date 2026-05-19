
import java.util.Scanner;
import java.util.InputMismatchException;

public class queueUsingArray {

    private int[] Queue;
    private int capacity;
    private int front,rear;

    queueUsingArray(int size){
        Queue = new int[size];
        capacity = size - 1;
        front = -1;
        rear = -1;
    }

    void insert(int ele){
        if(rear == capacity ){
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

    void display(){
        if(front == -1 | rear == -1){
            System.out.println("The Queue is Empty!!");
            return;
        }
        else{
            System.out.print("Elements in the Queue are(front --> rear): ");
            int start = front;
            for(int i = start; i<= rear; i++){
                System.out.printf("%d -> ",Queue[i]);

            }
            System.out.println("Null");
        }
    }

    void search(int target){
        for(int i = front; i<=rear ; i++){
            if(target == Queue[i]){
                System.out.printf("Element found at position %d\n",i);
                return;
            }
        }
        System.out.println("Element not found.");
    }

    void isEmpty(){
        if(front == -1 | rear == -1){
            System.out.println("The Queue is Empty!!");
            return;
        }
        else{
            System.out.println("Queue is not empty!!");
        }
    }


    public static void main(String args[]){
        Scanner read = new Scanner(System.in);

        System.out.println("Enter the size of the Queue: ");
        int size = read.nextInt();

        queueUsingArray queue = new queueUsingArray(size);
        loop1:
        while(true){
            int option = -1;
            try{
                System.out.printf("1. Insertion\n2. Deletion\n3. Transverse\n4. Search\n5. isEmpty\n0. Exit\nChoose an Option: ");
                option = read.nextInt();
            }
            catch(InputMismatchException e){
                System.out.println("Choose the number before the Operation.");
                read.nextLine();
                
            }

            switch(option){
                case 0:
                    System.out.println("Exiting..................");
                    break loop1;

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
                    int target = read.nextInt();
                    queue.search(target);
                    break;
                

                case 5:
                    queue.isEmpty();
                    break;

                default:
                    System.out.println("Option Invalid");
                    break;
            }
        }

        read.close();
    }
    
}
