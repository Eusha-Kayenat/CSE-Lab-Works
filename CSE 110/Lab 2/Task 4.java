import java.util.Scanner;
public class Task4{
  public static void main (String[]args){
     Scanner sc = new Scanner(System.in);
     System.out.println("Enter the number: ");
     int year = sc.nextInt();
     if((year%4==0 && year%100!=0)||(year%400==0)){
       System.out.print(year +" is a leap year");
     }
     else{
       System.out.print(year +" is not a leap year");
     }
  }
}
