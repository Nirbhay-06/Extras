public class rightTriangel {
    public static void main(String args[]){
        
        for(int i = 1; i <= 5 ;i++){
            //loop to print Blank Space.
            for(int j = 5; j > i ;j--){
                System.out.print(" ");
            }

            //loop to print the actual Star  Pattern.
            for(int j = 1; j <= i ; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
