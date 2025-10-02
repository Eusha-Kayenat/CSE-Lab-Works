import java.util.Scanner;
public class Task11_4{
  public static void main(String[]args){
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter a number: ");
    double x=sc.nextDouble();
    double y=sc.nextDouble();
    double sum=x+y;
    double product=x*y;
    double division=x/y;
    System.out.println(sum);
    System.out.println(product);
    System.out.print(division);    
  }
}
