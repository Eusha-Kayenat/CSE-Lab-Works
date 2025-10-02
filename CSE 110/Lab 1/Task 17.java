import java.util.Scanner;
public class Task17{
  public static void main(String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter a number: ");
    int a=sc.nextInt();
    int b=sc.nextInt();
    int c=sc.nextInt();
    int d=(2*b*((c-a)/3))+7;
    System.out.print(d);
  }
}
