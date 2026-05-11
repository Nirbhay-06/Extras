public class rightInvertedtriangle {

    public static void main(String args[]){
        for(int i=1;i<=5 ;i++){
            //Space loop.
            for(int j=1;j<i;j++){
                System.out.print(" ");
            }

            //Pattern loop.
            for(int j=i;j<=5;j++){
                System.out.print("*");
            }

            System.out.println();
        }
    }
    
}
