import java.util.Scanner;
public class Task2{
  public static void main(String[]args){
    Scanner sc=new Scanner(System.in);
       boolean j =true;
      for(int i=1;j==true;i++){
      System.out.println("Enter Number: ");
      int num=sc.nextInt();
      int square_val=0;
      if (num>0){
        square_val=num*num;
        System.out.println(square_val);
        j =true;
      }
      else{
         j =false;
      }
    }
  }
}
