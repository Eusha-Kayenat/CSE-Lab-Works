import java.util.Scanner;
public class Task9 {
 public static int sumDigits(int num) {
  if (num<10){
   return num;
  }
   return ((num%10)+sumDigits(num/10));
  }
 
 public static void main(String[] args) {
   Scanner sc = new Scanner(System.in);
   System.out.print("Enter the value of n: ");
   int num = sc.nextInt(); 
   int result= sumDigits(num);
   System.out.println(result);
 }
 }
