import java.util.Scanner;
public class Task5{
  public static void main (String[]args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter an input:");
    int num = sc.nextInt();
    if (num==0){
      System.out.print("Number is zero");
    }
    else if (num<0){
      System.out.print("Number is negative");
    }
    else if(num>0 && num%2==0){
      System.out.print("Number is positive and even");
    }
    else{
      System.out.print("Number is positive and odd");
    }
  }
}
