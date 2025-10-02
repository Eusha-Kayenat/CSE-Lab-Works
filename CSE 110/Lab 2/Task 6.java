import java.util.Scanner;
public class Task6{
  public static void main (String[]args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter an input:");
    int num = sc.nextInt();
    if (num<0){
      num*=2;
      System.out.print("output: "+ num);
    }
    else if (num>=0 && num<2){
      num+=1;
      System.out.print("output: "+ num);
    }
    else if(num>=2 && num<5){
      num=(num*num)-1;
      System.out.print("output: "+ num);
    }
    else{
      num=(3*(num*num)+2);
      System.out.print("output: "+ num);
    }
  }
}
