import java.util.Scanner;
public class Task11_3{
  public static void main(String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter a number: ");
    int x=sc.nextInt();
    int y=sc.nextInt();
    int product=x*y;
    int division=x/y;
    System.out.println(product);
    System.out.print(division);
  }
}
